

import numpy as np
import matplotlib.pyplot as plt

class Hello:
    def __init__(self):
        print("Hello World!")

    def hello(self):
        print("Hello World!")

    def love(self):
        print("I love you!")
        t = np.linspace(0, 2*np.pi, 1000)
        x = 16*np.sin(t)**3
        y = 13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)
        plt.plot(x, y, color='red', linewidth=2)
        plt.show()

def main():
    # hello()
    # Hello().hello()
    Hello().love()

if __name__ == '__main__':
    main()
