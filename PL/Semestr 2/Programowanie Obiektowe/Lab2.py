import matplotlib.pyplot as plt
import datetime as dt

#zadanie 3.1
class Punkt:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def nalezy_do(self,prosta):
    if self.y == (prosta.a * self.x) + prosta.b:
      return True
    else:
      return False

class Prosta:
  def __init__(self,a,b):
    self.a = a
    self.b = b
  def miejsce_zerowe(self):
    if self.a != 0:
      return -self.b / self.a
    else:
      return 'Taki punkt nie istnieje'
p = Punkt(3,6)
pr = Prosta(2,0)
print(p.nalezy_do(pr))
print('{:.0f}'.format(pr.miejsce_zerowe()))

#zadanie 3.2
class Punkt:
  def __init__(self,x,y):
    self.x = x
    self.y = y

class Prostokat:
  def __init__(self,punkt1,punkt2):
    self.punkt1 = punkt1
    self.punkt2 = punkt2

    self.punkt3 = Punkt(punkt1.x, punkt2.y)
    self.punkt4 = Punkt(punkt2.x, punkt1.y)

    self.bok1 = abs(self.punkt2.x - self.punkt1.x)
    self.bok2 = abs(self.punkt2.y - self.punkt1.y)
  def pole(self):
    return f'Pole = {self.bok1 * self.bok2}'
  def obwod(self):
    return f'Obwod = {2 * (self.bok1 + self.bok2)}'
  def rysuj(self):
    plt.plot([self.punkt1.x, self.punkt3.x], [self.punkt1.y, self.punkt3.y], color='blue')
    plt.plot([self.punkt3.x, self.punkt2.x], [self.punkt3.y, self.punkt2.y], color='blue')
    plt.plot([self.punkt2.x, self.punkt4.x], [self.punkt2.y, self.punkt4.y], color='blue')
    plt.plot([self.punkt4.x, self.punkt1.x], [self.punkt4.y, self.punkt1.y], color='blue')

    plt.scatter([self.punkt1.x, self.punkt2.x], [self.punkt1.y, self.punkt2.y], color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Prostokąt - rysuj()')
    plt.grid(True)
    plt.show()

punkt1 = Punkt(1, 1)
punkt2 = Punkt(5, 4)
prostokat = Prostokat(punkt1, punkt2)
print(prostokat.pole())
print(prostokat.obwod())
prostokat.rysuj()

#zadanie 3.3
class Note:
  def __init__(self,autor,tresc):
    self.autor = autor
    self.tresc = tresc
    self.czas = dt.datetime.now()
  def __str__(self):
    return f'{self.autor}: \"{self.tresc}\" o godzinie {self.czas.strftime("%H:%M")}'

class Notebook:
  def __init__(self):
    self.notatki = []
  def dodaj_nowa(self,autor,tresc):
    nowa_notatka = Note(autor,tresc)
    self.notatki.append(nowa_notatka)
  def dodaj(self,notatka):
    self.notatki.append(notatka)
  def wyswietl_wszystko(self):
    if not self.notatki:
      print("Notatnik jest pusty.")
    else:
      print("Masz takie notatki:")
      for i, notatka in enumerate(self.notatki, 1):
        print(f"{i}. {notatka}")

nb = Notebook()
nb.dodaj_nowa("Bartek", "Dokończyć instrukcje")
nb.wyswietl_wszystko()

n1 = Note("Andrii", "Sprawdzić instrukcje")
nb.dodaj(n1)
nb.wyswietl_wszystko()

#zadanie 3.4
class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self._id_pracownika = id(self)
        self.__pensja = 1000  # domyślnie pensja będzie wynosić 1000

    def przedstaw_sie(self):
        print(f'Cześć, nazywam się {self.imie} {self.nazwisko} i pracuję na stanowisku {self.stanowisko}.')

    def get_pensja(self):
        return self.__pensja

    def __zmien_pensje(self, pensja):
        self.__pensja = pensja

    def podwyzka(self, pensja):
        return self.__zmien_pensje(pensja)

pracownik1 = Pracownik("Jan", "Kowalski", "Inżynier")
pracownik1.przedstaw_sie()
pracownik2 = Pracownik("Anna", "Nowak", "Specjalista ds. Marketingu")
pracownik2.przedstaw_sie()
print(f"ID pracownika 1: {pracownik1._id_pracownika}")
print(f"ID pracownika 2: {pracownik2._id_pracownika}")
print(f"Wynagrodzenie pracownika 1: {pracownik1.get_pensja()}")
pracownik1.podwyzka(1500)
print(f"Wynagrodzenie pracownika 1: {pracownik1.get_pensja()}")

#zadanie 3.5
class Player:
  def __init__(self,nick):
    self.nick = nick
    self._health = 100 #base
    self._score = 0 #base

  def attack(self,enemy):
    if isinstance(enemy, Player):
      enemy.health -= 10
      self.score = 10
      print(f'{self.nick} attacked {enemy.nick}')

  def heal(self):
    self.health += 10
    print(f'{self.nick} healed themselves.')

  def _get_health(self):
    return self._health

  def _set_health(self,value):
    if value < 0:
      self._health = 0
    else:
      self._health = value
      print(f'{self.nick} health value changed to {self.health}')

  def _get_score(self):
    return self._score

  def _set_score(self,value):
    self._score = value

  @property
  def health(self):
    return self._get_health()

  @health.setter
  def health(self,value):
    self._set_health(value)

  @property
  def score(self):
    return self._get_score()

  @score.setter
  def score(self,value):
    self._set_score(value)

  @property
  def level(self):
    return self._score // 100 + 1

  def __str__(self):
    return f'{self.nick}: health={self.health} level={self.level} (EXP {self.score}/{self.level*100})'


player1 = Player("John")
player2 = Player("Mike")

print(player1)
print(player2)

player1.attack(player2)

print(player1)
print(player2)

player2.heal()

print(player1)
print(player2)

player1.health = 80
player2.score = 100

print(player1)
print(player2)
