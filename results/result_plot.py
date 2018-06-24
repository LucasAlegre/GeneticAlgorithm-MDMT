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

    n_groups = 10

    cplex = (13.11, 9.84, 24.85, 9.08, 23.96, 6.43, 20.46, 7.08, 5.43, 4.59)
    media = (-1.5, 7.09, 5.05, 0.95, 4.45, 0.31, 3.25, 2.42, 2.95, 0.49)
    melhor = (-2.61, 6.32, 3.35, -1.15, 3.02, -0.97, 2.77, 0.98, 2.15, 0.09)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.2
    opacity = 1
    error_config = {'ecolor': '0.3'}

    rects1 = ax.bar(index, cplex, bar_width,
	        alpha=opacity, color='RoyalBlue', error_kw=error_config,
	        label='CPLEX', zorder=3)

    rects2 = ax.bar(index + bar_width, media, bar_width,
	        alpha=opacity, color='Goldenrod', error_kw=error_config,
	        label='AG - Valor Médio', zorder=3)

    rects3 = ax.bar(index + bar_width*2, melhor, bar_width,
	        alpha=opacity, color='Teal', error_kw=error_config,
	        label='AG - Melhor Valor', zorder=3)

    ax.set_xlabel('Instância')
    ax.set_ylabel('Desvio para o BKV (%)')
    ax.set_title('Comparação dos testes das instâncias')
    ax.set_xticks(index + bar_width)
    ax.set_yticks([i for i in range(-4,27,2)])
    ax.set_xticklabels(('mdmt39.112.A', 'mdmt39.112.B', 'mdmt39.225.A', 'mdmt39.225.B', 'mdmt40.56.A', 'mdmt40.56.B', 'mdmt40.112.A', 'mdmt40.112.B', 'mdmt40.225.A', 'mdmt40.225.B'))
    ax.legend()
    ax.yaxis.grid()

    fig.tight_layout()
    plt.show()


