from numeric_m.polynom import Polynomial
from numeric_m.bisection import bisection_method
from numeric_m.newton import newton_method
from numeric_m.secant import secant_method

p = Polynomial(0, -1, 3, 0, -2, 2)
a = 2
b = 5
x0 = 2.26

def start_bisection_method():
    print("--------------------- BISECTION METHOD ------------------------")
    bisection_method(p, a, b)
    print("\n")


def start_newton_method():
    print("---------------------- NEWTON METHOD --------------------------")
    newton_method(p, x0)
    print("\n")

def start_secant_method():
    print("---------------------- SECANT METHOD --------------------------")
    secant_method(p, a, b)
    print("\n")

if __name__ == '__main__':
    start_bisection_method()
    start_newton_method()
    start_secant_method()
