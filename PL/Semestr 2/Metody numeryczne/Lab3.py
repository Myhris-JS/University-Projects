import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3

#zadanie 1
print(f'Zadanie 1:')
def rectangle_method(f,a,b,rect):
  step = (b - a) / rect
  sum = 0
  for i in range(rect):
    x = a + i * step
    sum += f(x + step/2)
  return sum*step

rectangle_method(f, 0, 2, 20)

#zadanie 2
print(f'Zadanie 2:')
def plot_rectangle_method(f,a,b,rect):
  x = np.linspace(a-0.3,b+0.2,100)
  y = f(x)
  plt.plot(x, y, 'b', linewidth=1.5)
  plt.grid(linestyle='--', alpha=0.6)

  step = (b - a) / rect
  for i in range(rect):
    x = a + i * step
    y = f(x + step/2)
    plt.plot([x, x, x+step, x+step, x],[0, y, y, 0, 0], color='red')

  plt.title('Rectangle method - visualization')
  plt.axvline(x=0, color='red', linestyle='--')
  plt.axvline(x=2, color='red', linestyle='--')
  plt.xlim(-0.5, 2.5)
  plt.ylim(-0.5,10)
  plt.show()

plot_rectangle_method(f,0,2,4)

#zadanie 3
print(f'Zadanie 3:')
def trapezoidal_method(f,a,b,trap):
  step = (b - a) / trap
  x = (f(a) + f(b)) / 2
  for i in range(1, trap):
      x += f(a * i * step)
  return x

trapezoidal_method(f, 0, 2, 20)


#zadanie 4
print(f'Zadanie 4:')
def plot_trapezoidal_method(f, a, b, trap):
    x = np.linspace(a - 0.3, b + 0.2, 100)
    y = f(x)
    plt.plot(x, y, 'b', linewidth=1.5)
    plt.grid(linestyle='--', alpha=0.6)

    step = (b - a) / trap
    for i in range(trap):
        x1 = a + i * step
        y1 = f(x1)
        x2 = a + (i + 1) * step
        y2 = f(x2)
        plt.plot([x1, x2], [y1, y1], color='red')
        plt.plot([x2, x2], [y1, y2], color='red')
        plt.plot([x1, x1], [y1, 0], color='red')

    plt.title('Trapezoidal method - visualization')
    plt.axvline(x=0, color='red', linestyle='-')
    plt.axvline(x=2, color='red', linestyle='-')
    plt.axhline(y=0, color='red', linestyle='-')
    plt.xlim(-0.5, 2.5)
    plt.ylim(-1, 10)
    plt.show()

plot_trapezoidal_method(f, 0, 2, 4)

#zadanie 5
print(f'Zadanie 5:')
def monte_carlo(f, a, b, monte):
  x = np.random.uniform(a, b, monte)
  y = f(x)
  i = ((b - a) / monte) * np.sum(y)
  return i

monte_carlo(f, 0, 2, 10000)

#zadanie 6
print(f'Zadanie 6:')
def monte_carlo(f, a, b, monte):
    x = np.random.uniform(a, b, monte)
    y = f(x)
    i = ((b - a) / monte) * np.sum(y)
    return i, x, y

def plot_monte_carlo_method(f,a,b,monte):
  i, x, fx = monte_carlo(f, a, b, monte)
  y = np.random.uniform(0, f(b), monte)

  plt.figure(figsize=(6, 4))
  plt.plot(np.linspace(a-0.2, b+0.2, 100), f(np.linspace(a-0.2, b+0.2, 100)), 'b', linewidth=2)
  plt.scatter(x[y <= fx], y[y <= fx], color='green', s=25)
  plt.scatter(x[y > fx], y[y > fx], color='red', s=25)
  rectangle = plt.Rectangle((0,0), 2, 8, fill=None,
                              edgecolor='k', linestyle='--')
  plt.gca().add_patch(rectangle)
  plt.grid(linestyle='--', alpha=0.5)
  plt.title('Monte Carlo method - visualization')
  plt.xlim(-0.4, 2.4)
  plt.ylim(-0.4, 11)
  plt.show()

plot_monte_carlo_method(f, 0, 2, 100)
