# Rozwiązanie 6

## Treść zadania

Napisz funkcję `IleCyfr` zgodną z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna

#### Wynik

* Liczba cyfr liczby $$n$$.

## Rozwiązanie

```vb
Function IleCyfr(n As Long) As Integer
    Dim wynik As Integer
    
    wynik = 1

    While n > 9
        n = n / 10
        wynik = wynik + 1
    Wend
    
    IleCyfr = wynik
End Function
```
