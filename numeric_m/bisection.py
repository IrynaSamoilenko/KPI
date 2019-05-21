"""
Full formula: 0*(1-0)*x^5 + (-1)*x^4 + 3*x^3 + 0*x^2 + (-2)*x + 2*1 = 0
Formula: -x^4 + 3*x^3 - 2x + 2 = 0
Eps = 0.00001
"""
from numeric_m.polynom import Polynomial


def bisection_method (f: Polynomial, a: float, b: float, eps: float = 0.0001):
    if f(a)*f(b) > 0:
        print("No roots (both f(a) and f(b) are the same sign)")
    else:
        i = 0
        while True:
            mid = (a + b) / 2.0
            # органичение епсилон на значение функции
            # if abs(f(mid)) < eps: break

            if (b-a)/2.0 < eps: break

            print(f'Iteration #{i}:\n '
                  f'x = {round(mid, 5)}\n F(x) = {round(f(mid), 6)}\n')

            dif = (b - a) / 2.0

            # органичение епсилон на промежуток
            if abs(dif) < eps: break

            if f(mid) == 0:
                return mid
            elif f(a)*f(mid) < 0:
                b = mid
            else:
                a = mid
            i += 1
        return mid

