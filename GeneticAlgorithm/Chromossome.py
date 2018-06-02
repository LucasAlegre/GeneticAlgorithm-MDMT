import random
import numpy as np


class Chromossome:

    def __init__(self, size, l, alleles=None):

        self.fitness = None
        self.size = size
        self.l = l
        if alleles is None:
            self.genes = np.full(self.size, False)
            inds = np.random.choice(self.genes.size, size=l, replace=False)  # Get l random indices
            self.genes[inds] = True
        else:
            self.genes = alleles

    def mutate(self):
        i1, i2 = random.randint(0, self.size-1), random.randint(0, self.size-1)
        self.genes[i1], self.genes[i2] = self.genes[i2], self.genes[i1]

    def turn_feasible(self):

        difference = self.l - np.sum(self.genes)
        if difference != 0:
            if difference < 0:
                inds = np.random.choice(np.where(self.genes == True)[0], size=abs(difference), replace=False)
                self.genes[inds] = False
            else:
                inds = np.random.choice(np.where(self.genes == False)[0], size=difference, replace=False)
                self.genes[inds] = True

    def __str__(self):

        # return 'Genome=(' + ' '.join(["{}".format(i) for i in self.alleles]) + ') Fitness=' + str(self.fitness)
        # return 'Num = ' + str(np.sum(self.genes)) + ' Fitness=' + str(self.fitness) + ' ' + str(Chromossome.C) + ' ' + str(Chromossome.T)
        return 'Fitness=' + str(self.fitness)