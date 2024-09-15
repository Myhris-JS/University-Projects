import numpy as np
import matplotlib.pyplot as plt

#funkcje testowe dla zadań i zmienne pomocnicze
def test1(x):
    return x**2-2
def test2(x):
    return np.sin(x)
def test3(x):
    return x**3-2*x+2
eps = 10**-6
max_iter = 100

#zadanie 1
def f(x):
    return (x-2)**3-x**2+2*x
def bisection_method(f,a,b,eps,max_iter):
    if f(a)*f(b)>=0:
        return 'Warunek f(a)f(b)<0 nie został zachowany.'
    else:
        i=0
        while abs(a-b)>eps and i<max_iter:
            c = (a+b)/2
            if abs(f(c))<eps:
                return '{:.2f}'.format(c)
            elif f(a)*f(c)<0:
                b=c
            else:
                a=c
            i+=1
        return '{:.2f}'.format((a+b)/2)
print(bisection_method(f,1.5,3,eps,max_iter))
print(bisection_method(test1,1,2,eps,max_iter))
print(bisection_method(test2,1,2,eps,max_iter))
print(bisection_method(test2,3,5,eps,max_iter))

#zadanie 2 
#Zmodyfikowane zadanie 1:
def f(x):
    return (x-2)**3-x**2+2*x
def bisection_method(f,a,b,eps,max_iter):
    if f(a)*f(b)>=0:
        return 'Warunek f(a)f(b)<0 nie został zachowany.'
    else:
        i=0
        points = []
        while abs(a-b)>eps and i<max_iter:
            c = (a+b)/2
            points.append(c)
            if abs(f(c))<eps:
                return points
            elif f(a)*f(c)<0:
                b=c
            else:
                a=c
            i+=1
        return points

def bisection_plot(f, a, b, eps, max_iter):
    points = bisection_method(f, a, b, eps, max_iter)
    result = points[-1]
    x_val = [a + i * (b - a) / 1000 for i in range(1000)]
    y_val = [f(x) for x in x_val]

    plt.plot(x_val, y_val, label="f(x)")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(a, color='red', linestyle='--', linewidth=0.5)
    plt.axvline(b, color='red', linestyle='--', linewidth=0.5)

    for point in points:
        plt.axvline(point, color='red', linestyle='--', linewidth=0.5)

    plt.ylabel('y')
    plt.xlabel('x')
    plt.title('x = {:.2f}'.format(result))
    plt.grid(True)
    plt.xlim(min(a, b) - 0.1, max(a, b) + 0.1)  # Ograniczenie zakresu osi x
    plt.legend()
    plt.show()


bisection_plot(f, 1.5, 3, eps, max_iter)

#zadanie 3
def newton(f, x0, eps=1e-7, max_iter=1000):
    h = 1e-7  # Mała wartość h dla obliczenia pochodnej
    for _ in range(max_iter):
        fx0 = f(x0)
        if abs(fx0) < eps:
            return x0
        fx0_derivative = (f(x0 + h) - fx0) / h
        x0 = x0 - fx0 / fx0_derivative
    print("Nie osiągnięto wymaganej dokładności w zadanej liczbie iteracji.")
    return x0

# Przykładowe wywołanie funkcji f2 z punktem początkowym x0=4
def f2(x):
    return (x - 2)**2 - 1

result = newton(f2, 4)
print(result)

#zadanie 4
def newton(f, f_prime, x0, eps=1e-7, max_iter=1000):
    h = 1e-7  # Mała wartość h dla obliczenia pochodnej
    x_values = [x0]  # Lista przechowująca wartości x w trakcie iteracji
    y_values = [f(x0)]  # Lista przechowująca wartości f(x) w trakcie iteracji
    for _ in range(max_iter):
        fx0 = f(x0)
        if abs(fx0) < eps:
            return x0, x_values, y_values
        fx0_derivative = f_prime(x0)
        x_new = x0 - fx0 / fx0_derivative
        x_values.append(x_new)
        y_values.append(f(x_new))
        x0 = x_new
    print("Nie osiągnięto wymaganej dokładności w zadanej liczbie iteracji.")
    return x0, x_values, y_values

def f1(x):
    return (x - 2)**3 - x**2 + 2*x

def f1_prime(x):
    h = 1e-7
    return (f1(x + h) - f1(x)) / h

def f2(x):
    return x**2 - 2

def f2_prime(x):
    return 2*x

def f3(x):
    return np.sin(x)

def f3_prime(x):
    return np.cos(x)

def f4(x):
    return x**3 - 2*x + 2

def f4_prime(x):
    return 3*x**2 - 2

def plot_newton_iterations(f, f_prime, x0, eps=1e-7, max_iter=1000):
    x_values = np.linspace(x0 - 2, x0 + 2, 1000)
    y_values = f(x_values)

    root, iterations_x, iterations_y = newton(f, f_prime, x0, eps, max_iter)

    plt.figure(figsize=(6, 4))
    plt.plot(x_values, y_values)
    plt.scatter(iterations_x, iterations_y, color='red')
    for i in range(len(iterations_x)):
        plt.plot([iterations_x[i], iterations_x[i]+0.5], [iterations_y[i], iterations_y[i] + 0.5 * f_prime(iterations_x[i])], color='red', linestyle='--', linewidth=0.8)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"x = {root}")
    plt.grid(True)
    plt.show()

# Wizualizacje
plot_newton_iterations(f1, f1_prime, 1.5)
plot_newton_iterations(f2, f2_prime, 2)
plot_newton_iterations(f3, f3_prime, 3)
plot_newton_iterations(f4, f4_prime, 0)
