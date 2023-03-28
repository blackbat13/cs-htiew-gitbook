# Metoda Monte Carlo

## Opis problemu

## Obliczanie przybliżonej wartości liczby PI

### Specyfikacja

#### Dane

* $$n$$ — liczba prób (im większa, tym większa dokładność)

#### Wynik

* $$pi$$ — przybliżona wartość liczby $$\pi$$

### Symulacja

{% embed url="https://academo.org/demos/estimating-pi-monte-carlo/" %}
Symulacja Monte Carlo
{% endembed %}

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
    
    8. Zwróć (4 * wkole) / n
```

### Schemat blokowy

```mermaid
flowchart TD
	START(["MonteCarloPi(n)"]) --> K1[wkole := 0\ni := 1]
	K1 --> K2{i <= n}
	K2 -- PRAWDA --> K3["x := losowa(-1, 1)\ny := losowa(-1, 1)\nodl := x * x + y * y"]
	K3 --> K6{odl <= 1}
	K6 -- PRAWDA --> K7[wkole := wkole + 1]
	K7 --> K2i[i := i + 1]
	K6 -- FAŁSZ --> K2i
	K2i --> K2
	K2 -- FAŁSZ ---> K8[/"Zwróć ((4 * wkole) / n)"/]
	K8 ---> STOP([STOP])
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
