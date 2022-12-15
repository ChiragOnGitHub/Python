import math
import matplotlib.pyplot as plt
import numpy as np

def curve():
    l1=[i for i in range(361)]
    listCos=[math.cos(math.radians(i)) for i in l1]
    listSin=[math.sin(math.radians(i)) for i in l1]

    l2=[i for i in range(200)]
    listPol=[i*i*i for i in l2]

    l3=[i for i in np.linspace(1,40,100)]
    listExp=[math.exp(i) for i in l3]

    plt.subplot(2,2,1)
    plt.plot(l1,listCos)
    plt.title("Cos x")
    
    plt.subplot(2,2,2)
    plt.plot(l1,listSin)
    plt.title("Sin x")

    plt.subplot(2,2,3)
    plt.plot(l2,listPol)
    plt.title("Polynomial Function")

    plt.subplot(2,2,4)
    plt.plot(l3,listExp)
    plt.axis([1,4,1,40])
    plt.title("Exponential Function")

    plt.tight_layout()
    plt.show()

curve()
