# Wyszukiwanie liniowe

## Opis problemu

{% content-ref url="../../../../algorithms/searching/linear-search.md" %}
[linear-search.md](../../../../algorithms/searching/linear-search.md)
{% endcontent-ref %}

## Istnienie elementu

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```swift
func linearSearch(array: [Int], number: Int) -> Bool {
    for el in array {
        if el == number {
            return true
        }
    }

    return false
}


let array = [8, 2, 9, 10, 5, 4, 2, 7, 18, 0]
let number = 7

let result = linearSearch(array: array, number: number)

if result {
    print("Liczba jest w tablicy")
} else {
    print("Liczby nie ma w tablicy")
}
```
{% endcode %}

### Link do implementacji

{% embed url="https://replit.com/@damiankurpiewski/LinearSearch1Swift#main.swift" %}
Wyszukiwanie liniowe - istnienie elementu
{% endembed %}

### Opis implementacji

Funkcja `linearSearch` (**linia 1**) zwraca jako wynik wartość prawda/fałsz i przyjmuje dwa argumenty: tablicę do przeszukania oraz wartość poszukiwanego elementu. Na początku funkcji przechodzimy pętlą przez wszystkie kolejne elementy w tablicy (**linia 2**). Dla każdego elementu sprawdzamy, czy jest to poszukiwana wartość (**linia 3**). Jeżeli tak, to zwracamy informację o znalezieniu wartości w tablicy (**linia 4**). Po przejściu przez wszystkie elementy i wyjściu z pętli (tzn. gdy nie znaleźliśmy poszukiwanego elementu) zwracamy wartość `false` informującą, że poszukiwany element nie znajduje się w tablicy (**linia 8**).

W części głównej programu na początku przygotowujemy dane do problemu: tablicę (**linia 12**) oraz wartość poszukiwanego elementu (**linia 13**). Następnie wywołujemy funkcję `linearSearch` z wcześniej przygotowanymi parametrami i jej wynik zapisujemy w nowej zmiennej `result` (**linia 15**). W zależności od wyniku (**linia 17**) wypisujemy odpowiedni komunikat (**linie 18 i 20**).

## Pozycja elementu

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```swift
func linearSearch(array: [Int], number: Int) -> Int {
    for i in 0...array.count - 1 {
        if array[i] == number {
            return i
        }
    }

    return -1
}


let array = [8, 2, 9, 10, 5, 4, 2, 7, 18, 0]
let number = 7

let index = linearSearch(array: array, number: number)

if index == -1 {
    print("Liczby nie ma w tablicy")
} else {
    print("Liczba jest pod indeksem \(index)")
}
```
{% endcode %}

### Link do implementacji

{% embed url="https://replit.com/@damiankurpiewski/LinearSearch2Swift#main.swift" %}
Wyszukiwanie liniowe - pozycja elementu
{% endembed %}

### Opis implementacji

Funkcja `linearSearch` (**linia 1**) zwraca jako wynik liczbę całkowitą i przyjmuje dwa argumenty: tablicę do przeszukania oraz wartość poszukiwanego elementu. Na początku funkcji przechodzimy pętlą przez wszystkie kolejne indeksy w tablicy od $$0$$ do rozmiaru tablicy minus jeden (**linia 2**). Rozmiar tablicy pobieramy za pomocą metody `count`. Dla każdego indeksu sprawdzamy, czy pod tym indeksem w tablicy znajduje się poszukiwana wartość (**linia 3**). Jeżeli tak, to zwracamy indeks tej wartości w tablicy (**linia 4**). Po przejściu przez wszystkie indeksy i wyjściu z pętli (tzn. gdy nie znaleźliśmy poszukiwanego elementu) zwracamy wartość `-1` informującą, że poszukiwany element nie znajduje się w tablicy (**linia 8**).

W części głównej programu na początku przygotowujemy dane do problemu: tablicę (**linia 12**) oraz wartość poszukiwanego elementu (**linia 13**). Następnie wywołujemy funkcję `linearSearch` z wcześniej przygotowanymi parametrami i jej wynik zapisujemy w nowej zmiennej `index` (**linia 15**). W zależności od wyniku (**linia 17**) wypisujemy odpowiedni komunikat (**linie 18 i 20**).

## Wszystkie pozycje elementu

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```swift
func linearSearch(array: [Int], number: Int) {
    for i in 0...array.count - 1 {
        if array[i] == number {
            print(i)
        }
    }
}


let array = [8, 2, 8, 4, 5, 6, 7, 8, 9, 8]
let number = 8

print("Indeksy, pod którymi znajduje się poszukiwana liczba:")
linearSearch(array: array, number: number)
```
{% endcode %}

### Link do implementacji

{% embed url="https://replit.com/@damiankurpiewski/LinearSearch3Swift#main.swift" %}
Wyszukiwanie liniowe - wszystkie pozycje elementu
{% endembed %}

### Opis implementacji

Funkcja `linearSearch` (**linia 1**) nie zwraca wyniku i przyjmuje dwa argumenty: tablicę do przeszukania oraz wartość poszukiwanego elementu. Na początku funkcji przechodzimy pętlą przez wszystkie kolejne indeksy w tablicy od $$0$$ do rozmiaru tablicy minus jeden (**linia 2**). Rozmiar tablicy pobieramy za pomocą metody `count`. Dla każdego indeksu sprawdzamy, czy pod tym indeksem w tablicy znajduje się poszukiwana wartość (**linia 3**). Jeżeli tak, to wypisujemy ten indeks (**linia 4**).

W części głównej programu na początku przygotowujemy dane do problemu: tablicę (**linia 10**) oraz wartość poszukiwanego elementu (**linia 11**). Następnie wypisujemy stosowny komunikat (**linia 13**) i wywołujemy funkcję `linearSearch` z wcześniej przygotowanymi parametrami (**linia 14**).