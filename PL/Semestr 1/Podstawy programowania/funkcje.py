import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify

def function_input(prompt):
    func_str = input(prompt)
    x = symbols('x')
    return lambdify(x, func_str, 'numpy')

def bisection_method(func, a, b, tol=1e-6, max_iter=1000):
    if func(a) * func(b) > 0:
        print("Błąd: Funkcje nie mają różnych znaków na krańcach przedziału.")
        return None

    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return round((a + b) / 2, 2)

def plot_functions_and_intersection(f, g, result):
    x_values = np.linspace(result - 2, result + 2, 100)
    plt.plot(x_values, f(x_values), label='f(x)')
    plt.plot(x_values, g(x_values), label='g(x)')
    plt.scatter(result, f(result), color='red', label=f'Punkt wspólny ({result}, {f(result)})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    f = function_input("Podaj wzór funkcji f(x): ")
    g = function_input("Podaj wzór funkcji g(x): ")
    x_start = float(input("Podaj punkt startowy x: "))

    result = bisection_method(lambda x: f(x) - g(x), x_start - 2, x_start + 2)

    if result is not None:
        print(f"Znaleziony punkt wspólny: ({result}, {f(result)})")
        plot_functions_and_intersection(f, g, result)
    else:
        print("Brak punktu wspólnego dla podanych funkcji.")

if __name__ == "__main__":
    main()
