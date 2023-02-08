# Sortowanie gnoma

## Opis problemu

Wyobraźmy sobie gnoma, który zarządza swoim ogródkiem, a konkretnie ustawia doniczki we właściwej kolejności. Doniczki ułożone są w rządku od lewej do prawej. Gnom przechodzi od lewej do prawej wzdłuż rzędu doniczek, uważnie je obserwując. Gdy tylko zauważy, że dwie sąsiednie doniczki są niewłaściwie ułożone, zamienia je miejscami i cofa się do poprzedniej doniczki. Gdy natomiast z doniczkami jest wszystko tak, jak należy, to przechodzi do kolejnej doniczki. Gdy gnom dotrze do końca doniczek może spokojnie stwierdzić, że wszystkie są ułożone we właściwym porządku.

### Specyfikacja

#### Dane

* $$n$$ — liczba naturalna, liczba elementów w tablicy
* $$A[1..n]$$ — tablica $$n$$ wartości całkowitych

#### Wynik

* Posortowana niemalejąco tablica $$A$$

### Przykład

Na początek przyjrzyjmy się poniższym animacjom. Spróbuj prześledzić jak kolejne wartości zamieniają się miejscami. Czy potrafisz, własnymi słowami, opisać przebieg algorytmu?

#### Dane

```
n := 8
A := [6, 5, 3, 1, 8, 7, 2, 4]
```

#### Animacja

{% embed url="https://blackbat13.github.io/visul2/sorting/gnome_sort/#array=%5B6%2C5%2C3%2C1%2C8%2C7%2C2%2C4%5D" %}

## Rozwiązanie

Zauważmy, że gnom ma do dyspozycji następujące operacje: 
- porównaj dwie sąsiednie doniczki: obecną z poprzednią,
- zamień dwie sąsiednie doniczki: obecną z poprzednią,
- idź o jedną doniczkę w prawo,
- idź o jedną doniczkę w lewo.

Gnom zaczyna swoją podróż od lewej strony, czyli od pierwszej doniczki, czy też od pierwszego elementu. Ponieważ może wyłącznie porównywać obecny element z poprzednim, to gdy znajduje się na samym początku nie ma wielkiego wyboru i musi pójść w prawo. Podobnie postępuje, gdy zauważy, że dwie sąsiednie doniczki są ułożone we właściwym porządku: przemieszcza się w prawo. Kiedy w takim razie gnom powinien pójść w lewo? Gdy napotka dwie sąsiednie doniczki, które są ułożone w złej kolejności. Wówczas zamienia je miejscami i idzie w lewo. I to wszystko powtarzamy tak długo, aż gnom wyjdzie poza rząd doniczek, czyli aż jego pozycja będzie większa od liczby elementów ($$n$$).

### Pseudokod

```
procedura SortGnoma(n, A):
    1. i := 1
    2. Dopóki i <= n, wykonuj:
        3. Jeżeli i = 1 lub A[i] >= A[i - 1], to:
            4. i := i + 1
        5. W przeciwnym przypadku:
            6. Zamień(A[i], A[i - 1])
            7. i := i - 1
```

### Złożoność

$$O(n^2)$$ — kwadratowa

Prześledzenie złożoności algorytmu sortowania gnoma może wydawać się nietrywialne, zauważmy jednak, że algorytm ten jest bardzo podobny do algorytmu sortowania przez wstawianie. Tak właściwie od wspomnianego algorytmu różni się jedynie dodatkowym "poruszaniem się w prawo", nie może mieć więc złożoności lepszej, niż tamten algorytm.

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/sorting/gnome-sort.md" %}
[gnome-sort.md](../../programming/c++/algorithms/sorting/gnome-sort.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/sorting/gnome-sort.md" %}
[gnome-sort.md](../../programming/python/algorithms/sorting/gnome-sort.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programming/kotlin/algorithms/sorting/gnome-sort.md" %}
[gnome-sort.md](../../programming/kotlin/algorithms/sorting/gnome-sort.md)
{% endcontent-ref %}