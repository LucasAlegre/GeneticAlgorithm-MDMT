from subprocess import call

if __name__ == '__main__':

    for i in range(1, 6):
        call("python3 MDMT.py -f mdmt/mdmt39.112.A.ins -ga -g 1000000 -p " + str(i*10) + " -o " + "tk" + str(i), shell=True)

