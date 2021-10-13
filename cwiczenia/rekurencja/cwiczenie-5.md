# Ćwiczenie 1

## Opis

Dana jest następująca specyfikacja i zgodna z nią funkcja rekurencyjna:

TODO - poprawić specyfikację

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna, liczba elementów w tablicy
* $$tab[1..n]$$ - tablica $$n$$ liczb całkowitych, numerowana od jedynki

#### Wynik

* $$suma$$ - suma elementów tablicy $$tab$$ 

### Funkcja rekurencyjna

$$
sum(tab, p, k) =  \begin{cases} 
      tab[p] & p == k \\
      tab[p] + sum(tab,p+1,k) & p < k \\
   \end{cases}
$$

## Zadania

1. Napisz pseudokod **rekurencyjnej** funkcji `sum(tab, p, k)` obliczający sumę elementów tablicy `tab` z zakresu `tab[p..k]` zgodnie z powyższą definicją funkcji rekurencyjnej.
2. Narysuj schemat blokowy **rekurencyjnej** funkcji `sum(tab, p, k)` obliczający sumę elementów tablicy `tab` z zakresu `tab[p..k]` zgodnie z powyższą definicją funkcji rekurencyjnej.

