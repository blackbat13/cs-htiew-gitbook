# Rozwiązanie 2

## Treść zadania

Napisz funkcję `KonwTemp` zgodną z poniższą specyfikacją.

Skorzystaj z następujących wzorów:

- $$C = K - 273.15$$
- $$C = \frac{5}{9} * (F - 32)$$
- $$F = \frac{9}{5} * C + 32$$
- $$F = \frac{9}{5} * K - 459.67$$
- $$K = C + 273.15$$
- $$K = \frac{5}{9} * (F + 459.67)$$

gdzie:

* $$C$$ - temperatura podana w stopniach Celsjusza
* $$F$$ - temperatura podana w stopniach Fahrenheita
* $$K$$ - temperatura podana w stopniach Kelvina

### Specyfikacja

#### Dane

* $$temp$$ - liczba rzeczywista, temperatura do konwersji
* $$jednZ$$ - jeden znak, wielka litera oznaczająca jednostkę temperatury z której należy dokonać konwersji
* $$jednDo$$ - jeden znak, wielka litera oznaczająca jednostkę temperatury do której należy dokonać konwersji

#### Wynik

* Podana temperatura przekonwertowana z jednostki $$jednZ$$ do jednostki $$jednDo$$.

## Rozwiązanie

```vb
Function KonwTemp(temp As Double, jednZ As String, jednDo As String) As Double
    If jednZ = "C" Then
        If jednDo = "F" Then
            KonwTemp = ((temp * 9) / 5) + 32
        ElseIf jednDo = "K" Then
            KonwTemp = temp + 273.15
        End If
    ElseIf jednZ = "F" Then
        If jednDo = "C" Then
            KonwTemp = ((temp - 32) * 5) / 9
        ElseIf jednDo = "K" Then
            KonwTemp = ((temp + 459.67) * 5) / 9
        End If
    ElseIf jednZ = "K" Then
        If jednDo = "C" Then
            KonwTemp = temp - 273.15
        ElseIf jednDo = "F" Then
            KonwTemp = ((temp * 9) / 5) - 459.67
        End If
    End If
End Function
```
