"""
Changelog:
    v1.0 - Changelog created. <04/10/2017>
    v1.1 - Function string bug corrected
    v1.2 - Git Repository created
    v2.0 - Included more constraints, which were causing some networks to give a wrong answer <10/03/2018>
Maintainer: Lucas Nunes Alegre (lucasnale@gmail.com)
Created (changelog): 04/10/2017
This module contains the System Optimal Solver, which calculates the SO of a network.
Warning: Use spaces instead of tabs, or configure your editor to transform tab to 4 spaces.
"""

import argparse
import os
import numpy as np
from docplex.mp.model import *
from GeneticAlgorithm.GeneticAlgorithm import GeneticAlgorithm
from GeneticAlgorithm.Genome import Genome


class MDMT:

    def __init__(self, instance_file):

        self.M, self.L, self.l, self.d = self.read_instance_file(instance_file)
        self.name = os.path.basename(instance_file)

    @staticmethod
    def read_instance_file(file):
        with open(file, 'r') as f:
            t = ' '.join(s.strip() for s in f.readlines())
            t = [int(float(x)) for x in t.split()]
            M, L, l = t[0], t[1], t[2]
            t = t[3:]
            d = np.zeros((M, L), dtype=np.int32)
            i = 0
            for ind in range(M):
                d[ind] = [x for x in t[i:i+L]]
                i += L
        return M, L, l, d

    def calculate_mdmt(self, x):
        mdmt = 0

        for i in range(self.M):
            mdmt += np.min(self.d[i][np.flatnonzero(x)])
        return mdmt - 100*(abs(sum(x) - self.l))

    def _init_cplex(self):

        self.model = Model(name=self.name)
        self.model.parameters.mip.strategy.nodeselect = 0  #DFS
        self.model.parameters.mip.strategy.variableselect = 3  #Strong Branching
        self.x_vars = None
        self.D_vars = None
        self.cplex_solution = None

        self._generate_vars()
        self._generate_objective_function()
        self._generate_constraints()

    def _generate_vars(self):

        self.x_vars = self.model.binary_var_list(self.L, name="x")
        self.D_vars = self.model.integer_var_list(self.M, lb=0, name="D")

    def _generate_constraints(self):

        self.model.add_constraint(sum(self.x_vars) == self.l)

        for i in range(self.M):
            for j in range(self.L):
                self.model.add_constraint(self.D_vars[i] <= self.d[i][j] + 100000*(1 - self.x_vars[j]))

    def _generate_objective_function(self):

        self.model.maximize(sum(self.D_vars))

    def solve_cplex(self, verbose=False):

        self._init_cplex()
        self.model.context.solver.log_output = verbose

        solution = self.model.solve()

        if solution:

            self.cplex_solution = solution.get_objective_value()

            if verbose:
                print(solution.display())
                print('MDMT = ' + str(self.cplex_solution))

        else:
            print('Error calculating MDMT!')

    def generate_lp(self):

        self._init_cplex()

        with open(self.name + '.lp', 'w') as lp_file:
            lp_file.write(self.model.export_as_lp_string())

    def solve_ga(self):

        genome = Genome(self.L, self.l)
        self.ga = GeneticAlgorithm(genome, pop_size=50, num_generations=10000, mutation_rate=0.01, elitism_rate=0.1)
        self.ga.fitness_function = self.calculate_mdmt
        self.ga.evolve()


if __name__ == '__main__':

    prs = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                  description="""MDMT Problem Solver""")
    prs.add_argument("-f", dest="file", required=True, help="The instance file.\n")

    prs.add_argument("-lp", action="store_true", default=False, help="Generate LP file of the problem.\n")

    prs.add_argument("-out", help="Output File name")

    prs.add_argument("-ga", action="store_true", default=False, help="Solve with Genetic Algorithm")

    prs.add_argument("-cplex", action="store_true", default=False, help="Solve with Cplex")

    args = prs.parse_args()

    m = MDMT(args.file)

    if args.cplex:
        m.solve_cplex(verbose=True)
        args.ga = False

    if args.ga:
        m.solve_ga()

    if args.lp:
        m.generate_lp()


