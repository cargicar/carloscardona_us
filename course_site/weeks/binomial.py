import numpy as np
import matplotlib.pyplot as plt

class Binomial(object):

    def __init__(self, N, width, image_path):
        self.N=N
        self.image_path=image_path
        self.width=width
        self.data={}
    for nr in range(0,self.N+1):
        self.data[nr]=int(scipy.special.binom(self.N, nr))

    nr = list(self.data.keys())
    cases = list(self.data.values())

    fig = plt.figure(figsize = (5, 5))

    # creating the bar plot
    plt.bar(nr, cases, color ='blue',
        width = self.width)

    plt.xlabel("Number of ways")
    plt.ylabel("Particle in the left chamber ")
    plt.title("Binomial distribution")
    plt.savefig(image_path)
