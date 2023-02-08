# Rozkład na czynniki pierwsze

## Opis problemu

TODO

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna, większa od zera

#### Wynik

* Rozkład liczby $$n$$ na czynniki pierwsze 

### Przykład

#### Dane

```
n := 124
```

**Wynik**: $$2, 2, 31$$ 

## Rozwiązanie

TODO

### Pseudokod

```
funkcja Rozklad(n):
    1. i := 2
    2. Dopóki n > 1, wykonuj:
        3. Jeżeli n mod i = 0, to:
            4. Wypisz i
            5. n := n div i
        6. W przeciwnym przypadku:
            7. i := i + 1
```

{% hint style="info" %}
**mod** oznacza resztę z dzielenia

**div** oznacza dzielenie całkowite
{% endhint %}

### Schemat blokowy

TODO

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/integers/prime-factors.md" %}
[prime-factors.md](../../programming/c++/algorithms/integers/prime-factors.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/integers/prime-factors.md" %}
[prime-factors.md](../../programming/python/algorithms/integers/prime-factors.md)
{% endcontent-ref %}
