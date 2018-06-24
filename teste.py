from subprocess import call
import os

if __name__ == '__main__':

    seeds = [7, 42, 100101, 9999, 381]
    #seeds = [12, 53, 1618468, 3574, 878]
    '''
    # max_non_improving_generations
    for g in range(100, 501, 100):
        for s in seeds:
            call("python3 MDMT.py -f mdmt/mdmt40.112.A.ins -ga -g {} -p {} -m {} -e {} -s {} -out {}".format(g, 40, 0.3, 0.1, s, "results/g"+str(g)+"40.112.A.txt"), shell=True)
    '''
    '''
    # population_size
    for p in range(10, 81, 10):
        for s in seeds:
            call("python3 MDMT.py -f mdmt/mdmt40.112.A.ins -ga -g {} -p {} -m {} -e {} -s {} -out {}".format(400, p, 0.3, 0.1, s, "results/p"+str(p)+"40.112.A.txt"), shell=True)
    '''
    '''
    # elitism_rate
    for e in range(0, 51, 10):
        e = e/100
        for s in seeds:
            call("python3 MDMT.py -f mdmt/mdmt40.112.A.ins -ga -g {} -p {} -m {} -e {} -s {} -out {}".format(400, 40, 0.3, e, s, "results/e"+str(e)+"40.112.A.txt"), shell=True)
    '''
    '''
    # tuned ga
    for ins in os.listdir('mdmt'):
        if ins.startswith('mdmt'):
            for s in seeds:
                call("python3 MDMT.py -f mdmt/{} -t {} -ga -g {} -p {} -m {} -e {} -s {} -out {}".format(ins, 1800, 400, 40, 0.3, 0.1, s, "results/"+ins), shell=True)
    '''
