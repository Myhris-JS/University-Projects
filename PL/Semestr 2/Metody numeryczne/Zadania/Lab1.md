# Laboratorium 1 (24.04.2024)
### Zadanie 1
Stwórz wektor (np.array) składający się z pięciu dowolnych wartości liczbowych. Wyświetl utworzony wektor. Następnie, zmień liczbę na drugiej pozycji (nie pod indeksem 2, tylko na drugiej pozycji) na -1, a liczbę znajdującą się na pozycji czwartej powiększ dwa razy.

### Zadanie 2
Stwórz macierz dwuwymiarową o wymiarach 3 na 4 (3 wiersze, 4 kolumny) składającą się z losowych wartości za pomocą polecenia np.random.randint. Przedział wartości może być dowolny. Następnie, wyświetl wygenerowaną macierz.
Wykonaj następujące polecenia:
* Wyświetl drugi wiersz macierzy (tutaj i dalej to są pozycje, nie indeksy. Chyba że jest powiedziane pod
indeksem);
* Wyświetl drugą kolumnę macierzy;
* Pomnóż cały pierwszy wiersz razy dwa.
* Wyświetl kwadratową macierz 2x2 składają się z pierwszych dwóch elementów pierwszego wiersza i
pierwszych dwóch elementów drugiego wiersza.

### Zadanie 3
Napisz funkcję simple_plot(a, b), która wyświetli wykres, dwóch podanych wektorów a oraz b. Wektor a będzie
określony przerywaną linią czerwoną, natomiast wektor b będzie określony ciągłą linią niebieską. Legenda do
wykresu pojawi się w prawym górnym rogu. Oś x powinna być podpisana x, oś y powinna być podpisana y.
Dodatkowo należy dodać podpis wykresu oraz siatkę. Siatka powinna być zdefiniowana zieloną linią przerywaną
z przezroczystością 0.5 i grubością linii 1.15.

*Pomoc:* Chodzi o to żeby utworzyć dwa wektory wartości (np.array lub lista z dowolnymi liczbami) i wrzucić
je do funkcji plt.plot() (każdy osobno do innej).

### Zadanie 4
Napisz funkcje func_plot(vmin, vmax, step), która wykona wykres funkcji \\(f(x) = x^2 − 4x + 8\\). Argument
vmin oznacza wartość początkową wektora x, vmax oznacza wartość końcową wektora x, step oznacza krok
w wektorze x.

### Zadanie 5
Napisz funkcję multi_plot(sizes, labels), która w jednym oknie wyświetli dwa wykresy: wykres kołowy dla
podanych rozmiarów w wektorze sizes oraz podpisów labels, oraz wykres słupkowy dla podanych rozmiarów
w wektorze sizes oraz podpisów labels. Jako przykładowe dane można wziąć na przykład liczbę mieszkańców
4-5 polskich miast oraz nazwy tych miast.

*Pomoc*:
* [Wykres słupkowy (bar).](https://matplotlib.org/stable/plot_types/basic/bar.html#sphx-glr-plot-types-basic-bar-py)
* [Wykres kołowy (pie).](https://matplotlib.org/stable/plot_types/stats/pie.html#sphx-glr-plot-types-stats-pie-py)
* [Kilka wykresów w jednym oknie.](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplot.html#sphx-glr-gallery-subplots-axes-and-figures-subplot-py)

### Zadanie 6
Napisz funkcję scatter_plot(), która wyświetli wykres punktowy dwóch zestawów danych (po 100 punktów każdy): współrzędne x i y punktów w pierwszym zestawie ma być wygenerowane za pomocą funkcji
np.random.rand(), a współrzędne drugiego zestawu danych mają być wygenerowane za pomocą funkcji
np.ranom.randn(). Pierwszy zestaw punktów ma być wizualizowany w kolorze niebieskim, a drugi w kolorze zielonym. Punkty drugiego zestawu danych muszą być w postaci gwiazdek (marker). Na wykresie ma
być pokazana legenda i siatka.

*Pomoc:*
* [Podstawowy przykład.](https://matplotlib.org/stable/plot_types/basic/scatter_plot.html#sphx-glr-plot-types-basic-scatter-plot-py)
* [Dokumentacja funkcji scatter().](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html#matplotlib.axes.Axes.scatter)
* [Przykład legendy.](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html#sphx-glr-gallery-lines-bars-and-markers-scatter-with-legend-py)

### Zadanie 7
Napisz funkcję make_3D(x, y), która wyświetli wykres powierzchni 3D funkcji funkcji f(x, y) = $\sqrt{x^2 + y^2}$

Oś x powinna być podpisana x, oś y powinna być podpisana y, oś z powinna być podpisana jako z.

*Pomoc:* [Przykład takiego wykresu.](https://matplotlib.org/stable/gallery/mplot3d/surface3d.html#sphx-glr-gallery-mplot3d-surface3d-py)
