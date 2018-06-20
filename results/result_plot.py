import matplotlib.pyplot as plt
import sys
import re
import numpy as np
import os


if __name__ == '__main__':
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
    plt.plot(x, [(6271-y)/6271 for y in y_value])
    plt.grid()
    plt.figure(2)
    plt.plot(x, y_time)           
    plt.grid()
    plt.show()     

