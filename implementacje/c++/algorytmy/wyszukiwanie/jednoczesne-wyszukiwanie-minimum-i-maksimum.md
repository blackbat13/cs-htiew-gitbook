# Jednoczesne wyszukiwanie minimum i maksimum

## Opis problemu

{% content-ref url="../../../../wyszukiwanie/jednoczesne-znajdowanie-minimum-i-maksimum.md" %}
[jednoczesne-znajdowanie-minimum-i-maksimum.md](../../../../wyszukiwanie/jednoczesne-znajdowanie-minimum-i-maksimum.md)
{% endcontent-ref %}

## Podejście naiwne

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Find minimum and maximum value in given array using naive algorithm
/// \param array - array to search in
/// \param length - length of given array
void findMinMaxNaive(int array[], int n) {
    int min, max;
    
    min = array[0];
    max = array[0];
    
    for (int i = 1; i < n; i++) {
        if (array[i] < min) {
            min = array[i];
        } else if (array[i] > max) {
            max = array[i];
        }
    }

    cout << "Min: " << min << endl;
    cout << "Max: " << max << endl;
}

int main() {
    int array[11] = {3, 6, 1, 9, 10, 4, -4, 6, 12, 5, 11};

    findMinMaxNaive(array, 11);
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/EJvOcg" %}
Jednoczesne znajdowanie min i max - podejście naiwne 
{% endembed %}

### Opis implementacji

Funkcja `findMinMaxNaive` (**linia 8**) przyjmuje tablicę o zadanej długości i wypisuje jej elementy minimalny i maksymalny, korzystając z naiwnego algorytmu jednoczesnego znajdowania minimum i maksimum.

Na początku tworzymy dwie zmienne do zapamiętania wartości min i max (**linia 9**), a następnie przypisujemy do nich wartość pierwszego elementu przeszukiwanej tablicy (**linie 11 i** **12**). Kolejnym etapem jest przejrzenie wszystkich pozostałych elementów tablicy za pomocą pętli (**linia 14**). Jeżeli sprawdzany element z tablicy ma wartość mniejszą od obecnej wartości minimum (**linia 15**), to zapamiętujemy nową wartość minimum (**linia 16**). W przeciwnym wypadku sprawdzamy, czy obecny element ma wartość większą od obecnej wartości maksimum (**linia 17**), a jeżeli tak to zapamiętujemy nową wartość maksimum (**linia 18**). Na koniec, po przejściu przez wszystkie elementy tablicy, wypisujemy znalezione wartości minimum i maksimum (**linie 22 i 23**).

W części głównej tworzymy przykładową tablicę (**linia 27**), a następnie wywołujemy funkcję `findMinMaxNaive` (**linia 29**).

## Podejście optymalne

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Find minimum and maximum value in given array using optimal divide and conquer algorithm
/// \param array - array to search in
/// \param length - length of given array
void findMinMaxOptimal(int array[], int length) {
    int min, max;
    int middle = (length + 1) / 2;
    int minCandidates[middle], maxCandidates[middle];
    
    for (int i = 1; i < length; i += 2) {
        if (array[i - 1] < array[i]) {
            minCandidates[i / 2] = array[i - 1];
            maxCandidates[i / 2] = array[i];
        } else {
            minCandidates[i / 2] = array[i];
            maxCandidates[i / 2] = array[i - 1];
        }
    }

    if (length % 2 != 0) {
        minCandidates[middle - 1] = array[length - 1];
        maxCandidates[middle - 1] = array[length - 1];
    }

    min = minCandidates[0];
    max = maxCandidates[0];
    
    for (int i = 1; i < middle; i++) {
        if (minCandidates[i] < min) {
            min = minCandidates[i];
        }

        if (maxCandidates[i] > max) {
            max = maxCandidates[i];
        }
    }

    cout << "Min: " << min << endl;
    cout << "Max: " << max << endl;
}

int main() {
    int array[11] = {3, 6, 1, 9, 10, 4, -4, 6, 12, 5, 11};

    findMinMaxOptimal(array, 11);
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/cLyaKc" %}
Jednoczesne wyszukiwanie min i max - podejście optymalne
{% endembed %}

### Opis implementacji

Funkcja `findMinMaxOptimal` (**linia 8**) przyjmuje tablicę o zadanej długości i wypisuje jej elementy minimalny i maksymalny, korzystając z optymalnego algorytmu jednoczesnego znajdowania minimum i maksimum.

Na początku funkcji definiujemy dwie tablice pomocnicze (**linia 11**): kandydatów na minimum (`minCandidates`) oraz kandydatów na maksimum (`maxCandidates`) . Każda z tych tablic ma długość równą połowie długości tablicy początkowej (zwiększonej o jeden w przypadku tablic o nieparzystej długości).

Następnie przechodzimy pętlą przez każdą sąsiadującą parę elementów z początkowej tablicy (**linia 13**). Jeżeli pierwszy z elementów jest mniejszy od swojego sąsiada (**linia 14**), to pierwszy z pary wrzucamy do tablicy kandydatów na minimum (**linia 15**), a kolejny do tablicy kandydatów na maksimum (**linia 16**). W przeciwnym wypadku postępujemy na odwrót (**linie 18** **i** **19**).

Jeżeli początkowa tablica jest nieparzystej długości (**linia 23**), to jej ostatni element dopisujemy do obu tablic pomocniczych: kandydatów na minimum (**linia 24**) i kandydatów na maksimum (**linia 25**) na ostatnie pozycje w tych tablicach.

Następnie przechodzimy do poszukiwania minimum i maksimum. Na początek przyjmujemy początkowe wartości tablic pomocniczych jako obecne wartości minimum i maksimum. Minimum bierzemy z kandydatów na minimum (**linia 28**), a maksimum z kandydatów na maksimum (**linia 29**).

W kolejnym kroku przechodzimy pętlą przez obie tablice pomocnicze (**linia 31**). Najpierw sprawdzamy, czy znaleźliśmy element mniejszy od obecnej wartości minimum w tablicy kandydatów na minimum (**linia 32**). Jeżeli tak, to przyjmujemy nową wartość minimum (**linia 33**).\
Podobnie postępujemy w przypadku maksimum. Jeżeli w tablicy kandydatów na maksimum znaleźliśmy element większy od obecnej wartości maksimum (**linia 36**), to przyjmujemy nową wartość maksimum (**linia 37**).

Na końcu funkcji wypisujemy znalezione wartości minimum (**linia 41**) oraz maksimum (**linia 42**).

W części głównej tworzymy przykładową tablicę (**linia 46**), a następnie wywołujemy funkcję `findMinMaxOptimal` (**linia 48**).
