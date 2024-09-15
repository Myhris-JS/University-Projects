# Laboratorium 2 (17.05.2024)
### Zadanie 1
Zaimplementować funkcję znajdującą pierwiastek podanej jako argument funkcji za pomocą metody połowienia.
Poniżej jest pokazane przykładowe wywołanie zaimplementowanej funkcji w celu znalezienia pierwiastka funkcji
*f(x) = (x − 2)3 − x
2 + 2x.*

<center>Listing 2: Przykładowe wywołanie funkcji.</center>

```
1 def f(x):
2 return (x - 2)**3 - x**2 + 2*x
3
4 print(bisection_method(f, 1.5, 3, eps=10**-6, max_iter=100))
5 # 2.000000238418579
```
Przykładowe argumenty: funkcja przyjmuje funkcje f której miejsce zerowe musi być znalezione, przedział [a, b]
w którym miejsce zerowe jest szukane, oraz dwa argumenty eps i max_iter, określające dokładność i maksymalną
liczbę iteracji (kroków) odpowiednio. Funkcja ma zwrócić odnalezione rozwiązanie (jedna wartość). W przypadku
gdy zostanie osiągnięta maksymalna liczba iteracji, a przedział poszukiwań nie zawęził się poniżej wskazanej dokładności należy wyświetlić stosowny komunikat.

<center>

*Proszę się upewnić, że zaimplementowana funkcja działa prawidłowo dla następujących nastawień:*

<table>
  <tr>
    <th>Funkcja</th>
    <th>a</th>
    <th>b</th>
    <th>Oczekiwany wynik</th>
  </tr>
  <tr>
    <td>\\[f(x)=(x-2)^3-x^2+2x\\]</td>
    <td>1.5</td>
    <td>3</td>
    <td>≈2</td>
  </tr>
  <tr>
    <td>\\[f(x)=x^2-2\\]</td>
    <td>1</td>
    <td>2</td>
    <td>≈1.41</td>
  </tr>
  <tr>
    <td>\\[f(x)=sin(x)\\]</td>
    <td>1</td>
    <td>2</td>
    <td>Warunek \\(f(a)f(b) < 0\\) nie jest zachowany, algorytm nie wystartuje i pokaże stosowny komunikat</td>
  </tr>
  <tr>
    <td>\\[f(x)=sin(x)\\]</td>
    <td>3</td>
    <td>5</td>
    <td>≈3.14</td>
  </tr>
</table>

**Uwaga:** proszę ustawić *eps* = 10−6 i *max_iter* = 100.
</center>








### Zadanie 2
Rozbudować funkcjonalność funkcji z ***Zadania 1*** tak żeby była pokazywana wizualizacja działania zaimplementowanej metody.

Przykład takiej wizualizacji jest pokazany na Rysunku poniżej.
<center>
  <img src="https://drive.google.com/uc?export=view&id=10_dmMA1UCBS3PvY4yGB7vGEDvRBvuY8l"><br>
  <b>Rysunek 1:</b> Przykładowa wizualizacja metody połowienia
</center>

### Zadanie 3
Zaimplementować funkcję znajdującą pierwiastek podanej jako argument funkcji za pomocą metody Newtona. Poniżej jest pokazane przykładowe wywołanie zaimplementowanej funkcji w celu znalezienia pierwiastka funkcji
*\\(f(x) = (x − 2)^2 − 1\\)*, z punktem początkowym *\\(x+0 = 4\\)*.

<center>Listing 3: Przykładowe wywołanie funkcji.</center>


```
1 def f2(x):
2 return (x - 2)**2 - 1
3
4 newton(f2, 4)
5 # 3.000000000000003
```

Przykładowe argumenty: funkcja przyjmuje funkcje f której miejsce zerowe musi być znalezione, punkt startu \\(x_0\\), w okolicach którego miejsce zerowe jest szukane, oraz dwa argumenty eps i max_iter, określające dokładność
i maksymalną liczbę iteracji (kroków) odpowiednio. Funkcja ma zwrócić odnalezione rozwiązanie (jedna wartość). W przypadku gdy zostanie osiągnięta maksymalna liczba iteracji, a przedział poszukiwań nie zawęził się poniżej
wskazanej dokładności należy wyświetlić stosowny komunikat.

**Podpowiedź:** Do obliczania wartości pochodnej funkcji w punkcie \\(x_0\\) należy użyć wzoru:

* \\(f'(x_0) =\\) $\frac{f(x_0 + h) - f(x_0)}{h}$,
  * gdzie h jest bardzo małą wartością (np. \\(h = 10^{-7}\\).

**Podpowiedź 2:** Styczną do funkcji w punkcie \\((x_0, f(x_0))\\) możemy wyrazić jako:
* \\(y = f′(x_0) * (x − x_0) + f(x_0)\\)


### Zadanie 4
Rozbudować funkcjonalność funkcji z Zadania 3 tak żeby była pokazywana wizualizacja działania zaimplementowanej metody.

Przykład takiej wizualizacji jest pokazany na Rysunku poniżej.

<center><img src="https://raw.githubusercontent.com/JordieMyhris/University-Projects/main/PL/Semestr%202/Metody%20numeryczne/Zadania/Obrazki/lab2-4.jpg"><br>
<b>Rysunek 2: Przykładowa wizualizacja metody Newtona</center>


<center><i>Proszę się upewnić, że zaimplementowana funkcja działa prawidłowo dla wszystkich przykładów z Tabeli.</i>
<table>
  <tr>
    <th>Funkcja</th>
    <th>\\(x_0\\)</th>
    <th>Oczekiwany wynik</th>
  </tr>
  <tr>
    <td>\\[f(x) = (x − 2)^3 − x^2 + 2x\\]</td>
    <td>1.5</td>
    <td>≈ 2</td>
  </tr>
  <tr>
    <td>\\[f(x) = x^2 − 2\\]</td>
    <td>2</td>
    <td>≈ 1.41</td>
  </tr>
  <tr>
    <td>\\[f(x) = sin(x)\\]</td>
    <td>3</td>
    <td>≈ 3.14</td>
  </tr>
  <tr>
    <td>\\[f(x) = x^3 − 2x + 2\\]</td>
    <td>0</td>
    <td>Wypisze się komunikat o osiągnięciu maksymalnej liczby iteracji</td>
  </tr>
</table>
