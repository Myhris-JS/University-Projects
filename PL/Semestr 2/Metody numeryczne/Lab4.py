import numpy as np
from scipy.optimize import fsolve
from scipy.integrate import quad

#zadanie 1
print(f'Zadanie 1:')
def func1(x):
    return (x - 2)**3 - x**2 + 2*x
def func2(x):
    return x**2 - 2
def func3(x):
    return np.sin(x)
def func4(x):
    return x**3 - 2*x + 2
root1 = fsolve(func1, 1.5)[0]
root2 = fsolve(func2, 2)[0]
root3 = fsolve(func3, 3)[0]
root4 = fsolve(func4, -4)[0]

print(f"f(x) = (x−2)^3 − x^2 + 2x: x ≈ {root1:.2f}")
print(f"f(x) = x^2 − 2: x ≈ {root2:.2f}")
print(f"f(x) = sin(x): x ≈ {root3:.2f}")
print(f"f(x) = x^3 − 2x + 2: x ≈ {root4:.2f}")

#zadanie 2
print(f'Zadanie 2:')
def func1(x):
    return x**3
def func2(x):
    return x**3 - 6*x**2 + 9*x + 2
def func3(x):
    return np.sin(2*x) + 1
def func4(x):
    return np.sin(8*x) / x + 1

result1, _ = quad(func1, 0, 2)
result2, _ = quad(func2, 0, 4)
result3, _ = quad(func3, 0, np.pi)
result4, _ = quad(func4, 1, 4)

print(f"∫(0 to 2) x^3 dx = {result1:.0f}")
print(f"∫(0 to 4) (x^3 - 6x^2 + 9x + 2) dx = {result2:.0f}")
print(f"∫(0 to π) (sin(2x) + 1) dx = {result3:.2f}")
print(f"∫(1 to 4) (sin(8x)/x + 1) dx ≈ {result4:.6f}")
