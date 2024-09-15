import random

#Trzy scenariusze, które zostały podane w instrukcji projektu
def script1():
    start=random.randint(0, 10)
    finish=random.randint(0, 10)
    while start==finish:
        finish=random.randint(0, 10)
    return start, finish

def script2():
    if random.random() < 0.7:
        start=random.randint(4,10)
        finish=0

        return start, finish
    return script1()

def script3():
    if random.random() < 0.7:
        start = 0
        finish = random.randint(1,10)

        return start, finish
    return script1()

#Algorytm I. Winda zostaje na tym piętrze na którym skończyła swój ruch.
def scriptI(data):
    stops=0
    previous=data[0][0]
    for start, finish in data:
        prev=abs(start-previous)
        stops+=abs(start-finish)+prev
        previous=finish
    return stops
#Algorytm II. Winda po przejeździe zawsze wraca na parter (piętro 0), a dopiero potem jedzie na kolejne piętro.
def scriptII(data):
    stops=0
    for start,finish in data:
        stops+=start+abs(start-finish)+finish
    return stops
#Algorytm III. Winda po przejeździe wraca na piętro 0 jeśli zatrzymała się na 4 piętrze, inaczej cofa się do piętra 5.
def scriptIII(data):
    stops=0
    previous=data[0][0]
    default=lambda f: 0 if f<=4 else 5
    for start,finish in data:
        start_off=abs(start-previous)
        finish_off=abs(finish-default(finish))
        stops+=start_off+abs(start-finish)+finish_off

        previous=default(finish)
    return stops

rep=1000          #powtorzenie symulacji X razy
dis=2.8/1000      #dystans (2.8m), ktory pokona winda w km
d1=[script1() for i in range(rep)]
d2=[script2() for i in range(rep)]
d3=[script3() for i in range(rep)]
data=[d1,d2,d3]

#wynik przedstawiony w formie:
#Algorytm X
#1. X.XX km
#2. X.XX km
#3. X.XX km
#Srednia: X.XX km
print('Algorytm I')
sc1=[scriptI(line)*dis for line in data]
print(f'1. {"{:.2f}".format(sc1[0])} km') 
print(f'2. {"{:.2f}".format(sc1[1])} km')
print(f'3. {"{:.2f}".format(sc1[2])} km')
print(f'Srednia: {"{:.2f}".format( sum(sc1)/3)} km')

print('Algorytm II')
sc2=[scriptII(line)*dis for line in data]
print(f'1. {"{:.2f}".format(sc2[0])} km') 
print(f'2. {"{:.2f}".format(sc2[1])} km')
print(f'3. {"{:.2f}".format(sc2[2])} km')
print(f'Srednia: {"{:.2f}".format( sum(sc2)/3)} km')

print('Algorytm III')
sc3=[scriptIII(line)*dis for line in data]
print(f'1. {"{:.2f}".format(sc3[0])} km') 
print(f'2. {"{:.2f}".format(sc3[1])} km')
print(f'3. {"{:.2f}".format(sc3[2])} km')
print(f'Srednia: {"{:.2f}".format( sum(sc3)/3)} km')

