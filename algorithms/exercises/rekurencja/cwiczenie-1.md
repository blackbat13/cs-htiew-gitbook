# Ćwiczenie 1

## Opis

Dana jest następująca specyfikacja i zgodna z nią funkcja rekurencyjna:

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna, liczba elementów w tablicy
* $$tab[1..n]$$ - tablica $$n$$ liczb całkowitych, numerowana od jedynki
* $$p, k$$ - początek i koniec zakresu, liczby naturalne

#### Wynik

* $$suma$$ - suma elementów tablicy $$tab[p..k]$$, tzn. $$tab[p]+tab[p+1]+...+tab[k]$$ 

### Funkcja rekurencyjna

$$
sum(tab, p, k) =  \begin{cases} 
      tab[p] & p == k \\
      tab[p] + sum(tab,p+1,k) & p < k \\
   \end{cases}
$$

## Zadania

### Zadanie 1

Napisz pseudokod **rekurencyjnej** funkcji `sum(tab, p, k)` obliczający sumę elementów tablicy `tab` z zakresu `tab[p..k]` zgodnie z powyższą definicją funkcji rekurencyjnej.

### Zadanie 2

Narysuj schemat blokowy **rekurencyjnej** funkcji `sum(tab, p, k)` obliczający sumę elementów tablicy `tab` z zakresu `tab[p..k]` zgodnie z powyższą definicją funkcji rekurencyjnej.