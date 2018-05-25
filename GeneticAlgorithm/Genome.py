import random
import copy
import numpy as np


class Genome:

    def __init__(self, size, l, alleles=None):

        self.fitness = None
        self.size = size
        self.l = l
        if alleles is None:
            self.alleles = np.full(self.size, False)
            inds = np.random.choice(self.alleles.size, size=l, replace=False)  # Get l random indices
            self.alleles[inds] = True
        else:
            self.alleles = alleles

    def mutate(self, mutation_rate):
        for i in range(self.size):
            if random.random() < mutation_rate:
                self.alleles[i] = np.logical_not(self.alleles[i])

    def __str__(self):

        # return 'Genome=(' + ' '.join(["{}".format(i) for i in self.alleles]) + ') Fitness=' + str(self.fitness)
        return 'Num = ' + str(sum(self.alleles)) + ' Fitness=' + str(self.fitness)