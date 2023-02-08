# Metoda Monte Carlo

## Opis problemu

## Obliczanie przybliżonej wartości liczby PI

### Specyfikacja

#### Dane

* $$n$$ — liczba prób (im większa, tym większa dokładność)

#### Wynik

* $$pi$$ — przybliżona wartość liczby $$\pi$$

### Rozwiązanie

### Pseudokod

```
funkcja MonteCarloPI(n)
    1. wkole := 0
    2. Dla i := 1 do n, wykonuj:
        3. x := losowa liczba rzeczywista z przedziału [-1, 1]
        4. y := losowa liczba rzeczywista z przedziału [-1, 1]
        5. odl := (x * x) + (y * y)
        6. Jeżeli odl <= 1, to:
            7. wkole := wkole + 1
    
    8. wynik := (4 * wkole) / n
    9. Zwróć wynik
```

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/numerical-methods/monte-carlo.md" %}
[monte-carlo.md](../../programming/c++/algorithms/numerical-methods/monte-carlo.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/numerical-methods/monte-carlo.md" %}
[monte-carlo.md](../../programming/python/algorithms/numerical-methods/monte-carlo.md)
{% endcontent-ref %}
