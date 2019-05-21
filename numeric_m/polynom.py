"""
Full formula: 0*(1-0)*x^5 + (-1)*x^4 + 3*x^3 + 0*x^2 + (-2)*x + 2*1 = 0
Formula: -x^4 + 3*x^3 - 2x + 2 = 0
Eps = 0.00001
"""

import matplotlib.pyplot as plt
import numpy as np


class Polynomial:

    def __init__(self, *coef):
        self.coef = coef[::-1]

    def __repr__(self):
        return f"Polynomial formula is " \
               + str(self.coef[::-1])

    def __call__(self, x):
        fx = 0
        for index, c in enumerate(self.coef):
            fx += c * x ** index
        return fx

    def df(self, x):
        df = 0
        for index, c in enumerate(self.coef):
            df += index * c * x ** (index - 1)
        return df


if __name__ == '__main__':
    p = Polynomial(0, -1, 3, 0, -2, 2)
    X = np.linspace(-1.1, 2.9, endpoint=True)
    F = p(X)
    plt.plot(X, F)
    plt.show()

