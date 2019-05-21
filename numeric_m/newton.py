from numeric_m.polynom import Polynomial


def newton_method(f: Polynomial, x0: float, eps=0.00001):
    i = 0
    while True:
        x_next = x0 - f(x0) / f.df(x0)
        if abs(x0-x_next) < eps:
            break
        # органичение епсилон на значение функции
        # if abs(f(x_next)) < epsilon: return x_next
        print(f'Iteration #{i}: F({round(x0, 6)}) = {round(f(x0), 6)}')
        x0 = x_next
        i += 1