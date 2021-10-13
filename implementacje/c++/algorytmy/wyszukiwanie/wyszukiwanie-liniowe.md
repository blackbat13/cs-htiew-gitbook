# Wyszukiwanie liniowe

## Opis problemu

{% content-ref url="../../../../wyszukiwanie/liniowe-wyszukiwanie.md" %}
[liniowe-wyszukiwanie.md](../../../../wyszukiwanie/liniowe-wyszukiwanie.md)
{% endcontent-ref %}

## Istnienie elementu

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Checks if given number is present in the array
/// \param array - array to search in
/// \param length - length of array
/// \param number - element to find
/// \return true if the element is present in the array, false otherwise
bool linearSearch(int array[], int n, int number) {
    for (int i = 0; i < n; i++) {
        if (array[i] == number) {
            return true;
        }
    }

    return false;
}

int main() {
    int array[10] = {8, 2, 9, 10, 5, 4, 2, 7, 18, 0};
    int n = 10;
    int number = 7;
    
    bool result = linearSearch(array, n, number);
    
    if (result) {
        cout << "Liczba jest w tablicy" << endl;
    } else {
        cout << "Liczby nie ma w tablicy" << endl;
    }

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/2ZCRND" %}
Wyszukiwanie liniowe - istnienie elementu
{% endembed %}

### Opis implementacji

Funkcja `linearSearch` (**linia 10**) zwraca jako wynik wartość prawda/fałsz i przyjmuje trzy argumenty: tablicę do przeszukania, rozmiar tablicy oraz wartość poszukiwanego elementu. Na początku funkcji przechodzimy pętlą przez wszystkie kolejne indeksy w tablicy od $$0$$ do $$n-1$$ włącznie (**linia 11**). Dla każdego indeksu sprawdzamy, czy pod tym indeksem w tablicy znajduje się poszukiwana wartość (**linia 12**). Jeżeli tak, to zwracamy informację o znalezieniu wartości w tablicy (**linia 13**). Po przejściu przez wszystkie indeksy i wyjściu z pętli (tzn. gdy nie znaleźliśmy poszukiwanego elementu) zwracamy wartość `false` informującą, że poszukiwany element nie znajduje się w tablicy (**linia 17**).

W części głównej programu na początku przygotowujemy dane do problemu: tablicę (**linia 21**), jej rozmiar (**linia 22**), oraz wartość poszukiwanego elementu (**linia 23**). Następnie wywołujemy funkcję `linearSearch` z wcześniej przygotowanymi parametrami i jej wynik zapisujemy w nowej zmiennej `result` (**linia 25**). W zależności od wyniku (**linia 27**) wypisujemy odpowiedni komunikat (**linie 28 i 30**).

## Pozycja elementu

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Perform linear search on given array
/// \param array - array to search in
/// \param length - length of array
/// \param number - element to find
/// \return index of element in array, or -1 if not found
int linearSearch(int array[], int n, int number) {
    for (int i = 0; i < n; i++) {
        if (array[i] == number) {
            return i;
        }
    }

    return -1;
}

int main() {
    int array[10] = {8, 2, 9, 10, 5, 4, 2, 7, 18, 0};
    int n = 10;
    int number = 7;

    int index = linearSearch(array, n, number);
    
    if (index == -1) {
        cout << "Liczby nie ma w tablicy" << endl;
    } else {
        cout << "Liczba jest pod indeksem " << index << endl;
    }

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/bIo8zN" %}
Wyszukiwanie liniowe - pozycja elementu
{% endembed %}

### Opis implementacji

Funkcja `linearSearch` (**linia 10**) zwraca jako wynik liczbę całkowitą i przyjmuje trzy argumenty: tablicę do przeszukania, rozmiar tablicy oraz wartość poszukiwanego elementu. Na początku funkcji przechodzimy pętlą przez wszystkie kolejne indeksy w tablicy od $$0$$ do $$n-1$$ włącznie (**linia 11**). Dla każdego indeksu sprawdzamy, czy pod tym indeksem w tablicy znajduje się poszukiwana wartość (**linia 12**). Jeżeli tak, to zwracamy indeks tej wartości w tablicy (**linia 13**). Po przejściu przez wszystkie indeksy i wyjściu z pętli (tzn. gdy nie znaleźliśmy poszukiwanego elementu) zwracamy wartość $$-1$$ informującą, że poszukiwany element nie znajduje się w tablicy (**linia 17**).

W części głównej programu na początku przygotowujemy dane do problemu: tablicę (**linia 21**), jej rozmiar (**linia 22**), oraz wartość poszukiwanego elementu (**linia 23**). Następnie wywołujemy funkcję `linearSearch` z wcześniej przygotowanymi parametrami i jej wynik zapisujemy w nowej zmiennej `index` (**linia 25**). W zależności od wyniku (**linia 27**) wypisujemy odpowiedni komunikat (**linie 28 i 30**).

## Wszystkie pozycje elementu

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Prints all positions of the given value
/// \param array - array to search in
/// \param length - length of array
/// \param number - element to find
void linearSearch(int array[], int n, int number) {
    for (int i = 0; i < n; i++) {
        if (array[i] == number) {
            cout << i << endl;
        }
    }
}

int main() {
    int array[10] = {8, 2, 9, 10, 5, 4, 2, 7, 18, 0};
    int n = 10;
    int number = 7;

    cout << "Indeksy, pod ktorymi znajduje sie poszukiwana liczba:" << endl;
    linearSearch(array, n, number);

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/PXatsk" %}
Wyszukiwanie liniowe - wszystkie pozycje elementu
{% endembed %}

### Opis implementacji

Funkcja `linearSearch` (**linia 9**) nie zwraca wyniku i przyjmuje trzy argumenty: tablicę do przeszukania, rozmiar tablicy oraz wartość poszukiwanego elementu. Na początku funkcji przechodzimy pętlą przez wszystkie kolejne indeksy w tablicy od $$0$$ do $$n-1$$ włącznie (**linia 10**). Dla każdego indeksu sprawdzamy, czy pod tym indeksem w tablicy znajduje się poszukiwana wartość (**linia 11**). Jeżeli tak, to wypisujemy ten indeks (**linia 12**). 

W części głównej programu na początku przygotowujemy dane do problemu: tablicę (**linia 18**), jej rozmiar (**linia 19**), oraz wartość poszukiwanego elementu (**linia 20**). Następnie wypisujemy stosowny komunikat i wywołujemy funkcję `linearSearch` z wcześniej przygotowanymi parametrami.
