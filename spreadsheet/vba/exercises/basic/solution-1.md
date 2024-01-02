# Rozwiązanie 1

## Treść zadania

Napisz funkcję `CnaF` zgodną z poniższą specyfikacją.

Skorzystaj z następującego wzoru:

$$F = \frac{9}{5} * C + 32$$

gdzie:

* $$C$$ - temperatura podana w stopniach Celsjusza
* $$F$$ - temperatura podana w stopniach Fahrenheita

### Specyfikacja

#### Dane

* $$temp$$ - liczba rzeczywista, temperatura podana w stopniach Celsjusza

#### Wynik

* Podana temperatura przekonwertowana na stopnie Fahrenheita.

## Rozwiązanie

```vb
Function CtoF(temp As Double) As Double
    CtoF = ((temp * 9) / 5) + 32
End Function
```
