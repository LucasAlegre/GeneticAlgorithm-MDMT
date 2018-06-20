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
import random
from docplex.mp.model import *
from GeneticAlgorithm.GeneticAlgorithm import GeneticAlgorithm
from GeneticAlgorithm.Chromossome import Chromossome


class MDMT:

    def __init__(self, instance_file):

        self.M, self.L, self.l, self.d = self.read_instance_file(instance_file)
        self.name = os.path.basename(instance_file)
        self.model = None

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
        vertices_chosen = np.flatnonzero(x)
        for i in range(self.M):
            # Mínimo valor da linha do vértice Mi considerando apenas as colunas dos vértices L escolhidos
            mdmt += np.min(self.d[i][vertices_chosen])
        return mdmt

    def _init_cplex(self):
        if self.model is not None:
            return

        self.model = Model(name=self.name)
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

        big_constant = self.d.max()
        for i in range(self.M):
            for j in range(self.L):
                self.model.add_constraint(self.D_vars[i] <= self.d[i][j] + big_constant*(1 - self.x_vars[j]))

    def _generate_objective_function(self):

        self.model.maximize(sum(self.D_vars))

    def solve_cplex(self, verbose=False, time_limit=1800):

        self._init_cplex()
        self.model.context.solver.log_output = verbose
        self.model.set_time_limit(time_limit)

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

    def solve_ga(self, p, g, m, e, k, out_file, time_limit, seed):

        if seed is not None:
            np.random.seed(seed)
            random.seed(seed)

        chromossome = Chromossome(self.L, self.l)
        self.ga = GeneticAlgorithm(chromossome, pop_size=p, max_no_improv=g, mutation_rate=m, elitism_rate=e, k=k, out_filename=out_file, time_limit=time_limit)
        self.ga.fitness_function = self.calculate_mdmt
        self.ga.evolve()


def valid_rate(x):
    x = float(x)
    if x < 0 or x > 1:
        raise argparse.ArgumentTypeError("Rate must be between 0 and 1")
    return x


if __name__ == '__main__':

    prs = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                  description="""MDMT(Maior Distância Mínima Total) Solver""")
    prs.add_argument("-f", dest="file", required=True, help="The instance file.\n")

    prs.add_argument("-lp", action="store_true", default=False, help="Generate LP file of the problem.\n")

    prs.add_argument("-out", help="Output Filename, for best solution and time elapsed")

    prs.add_argument("-ga", action="store_true", default=False, help="Solve with Genetic Algorithm")
    prs.add_argument("-m", default=0.1, type=valid_rate, help="Mutation Rate of the Genetic Algorithm")
    prs.add_argument("-e", default=0.1, type=valid_rate, help="Elitism Rate of the Genetic Algorithm")
    prs.add_argument("-p", default=50, type=int, help="Population Size of the Genetic Algorithm")
    prs.add_argument("-g", default=200, type=int, help="Max Number Of Generations Without Improvement of the Genetic Algorithm")
    prs.add_argument("-t", default=600, type=float, help="Time Limit")
    prs.add_argument("-k", default=4, type=int, help="Number of Individuals Choosen on Tournament Selection")
    prs.add_argument("-s", type=int, help="Random Seed")

    prs.add_argument("-cplex", action="store_true", default=False, help="Solve with Cplex")

    args = prs.parse_args()

    m = MDMT(args.file)

    if args.cplex:
        m.solve_cplex(verbose=True, time_limit=args.t)
        args.ga = False

    if args.ga:
        m.solve_ga(p=args.p, g=args.g, m=args.m, e=args.e, k=args.k, out_file=args.out, time_limit=args.t, seed=args.s)

    if args.lp:
        m.generate_lp()


