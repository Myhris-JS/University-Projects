from abc import ABC, abstractmethod
import random
import math

#zadanie 3.1
class Transport(ABC):
  def __init__(self,start,koniec,ladunek):
    self.start = start
    self.koniec = koniec
    self.ladunek = ladunek

  @abstractmethod
  def transportuj(start, nowy_koniec):
    pass

  def get_start(self):
    return self.start

  def get_koniec(self):
    return self.koniec

  def get_ladunke(self):
    return self.ladunek

  def __str__(self):
    return f"{self.__class__.__name__}(start={self.start}, koniec={self.koniec}, ladunek={self.ladunek})"

  def __repr__(self):
    return self.__str__()

class Samolot(Transport):
  def __init__(self,start,koniec,ladunek,ilosc_pasazerow,ilosc_bagazy):
    super().__init__(start,koniec,ladunek)
    self.ilosc_pasazerow = ilosc_pasazerow
    self.ilosc_bagazy = ilosc_bagazy

  def transportuj(self, nowy_koniec):
    print(f'Samolot startuje z {self.get_start()} do {self.get_koniec()}')
    print(f'Ilość pasażerów={self.ilosc_pasazerow}, Ilość bagaży={self.ilosc_bagazy}')
    self.start = self.koniec
    self.koniec = nowy_koniec
    print(f'Samolot dotarł do {self.get_koniec()}')

  def __str__(self):
     return (f"Samolot(start={self.start}, koniec={self.koniec}, ladunek={self.ladunek}, "
            f"ilosc_pasazerow={self.ilosc_pasazerow}, ilosc_bagazy={self.ilosc_bagazy})")
    
class Statek(Transport):
  def __init__(self,start,koniec,ladunek,rodzaj_ladunku,ilosc_kontenerow):
    super().__init__(start,koniec,ladunek)
    self.rodzaj_ladunku = rodzaj_ladunku
    self.ilosc_kontenerow = ilosc_kontenerow

  def transportuj(self,nowy_koniec):
     print(f"Statek wypływa z portu {self.get_start()} do portu {self.get_koniec()}.")
     print(f"Rodzaj ładunku: {self.rodzaj_ladunku}, ilość kontenerów: {self.ilosc_kontenerow}.")
     self.start = self.koniec
     self.koniec = nowy_koniec
     print(f"Statek dotarł do {self.get_koniec()}")

  def __str__(self):
    return (f"Statek(start={self.start}, koniec={self.koniec}, ladunek={self.ladunek}, "
            f"Rodzaj ladunku={self.rodzaj_ladunku}, Ilosc kontenerow={self.ilosc_kontenerow})")

class Ciezarowka(Transport):
  def __init__(self,start,koniec,ladunek,typ_ladunku,ilosc_palet):
    super().__init__(start,koniec,ladunek)
    self.typ_ladunku = typ_ladunku
    self.ilosc_palet = ilosc_palet

  def transportuj(self,nowy_koniec):
     print(f"Ciężarówka rusza z {self.get_start()} do {self.get_koniec()}.")
     print(f"Ilość palet: {self.ilosc_palet}, typ ładunku: {self.typ_ladunku}.")
     self.start = self.koniec
     self.koniec = nowy_koniec
     print(f"Ciężarówka dotarła do {self.get_koniec()}")

  def __str__(self):
    return (f"Ciezarowka(start={self.start}, koniec={self.koniec}, ladunek={self.ladunek}, "
            f"Typ ladunek={self.typ_ladunku}, Ilosc palet={self.ilosc_palet})")

samolot = Samolot("Gdańsk", "Warszawa", "Ludzie",100, 120)
samolot.transportuj("Berlin")
print(samolot)

statek = Statek("Gdańsk", "Oslo", "kontener","metale", 120)
statek.transportuj("Rotterdam")
print(statek)

ciezarowka = Ciezarowka("Szczecin","Berlin","palety","metale",63)
ciezarowka.transportuj("Hamburg")
print(ciezarowka)

#zadanie 3.2
class GameObject(ABC):
  def __init__(self,health):
    self.health = health

  def is_alive(self):
    return self.health > 0

  @abstractmethod
  def interact(self, other):
    pass

class Player(GameObject):
    def interact(self, other):
        pass

class Monster(GameObject):
    def interact(self, other):
      if isinstance(other, Player):
        other.health -= 10
        self.health = 0
        print("Gracz zabił potwora.")

class Door(GameObject):
  def interact(self,other):
    if isinstance(other,Player):
      print("Gracz przeszedł przez drzwi.")

def game():
  player = Player(50)

  objects = []
  for _ in range(10):
    if random.random() < 0.7:
      objects.append(Monster(30))
    else:
      objects.append(Door(1))

  for _,obj in enumerate(objects):
    obj.interact(player)
    if not player.is_alive():
      print("Gracz został zabity.")
      break

game()

#zadanie 3.3
from abc import ABC, abstractmethod
import math

class Equation(ABC):
  def __init__(self,wspolczynniki):
    self.wspolczynniki = wspolczynniki

  @abstractmethod
  def solve(self):
    pass

class LinearEquation(Equation):
  def __init__(self,wspolczynniki):
    if len(wspolczynniki) != 2:
      raise ValueError("Funkcja liniowa wymaga 2 wspolczynniki.")
    super().__init__(wspolczynniki)

  def solve(self):
    a,b = self.wspolczynniki
    if a == 0 and b != 0:
      print('Brak rozwiązań.')
    elif a == 0 and b == 0:
      print("Nieskończenie wiele rozwiązań.")
    else:
      x = -b / a
      print(f"x = {x}")

class QuadraticEquation(Equation):
  def __init__(self,wspolczynniki):
    if len(wspolczynniki) != 3:
      raise ValueError("Funkcja kwadratowa wymaga 3 wspolczynnikow.")
    super().__init__(wspolczynniki)

  def solve(self):
    a,b,c = self.wspolczynniki
    if a == 0:
      if b == 0:
        if c == 0:
          print("Nieskończenie wiele rozwiązań.")
        else:
         print("Brak rozwiązania.")
      else:
       x = -c/b
       print(f'x = {x}')
    else:
      delta = b**2 - 4*a*c
      if delta < 0:
        print("Brak rozwiazań")
      elif delta == 0:
        x = -b / (2*a)
        print(f"x = {x}")
      else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"x1 = {x1}, x2 = {x2}")

eq = LinearEquation([2, 0])
eq.solve()

eq1 = LinearEquation([0, 2])
eq1.solve()

eq2 = QuadraticEquation([1, -5, 6])
eq2.solve()

eq3 = QuadraticEquation([3, -4, 1])
eq3.solve()

