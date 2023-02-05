# Sortowanie koktajlowe

## Opis problemu

### Specyfikacja

#### Dane

* $$n$$ — liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ — tablica $$n$$ wartości całkowitych

#### Wynik

* Posortowana niemalejąco tablica $$A$$

### **Przykład**

#### Dane

```
n := 8
A := [6, 5, 3, 1, 8, 7, 2, 4]
```

#### Animacja

{% embed url="https://blackbat13.github.io/visul2/sorting/cocktail_shaker_sort/#array=%5B6%2C5%2C3%2C1%2C8%2C7%2C2%2C4%5D" %}

## Rozwiązanie

### Pseudokod

```
procedura SortowanieKoktajlowe(n, A):
    1. Od i := 1 do n div 2, wykonuj:
        2. Od j := i do n - i, wykonuj:
            3. Jeżeli A[j] > A[j + 1], to:
                4. Zamień(A[j], A[j + 1])
        5. Od j := n - i w dół do i + 1, wykonuj:
            6. Jeżeli A[j] < A[j - 1], to:
                7. Zamień(A[j], A[j - 1]
```

{% hint style="info" %}
**div** oznacza dzielenie całkowite
{% endhint %}

### Złożoność

$$O(n^2)$$ — kwadratowa

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/sorting/cocktail-shaker-sort.md" %}
[cocktail-shaker-sort.md](../../programowanie/c++/algorytmy/sorting/cocktail-shaker-sort.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/sortowanie/sortowanie-koktajlowe.md" %}
[sortowanie-koktajlowe.md](../../programowanie/python/algorytmy/sortowanie/sortowanie-koktajlowe.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programowanie/kotlin/algorithms/sorting/cocktail-shaker-sort.md" %}
[cocktail-shaker-sort.md](../../programowanie/kotlin/algorithms/sorting/cocktail-shaker-sort.md)
{% endcontent-ref %}