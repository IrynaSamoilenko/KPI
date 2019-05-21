"""
Full formula: 0*(1-0)*x^5 + (-1)*x^4 + 3*x^3 + 0*x^2 + (-2)*x + 2*1 = 0
Formula: -x^4 + 3*x^3 - 2x + 2 = 0
Eps = 0.00001
"""
from numeric_m.polynom import Polynomial


def secant_method(f: Polynomial, a: float, b: float, eps: float = 0.00001):
    if f(a)*f(b) > 0:
        print("No roots (both f(a) and f(b) are the same sign)")
    else:
        i = 0
        while True:
            c = b - (f(b) * (b - a)) / (f(b) - f(a))
            a, b = b, c
            print(f'Iteration #{i}: '
                  f'c = {round(c, 6)}; F(c) = {round(f(c), 6)}; ')

            if abs(b - a) < eps: break

            i+= 1

