# Rozwiązanie 1

## Treść zadania

Stwórz przycisk, który po kliknięciu pokoloruje wszystkie komórki w zakresie `A1:A10`, które zawierają wartość poniżej średniej z tego zakresu.

## Rozwiązanie

```vb
Sub Przycisk1_Click()
    Dim zakres As Range
    Dim srednia As Double
    
    Set zakres = Range("A1:A10")
    srednia = Application.WorksheetFunction.Average(zakres)
    
    For Each kom In zakres
        If kom.Value < srednia Then
            kom.Interior.Color = RGB(0, 255, 0)
        End If
    Next kom
End Sub
```
