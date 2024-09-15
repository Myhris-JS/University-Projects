#Zadanie 1
#Złożoność obliczeniowa to O(N), ponieważ danymi jest lista o długości N, dla której
#pętla wykona się N razy.
def minmax (a):
    min=0
    max=0
    for i in range(len(a)):
        if min>=a[i]:
            min=a[i]
        elif max<=a[i]:
            max=a[i]
    return min, max
print(minmax([8,2,4,1,5,6,3,7,10]))

#Zadanie 2
#Złożoność obliczeniowa to O(n^2), ponieważ danymi jest lista o długości N, dla której
#wykonają się dwie pętle N razy.
def insertion_sort(a):
    for i in range (len(a)):
        temp=a[i]
        j=i-1
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j-=1
            a[j+1]=temp
    return a
print(insertion_sort([0,8,2,4,6,7,9,1,3,5]))

#zadanie 3
#Złożoność obliczeniowa to O(NM), ponieważ danymi wejściowymi są dwie listy
#o różnych długościach (N i M),
def check_how_many(s1,s2):
    wynik=0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                wynik+=1
    return wynik
print(check_how_many('ala ma kota','aoiuye'))

#zadanie 4
#Złożoność obliczeniowa to O(N), gdzie N to ilość znaków w ciągu.
def suma(a):
    liczba = str(a)
    suma = 0
    for i in liczba:
        suma = suma + int(i)
    return suma
cyfra = input("podaj cyfrę: ")
print(suma(cyfra))
