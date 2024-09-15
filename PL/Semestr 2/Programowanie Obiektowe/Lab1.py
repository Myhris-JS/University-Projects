#zadanie 1
class Samochod:
  def __init__(self,marka,model,rok,predkosc):
    self.marka = marka
    self.model = model
    self.rok = rok
    self.predkosc = predkosc

  def jedz(self,droga):
    self.droga = droga
    print(f'Samochód marki {self.marka}, model {self.model} z {self.rok} roku jedzie z prędkością {self.predkosc} km/h.')
    if droga.maks<self.predkosc:
      print(f'Przekraczasz maksymalną prędkość o {self.predkosc - droga.maks} km/h na drodze typu {droga.typ}.')
    else:
      print(f'Nie przekraczasz maksymalnej prędkość {droga.maks} km/h na drodze typu {droga.typ}.')

  def __del__(self): #pokaże się automatycznie w .py
    print(f'Samochod marki {self.marka} jest niszczony.')

class Droga:
  def __init__(self,typ,maks):
    self.typ = typ
    self.maks = maks

auto = Samochod('Ferrari','250 GTO',2019,200)
moja_droga = Droga('Autostrada',140)
auto.jedz(moja_droga)

#zadanie 2
class KontoBankowe:
  def __init__(self,numer_konta,imie,nazwisko,saldo):
    self.numer_konta = numer_konta
    self.imie = imie
    self.nazwisko = nazwisko
    self.saldo = saldo

  def __del__(self):
    print(f'Konto o numerze {self.numer_konta} należące do {self.imie} {self.nazwisko} zostało usunięte.')

  def wplata(self,wplata):
    self.wplata = wplata
    self.saldo += wplata
    print(f'Wpłata na konto o numerze {self.numer_konta} została wykonana. Aktualne saldo: {self.saldo}')

  def wyplata(self,wyplata):
    self.wyplata = wyplata
    self.saldo -= wyplata
    print(f'Wypłata z konta o numerze {self.numer_konta} została wykonana. Aktualne saldo: {self.saldo}')

moje_konto = KontoBankowe('123456','Jan','Kowalski',1000)
moje_konto.wplata(500)
moje_konto.wyplata(1500)
print(moje_konto.saldo)

#zadanie 3
class EnergiaOdnawialna:
  def __init__(self,nazwa,moc,lokacja):
    self.nazwa = nazwa
    self.moc = moc
    self.lokacja = lokacja

  def __str__(self):
    return f'źródło: {self.nazwa}, Moc: {self.moc} MW'

  def __add__(self, other):
    return EnergiaOdnawialna(f'{self.nazwa}, {other.nazwa}',self.moc + other.moc, f'{self.lokacja}, {other.lokacja}')

  def get_info(self):
    print(f'Źródło: {self.nazwa}, Moc: {self.moc} MW, Lokacja: {self.lokacja}')

wiatrowa = EnergiaOdnawialna('Wiatr', 50, 'Niemcy')
sloneczna = EnergiaOdnawialna('Słońce', 30, 'Polska')
wiatrowa.get_info()
sloneczna.get_info()
hybrydowa = wiatrowa + sloneczna
hybrydowa.get_info()
print(wiatrowa)
print(wiatrowa == sloneczna)

#zadanie 4
class Fraction:
  def __init__(self,a,b):
    self.a = a
    self.b = b

  def __repr__(self):
    return f'Fraction({self.a},{self.b})'

  def __str__(self):
    if self.b == 0:
      return f'Mianownik nie może być równy 0. (ZeroDivisionError)'
    elif self.a > self.b:
      if self.a % self.b != 0:
        return f'{int(self.a/self.b)} {self.a-self.b}/{self.b}'
      else:
        return f'{int(self.a/self.b)}'
    elif abs(self.a) == abs(self.b):
      return f'{self.a}'
    else:
      return f'{self.a}/{self.b}'

  def __add__(self,other):
    if self.b == other.b:
      return Fraction(self.a + other.a, self.b)
    else:
      a = self.a * other.b + other.a * self.b
      b = self.b * other.b
      return Fraction(a,b)

f = Fraction(3,4)
f2 = Fraction(3,4)
print(repr(f))
print(f)
print(f2)
print(Fraction(4,0))
f3 = f + f2
print(f3)
