import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit

#Dane z tabel do poszczegolnych zadan
data1 = np.array([[0, -1], [1, 2], [2, 5], [3, 8], [4, 11]])
data2 = np.array([[0.0, 0.0], [0.5, 0.84], [1.0, 0.91], [1.5, 0.14], [2.0, -0.76], [2.5, -0.96], [3.0, -0.28]])
data3 = np.array([[0, 1.55], [1, 4.71], [2, 5.99], [3, 9.47], [4, 13.18]])
data4 = np.array([[0.0, 1.0], [0.5, 0.92], [1.0, 0.63], [1.5, -0.41], [2.0, -0.94], [2.5, 0.27], [3.0, 0.89]])

#zadanie 1 - Interpolacja 1
print(f'Zadanie 1:')
x1, y1 = data1[:, 0], data1[:, 1]
x_new = np.linspace(min(x1), max(x1), 100)

methods = ['linear', 'nearest', 'cubic']
plt.figure(figsize=(8, 4))
plt.scatter(x1, y1, label='Dane oryginalne')

for method in methods:
    f = interp1d(x1, y1, kind=method)
    plt.plot(x_new, f(x_new), label=method)

plt.title('Interpolacja 1')
plt.legend()
plt.show()
print('Powyższy kod rysuje wykres przedstawiający dane oryginalne oraz wyniki trzech różnych interpolacji (linear,nearest,cubic). Na podstawie wykresu możemy zobaczyć, która interpolacja najlepiej pasuje do tych danych. Dla tych konkretnych danych interpolacja cubic wydaje się najlepiej pasować, ponieważ krzywa jest bardziej gładka i przechodzi przez większość punktów.')

#zadanie 2 - Interpolacja 2
print(f'Zadanie 2:')
x2, y2 = data2[:, 0], data2[:, 1]

methods = ['linear', 'nearest', 'cubic']
plt.figure(figsize=(8, 4))
plt.scatter(x2, y2, label='Dane oryginalne')
x_new2 = np.linspace(x2.min(), x2.max(), 100)

for method in methods:
    f = interp1d(x2, y2, kind=method)
    plt.plot(x_new2, f(x_new2), label=method)

plt.title('Interpolacja 2')
plt.legend()
plt.show()

#zadanie 3 - Aproksymacja 1
print(f'Zadanie 3:')
x3, y3 = data3[:,0], data3[:,1]
degrees = [1, 2, 3, 4]

# Funkcja do aproksymacji wielomianem N-tego stopnia
def polynomial_function_N(x, *wsp):
    return np.sum([wsp[i] * x**i for i in range(len(wsp))], axis=0)

#współczynniki wielomianów i wartości R^2
wsp_list = []
r2_list = []

in_guess = np.ones(len(degrees))

# Aproksymacja dla każdego stopnia wielomianu
for degree in degrees:
  popt, _ = curve_fit(polynomial_function_N, x3, y3, p0=in_guess[:degree])
  y_fit = polynomial_function_N(x3, *popt)
  r2 = 1 - np.sum((y3 - y_fit) ** 2) / np.sum((y3 - np.mean(y3)) ** 2)
  wsp_list.append(popt)
  r2_list.append(r2)

#Najlepszy wielomian na podstawie R**2
best_index = np.argmax(r2_list)
best_degree = degrees[best_index]
best_wsp = wsp_list[best_index]

x_new3 = np.linspace(x3.min(), x3.max(), 100)
y_new3 = polynomial_function_N(x_new3, *best_wsp)

#Wykres
plt.figure(figsize=(8, 4))
plt.plot(x3, y3, 'o', label='Dane oryginalne')
plt.plot(x_new3, y_new3, label=f'Aproksymacja wielomianem stopnia {best_degree}')
plt.title('Aproksymacja - 1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

print(f'Najlepszy stopień wielomianu: {best_degree}')
print(f'Współczynniki wielomianu: {best_wsp}')

#zadanie 4 - Aproksymacja 2
print(f'Zadanie 4:')
x4, y4 = data4[:,0], data4[:,1]
degrees = [1, 2, 3, 4, 5, 6]

wsp_list = []
r2_list = []
in_guess = np.ones(len(degrees))

for degree in degrees:
    popt, _ = curve_fit(polynomial_function_N, x4, y4, p0=in_guess[:degree])
    y_fit = polynomial_function_N(x4, *popt)
    r2 = 1 - np.sum((y4 - y_fit) ** 2) / np.sum((y4 - np.mean(y4)) ** 2)
    wsp_list.append(popt)
    r2_list.append(r2)

best_index = np.argmax(r2_list)
best_degree = degrees[best_index]
best_wsp = wsp_list[best_index]


x_new4 = np.linspace(x4.min(), x4.max(), 100)
y_new4 = polynomial_function_N(x_new4, *best_wsp)

plt.figure(figsize=(8, 4))
plt.plot(x4, y4, 'o', label='Dane oryginalne')
plt.plot(x_new4, y_new4, label=f'Aproksymacja wielomianem stopnia {best_degree}')
plt.title('Aproksymacja - 2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

print(f'Najlepszy stopień wielomianu: {best_degree}')
print(f'Współczynniki wielomianu: {best_wsp}')
