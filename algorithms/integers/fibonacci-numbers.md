# Liczby Fibonacciego

## Opis problemu

TODO

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna, większa od zera

#### Wynik

* $$n$$-ta liczba Fibonacciego

### Przykład

#### Dane

```
n := 10
```

**Wynik**: $$55$$ 

{% hint style="info" %}
**Wyjaśnienie**

Pierwszych kolejnych dziesięć liczb Fibonacciego to: $$1, 1, 2, 3, 5, 8, 13, 21, 34, 55$$ 
{% endhint %}

## Rozwiązanie rekurencyjne

TODO

### Pseudokod

```
funkcja Fib(n):
    1. Jeżeli n <= 2, to:
        2. Zwróć 1 i zakończ
    3. Zwróć Fib(n - 1) + Fib(n - 2) i zakończ
```

### Schemat blokowy

TODO

## Rozwiązanie iteracyjne

TODO

### Pseudokod

```
funkcja Fib(n):
    1. f1 := 1
    2. f2 := 1
    3. Od i := 3 do n + 1, wykonuj:
        4. f3 := f1 + f2
        5. f1 := f2
        6. f2 := f3
    7. Zwróć f2
```

### Schemat blokowy

TODO

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/integers/fibonacci-numbers.md" %}
[fibonacci-numbers.md](../../programming/c++/algorithms/integers/fibonacci-numbers.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/integers/fibonacci-numbers.md" %}
[fibonacci-numbers.md](../../programming/python/algorithms/integers/fibonacci-numbers.md)
{% endcontent-ref %}
