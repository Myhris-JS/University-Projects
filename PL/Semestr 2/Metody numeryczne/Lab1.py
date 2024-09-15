import numpy as np
import matplotlib.pyplot as plt

#Zadanie 1
print(f'Zadanie 1:')
a = np.array([1, 2, 3, 4, 5])
print(a)
a[1] = -1
a[3] *= 2
print(f'{a}\n')

#Zadanie 3
print(f'Zadanie 2:')
r = np.array(np.random.randint(5, size=(3,4)))
print(r)
print(f'Drugi wiersz: \n {r[1]}')
print(f'Druga kolumna: \n {r[:,1]}')
print(f'Pierwszy wiersz *2: \n {r[0]*2}')
print(f'Kwadratowa macierz...: \n {r[[0,1],:2]}\n')

#Zadanie 4
print(f'Zadanie 3:')
def simple_plot(a,b):
    plt.plot(a, color='red', linestyle='--', label='a')
    plt.plot(b, 'b-', label='b')
    plt.legend(loc="upper right")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Zadanie 3')
    plt.grid(color='green', linestyle='--', alpha=0.5, linewidth=1.15)
    plt.show()
x = np.array(np.random.randn(4))
y = np.array(np.random.randn(4))
print(f'x:{x}, y:{y}')
simple_plot(x,y)

#Zadanie 4
print(f'Zadanie 4:')
def f(x):
  return x**2 - 4*x +8

def func_plot(vmin,vmax,step):
  x = np.arange(vmin,vmax+step,step) #vmax+step -> dodane, aby vmax był pokazany na wykresie
  y = f(x)
  plt.plot(x,y)
  plt.xlabel('x')
  plt.ylabel('y')
  plt.title('f(x) = x^2 - 4x + 8')
  plt.grid(True, color='gray', linestyle='--', linewidth=1)
  plt.show()

func_plot(-1,1,0.2)

#Zadanie 5
print(f'Zadanie 5:')
def multi_plot(sizes, labels):
  plt.subplot(1,2,1)
  plt.pie(sizes,labels=labels)
  plt.title('Wykres kołowy')

  plt.subplot(1,2,2)
  plt.bar(labels, sizes, color="red")
  plt.title('Wykres słupkowy')

  plt.tight_layout()
  plt.show()

sizes = [1000000, 2000000, 1500000, 1200000]
labels = ['Warszawa', 'Kraków', 'Łódź', 'Wrocław']

multi_plot(sizes, labels)

#Zadanie 6
print(f'Zadanie 6:')
def scatter_plot():
  x1 = np.random.rand(100)
  y1 = np.random.rand(100)

  x2 = np.random.randn(100)
  y2 = np.random.randn(100)

  plt.scatter(x1, y1, color='blue', label='Zestaw 1')
  plt.scatter(x2, y2, color='green', marker='*', label='Zestaw 2')

  plt.xlabel('x')
  plt.ylabel('y')
  plt.grid(True, color='red', linestyle=':', linewidth=0.5)
  plt.legend(loc='upper right')
  plt.show()

scatter_plot()

#Zadanie 7
print(f'Zadanie 7:')
def make_3D(x,y):
  X,Y = np.meshgrid(x,y)
  Z = np.sqrt(X**2 + Y**2)

  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.plot_surface(X, Y, Z, cmap='viridis')

  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('z')

  plt.show()

a = np.random.randn(100)
b = np.random.randn(100)
make_3D(a,b)
