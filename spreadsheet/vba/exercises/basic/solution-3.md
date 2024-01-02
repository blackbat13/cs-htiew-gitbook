# Rozwiązanie 3

## Treść zadania

Napisz funkcję `CzyParzysta` zgodną z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna

#### Wynik

* PRAWDA, jeżeli $$n$$ jest liczbą parzystą, FAŁSZ w przeciwnym przypadku.

## Rozwiązanie

```vb
Function CzyParzysta(n As Integer) As Boolean
    If n Mod 2 = 0 Then
        CzyParzysta = True
    Else
        CzyParzysta = False
    End If
End Function
```
