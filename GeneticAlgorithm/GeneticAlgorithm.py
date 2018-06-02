import random
import copy
import heapq
import numpy as np
import time
from .Chromossome import Chromossome


class GeneticAlgorithm:

    def __init__(self, chromossome, pop_size=50, max_no_improv=200, mutation_rate=0.1, elitism_rate=0.1, k=4, out_filename=None, time_limit=600):

        self.pop_size = pop_size
        self.population = [chromossome] + [Chromossome(chromossome.size, chromossome.l) for _ in range(self.pop_size - 1)]
        self.max_no_improv = max_no_improv
        self.count_no_improv = 0
        self.old_solution = 0
        self.termination_criteria = termination_criteria
        self.crossover = uniform_crossover
        self.selection = tournament_selection
        self.fitness_function = None
        self.mutation_rate = mutation_rate
        self.elitism_rate = elitism_rate
        self.k = k
        self.best_solution = None
        self.generation = 1
        self.out_file = out_filename
        self.start_time = None
        self.time_limit = time_limit
        if out_filename is not None:
            self.out_file = open(out_filename, 'a')

    def evolve(self):
        self.start_time = time.time()

        # First generation
        self.best_solution = self.population[0]
        self.eval(self.population)
        self.best_solution = max(self.population, key=lambda x: x.fitness)
        self.old_solution = self.best_solution.fitness

        print("Generation {} ".format(self.generation), end='')
        print(self.best_solution)

        self.generation += 1
        while not self.termination_criteria(self):
            next_pop = []

            # Selection and Reprodution
            num_new_child = int((1 - self.elitism_rate) * self.pop_size)
            while len(next_pop) < num_new_child:
                father = self.selection(self.population, self.k)
                mother = self.selection(self.population, self.k)
                child1, child2 = self.crossover(father, mother)
                next_pop.extend([child1, child2])

            # Mutation
            for c in next_pop:
                c.turn_feasible()
                if random.random() < self.mutation_rate:
                    c.mutate()

            # Evaluation
            self.eval(next_pop)

            # Elitism
            next_pop.extend(heapq.nlargest(self.pop_size - len(next_pop), self.population, key=lambda x: x.fitness))

            # Update population
            self.population = next_pop

            print("Generation {} ".format(self.generation), end='')
            print(self.best_solution)

            self.generation += 1

        total_time = time.time() - self.start_time
        if self.out_file is not None:
            self.out_file.write("{} {}\n".format(self.best_solution.fitness, total_time))
            self.out_file.close()
        print("Time elapsed = {} seconds".format(total_time))

    def eval(self, chromossomes):
        for c in chromossomes:
            c.fitness = self.fitness_function(c.genes)
            if c.fitness > self.best_solution.fitness:
                self.best_solution = c

        if self.best_solution.fitness == self.old_solution:
            self.count_no_improv += 1
        else:
            self.count_no_improv = 0
            self.old_solution = self.best_solution.fitness


def uniform_crossover(genome1, genome2):
    child1 = copy.deepcopy(genome1)
    child2 = copy.deepcopy(genome2)
    mask = [random.random() < 0.5 for _ in range(genome1.size)]
    for index, n in enumerate(mask):
        if n:
            child1.genes[index], child2.genes[index] = child2.genes[index], child1.genes[index]

    return child1, child2


def termination_criteria(ga):
    if ga.count_no_improv > ga.max_no_improv or ga.time_limit <= (time.time() - ga.start_time):
        return True
    else:
        return False


def tournament_selection(pop, k):
    '''
    Tournament Selection
    Return the best genome from a sample of the population of size k
    :param pop: The population from which the genome will be selected
    :return: The genome selected
    '''
    return max(random.sample(pop, k), key=lambda g: g.fitness)
