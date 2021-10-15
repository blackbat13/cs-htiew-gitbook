# Sito Eratostenesa

## Opis problemu

TODO

### Specyfikacja

#### Dane:

* $$n$$ - liczba całkowita

#### Wynik:

* Wszystkie liczby pierwsze od $$1$$ do $$n$$ włącznie.

### Przykład

#### Dane

```
n := 10
```

#### Wynik

$$2, 3, 5, 7$$ 

### Prezentacja

{% file src="../../.gitbook/assets/Sito Eratostenesa.pdf" %}
Prezentacja
{% endfile %}

## Rozwiązanie

TODO

### Pseudokod

```
funkcja SitoEratostenesa(n):
    1. A[1..n] := tablica wypełniona wartościami true
    2. A[1] := false
    3. Od i := 2 do n wykonuj:
        4. Jeżeli A[i] = true, to:
            5. j := i * 2
            6. Dopóki j <= n, wykonuj:
                7. A[j] := false
                8. j := j + i
    9. Od i := 2 do n, wykonuj:
        10. Jeżeli A[i] = true, to:
            11. Wypisz i
```

### Złożoność

TODO

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/algorytmy-na-liczbach-calkowitych/sito-eratostenesa.md" %}
[sito-eratostenesa.md](../../programowanie/c++/algorytmy/algorytmy-na-liczbach-calkowitych/sito-eratostenesa.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/algorytmy-na-liczbach-calkowitych/sito-eratostenesa.md" %}
[sito-eratostenesa.md](../../programowanie/python/algorytmy/algorytmy-na-liczbach-calkowitych/sito-eratostenesa.md)
{% endcontent-ref %}
