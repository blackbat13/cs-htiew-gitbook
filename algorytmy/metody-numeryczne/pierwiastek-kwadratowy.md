# Pierwiastek kwadratowy

## Opis problemu

TODO

### Specyfikacja

#### Dane

* $$n$$ - liczba rzeczywista.
* $$p$$ - liczba rzeczywista, dokładność.

#### Wynik

* $$\sqrt{n}$$ policzony z dokładnością $$p$$.&#x20;

### Przykład

TODO

## Rozwiązanie - metoda Herona

TODO

### Pseudokod

```
funkcja MetodaHerona(n, p)
    1. x1 := n / 2
    2. x2 := (x1 + (n / x1)) / 2
    3. Dopóki |x2 - x1| > p, wykonuj:
        4. x1 := (x2 + (n / x2)) / 2
        3. Zamień(x1, x2)
    4. Zwróć x2
```

### Złożoność

TODO

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/metody-numeryczne/pierwiastek-kwadratowy.md" %}
[pierwiastek-kwadratowy.md](../../programowanie/c++/algorytmy/metody-numeryczne/pierwiastek-kwadratowy.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/metody-numeryczne/pierwiastek-kwadratowy.md" %}
[pierwiastek-kwadratowy.md](../../programowanie/python/algorytmy/metody-numeryczne/pierwiastek-kwadratowy.md)
{% endcontent-ref %}
