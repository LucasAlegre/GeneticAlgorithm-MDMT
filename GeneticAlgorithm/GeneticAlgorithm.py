import random
import copy
import heapq
import numpy as np
import time
from .Genome import Genome


class GeneticAlgorithm:

    def __init__(self, genome, pop_size=50, num_generations=100, mutation_rate=0.01, elitism_rate=0.1, out_filename=None):

        self.pop_size = pop_size
        self.population = [genome] + [Genome(genome.size, genome.l) for _ in range(self.pop_size - 1)]
        self.num_generations = num_generations
        self.termination_criteria = gen_limit_termination_criteria
        self.crossover = uniform_crossover
        self.selection = tournament_selection
        self.fitness_function = None
        self.mutation_rate = mutation_rate
        self.elitism_rate = elitism_rate
        self.best_genome = None
        self.generation = 1
        self.out_file = out_filename
        if out_filename is not None:
            self.out_file = open(out_filename, 'w+')

    def evolve(self):
        start = time.time()

        # First generation
        self.eval(self.population)
        self.best_genome = max(self.population, key=lambda x: x.fitness)
        self.generation += 1

        print("Generation {} ".format(self.generation), end='')
        print(self.best_genome)
        if self.out_file is not None:
            self.out_file.write("GA - pop_size={} mutation_rate={} elitism_rate{}\n".format(self.pop_size, self.mutation_rate, self.elitism_rate))
            self.out_file.write("{} {}\n".format(self.generation, self.best_genome.score))

        while not self.termination_criteria(self):
            next_pop = []

            # Selection and Reprodution
            num_new_child = int((1 - self.elitism_rate) * self.pop_size)
            while len(next_pop) < num_new_child:
                father = self.selection(self.population)
                mother = self.selection(self.population)
                child1, child2 = self.crossover(father, mother)
                next_pop.extend([child1, child2])

            # Mutation
            for g in next_pop:
                g.mutate(self.mutation_rate)

            # Evaluation
            self.eval(next_pop)
            self.best_genome = max(next_pop + [self.best_genome], key=lambda x: x.fitness)

            # Elitism
            next_pop.extend(heapq.nlargest(self.pop_size - len(next_pop), self.population, key=lambda x: x.fitness))

            # Update population
            self.population = next_pop

            print("Generation {} ".format(self.generation), end='')
            print(self.best_genome)
            if self.out_file is not None:
                self.out_file.write("{} {}\n".format(self.generation, self.best_genome.fitness))

            self.generation += 1

        total_time = time.time() - start
        if self.out_file is not None:
            self.out_file.write("Time elapsed = {}\n".format(total_time))
            self.out_file.close()
        print("Time elapsed = {}".format(total_time))

    def eval(self, genomes):
        for g in genomes:
            g.fitness = self.fitness_function(g.alleles)


def single_point_crossover(genome1, genome2):
    child1 = copy.deepcopy(genome1)
    child2 = copy.deepcopy(genome2)

    cut_index = random.randint(1, genome1.size - 2)
    child1.alleles[:cut_index], child1.alleles[cut_index:] = genome1.alleles[:cut_index], genome2.alleles[cut_index:]
    child2.alleles[:cut_index], child2.alleles[cut_index:] = genome2.alleles[:cut_index], genome1.alleles[cut_index:]

    return child1, child2


def uniform_crossover(genome1, genome2):
    child1 = copy.deepcopy(genome1)
    child2 = copy.deepcopy(genome2)
    mask = [random.random() < 0.5 for _ in range(genome1.size)]
    for index, n in enumerate(mask):
        if n:
            child1.alleles[index], child2.alleles[index] = child2.alleles[index], child1.alleles[index]

    return child1, child2


def gen_limit_termination_criteria(ga):
    if ga.generation > ga.num_generations:
        return True
    else:
        return False


def tournament_selection(pop):
    '''
    Tournament Selection
    Return the best genome from a sample of the population of size k = 3
    :param pop: The population from which the genome will be selected
    :return: The genome selected
    '''
    return max(random.sample(pop, 3), key=lambda g: g.fitness)


def spin_wheel_selection(pop):
    s = sum(g.fitness for g in pop)
    r = random.uniform(0, s)
    t = 0
    for g in pop:
        t += g.fitness
        if t >= r:
            return g