# Całkowanie numeryczne

## Opis problemu

Hasło "całkowanie numeryczne" może brzmieć strasznie, ale samo pojęcie jest dość proste do zrozumienia. To nic innego, niż policzenie pola pod wykresem funkcji w zadanym przedziale. Oczywiście w ogólności to zadanie jest dość skomplikowane obliczeniowo, dlatego tutaj skupimy się na przybliżeniu tej wartości.

Wyróżniamy dwie podstawowe metody: metodę prostokątów i metodę trapezów.

### Specyfikacja

#### Dane

* $$f(x)$$ — funkcja, której wykres nas interesuje
* $$a$$ — liczba rzeczywista, początek przedziału
* $$b$$ — liczba rzeczywista, koniec przedziału
* $$n$$ — liczba podziałów (im większa, tym większa dokładność)

#### Wynik

* $$pole$$ — przybliżona wartość pola pod wykresem funkcji $$f(x)$$ w przedziale $$[a,b]$$

## Rozwiązanie — metoda prostokątów

Idea tej metody jest prosta: podzielmy pole pod wykresem funkcji na prostokąty i policzmy ich pole.

### Pseudokod

```
funkcja MetodaProstokatow(f, a, b, n):
    1. pole := 0
    2. sz := (b - a) / n
    3. c := a + sz
    
    4. Dopóki c <= b, wykonuj:
        5. wys := f(c)
        6. pole := pole + sz * wys
        7. c := c + sz
        
    8. Zwróć pole
```

## Rozwiązanie — metoda trapezów

W celu uzyskania lepszej dokładności, możemy podzielić pole pod wykresem funkcji na trapezy.

### Pseudokod

```
funkcja MetodaTrapezow(f, a, b, n):
    1. pole := 0
    2. sz := (b - a) / n
    3. c := a + sz
    
    4. Dopóki c <= b, wykonuj:
        5. pole := pole + (f(c - sz) + f(c) * sz) / 2
        6. c := c + sz

    7. Zwróć pole
```

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/numerical-methods/numerical-integration.md" %}
[numerical-integration.md](../../programming/c++/algorithms/numerical-methods/numerical-integration.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/numerical-methods/numerical-integration.md" %}
[numerical-integration.md](../../programming/python/algorithms/numerical-methods/numerical-integration.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programming/kotlin/algorithms/numerical-methods/numerical-integration.md" %}
[numerical-integration.md](../../programming/kotlin/algorithms/numerical-methods/numerical-integration.md)
{% endcontent-ref %}