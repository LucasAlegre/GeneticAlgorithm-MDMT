from subprocess import call

if __name__ == '__main__':
	
    seeds = [7, 42, 100101, 9999, 381]
    
    # max_non_improving_generations
    for g in range(100, 501, 100):
        for s in seeds:
            call("python3 MDMT.py -f mdmt/mdmt40.112.A.ins -ga -g {} -p {} -m {} -e {} -s {} -out {}".format(g, 40, 0.3, 0.1, s, "results/g"+str(g)+"40.112.A.txt"), shell=True)

