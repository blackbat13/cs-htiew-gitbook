# Rozwiązanie 5

## Treść zadania

Napisz funkcję `NWW` zgodną z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$a$$ - liczba naturalna
* $$b$$ - liczba naturalna

#### Wynik

* Najmniejsza wspólna wielokrotność liczb $$a$$ i $$b$$.

## Rozwiązanie

```vb
Function NWW(a As Integer, b As Integer) As Integer
    Dim na As Integer
    Dim nb As Integer

    na = a
    nb = b

    While na <> nb
        If na < nb Then
            na = na + a
        Else
            nb = nb + b
        End If
    Wend
    
    NWW = na
End Function
```
