import matplotlib.pyplot as plt
import sys
import re
import numpy as np
import os


if __name__ == '__main__':

    '''
    plt.figure(1)
    
    x = [i for i in range(100, 501, 100)]
    y_value = []
    y_time = []
    for filename in sorted(os.listdir(".")):
        if filename[0] == 'g':
            with open(filename, 'r') as f:
                v = 0
                t = 0.0
                for line in f.readlines():
                    va, ta = line.split()
                    v += int(va)
                    t += float(ta)
                y_value.append(v/5)
                y_time.append(t/5)
    plt.plot(x, [100*(6271-y)/6271 for y in y_value])
    plt.grid()
    plt.ylabel("Desvio médio para o BKV (%)")
    plt.xlabel("max_non_improving_generations")
    plt.title("max_non_impriving_generations vs. Desvio médio em relação ao BKV")

    plt.figure(2)
    plt.plot(x, y_time)
    plt.grid()
    plt.ylabel("Tempo de execução(segundos)")
    plt.xlabel("max_non_improving_generations")
    plt.title("max_non_impriving_generations vs. Tempo de execução")
    plt.show()
    '''
    '''
    plt.figure(1)

    x = [i for i in range(10, 81, 10)]
    y_value = []
    y_time = []
    for filename in sorted(os.listdir(".")):
        if filename[0] == 'p':
            with open(filename, 'r') as f:
                v = 0
                t = 0.0
                for line in f.readlines():
                    va, ta = line.split()
                    v += int(va)
                    t += float(ta)
                y_value.append(v/10)
                y_time.append(t/10)
    plt.plot(x, [100*(6271-y)/6271 for y in y_value])
    plt.grid()
    plt.ylabel("Desvio médio para o BKV (%)")
    plt.xlabel("population_size")
    plt.title("population_size vs. Desvio médio em relação ao BKV")

    plt.figure(2)
    plt.plot(x, y_time)
    plt.grid()
    plt.ylabel("Tempo de execução(segundos)")
    plt.xlabel("population_size")
    plt.title("population_size vs. Tempo de execução")
    plt.show()
    '''
    
    plt.figure(1)

    x = [i/100 for i in range(0, 51, 10)]
    y_value = []
    y_time = []
    for filename in sorted(os.listdir(".")):
        if filename[0] == 'e':
            with open(filename, 'r') as f:
                v = 0
                t = 0.0
                for line in f.readlines():
                    va, ta = line.split()
                    v += int(va)
                    t += float(ta)
                y_value.append(v/10)
                y_time.append(t/10)
    plt.plot(x, [100*(6271-y)/6271 for y in y_value])
    plt.grid()
    plt.ylabel("Desvio médio para o BKV (%)")
    plt.xlabel("elitism_rate")
    plt.title("elitism_rate vs. Desvio médio em relação ao BKV")

    plt.figure(2)
    plt.plot(x, y_time)
    plt.grid()
    plt.ylabel("Tempo de execução(segundos)")
    plt.xlabel("elitism_rate")
    plt.title("elitism_rate vs. Tempo de execução")
    plt.show()
    
    '''
    plt.figure(1)

    x = [i/100 for i in range(0, 101, 10)]
    y_value = []
    y_time = []
    for filename in sorted(os.listdir(".")):
        if filename[0] == 'm' and filename[1] != 'd':
            with open(filename, 'r') as f:
                v = 0
                t = 0.0
                for line in f.readlines():
                    va, ta = line.split()
                    v += int(va)
                    t += float(ta)
                y_value.append(v/5)
                y_time.append(t/5)
    plt.plot(x, [100*(6271-y)/6271 for y in y_value])
    plt.grid()
    plt.xticks(x)
    plt.ylabel("Desvio médio para o BKV (%)")
    plt.xlabel("mutation_rate")
    plt.title("mutation_rate vs. Desvio médio em relação ao BKV")

    plt.figure(2)
    plt.plot(x, y_time)
    plt.grid()
    plt.ylabel("Tempo de execução(segundos)")
    plt.xlabel("mutation_rate")
    plt.title("mutation_rate vs. Tempo de execução")
    plt.show()
    '''


