# Rozwiązanie 3

## Treść zadania

Stwórz przycisk, który po kliknięciu wpisze w kolumnie C wszystkie wartości z zakresu `A1:A10`, które występują jednocześnie w zakresie `B1:B10`. Możesz założyć, że w obu zakresach wartości są unikalne w ramach danego zakresu.

## Rozwiązanie

```vb
Sub CzescWspolna_Click()
    Dim zakres1, zakres2, zakres3 As Range
    
    Set zakres1 = Range("A1:A10")
    Set zakres2 = Range("B1:B10")
    Set zakres3 = Range("C1")
    
    For Each kom1 In zakres1
        For Each kom2 In zakres2
            If kom1.Value = kom2.Value Then
                zakres3.Value = kom1.Value
                Set zakres3 = zakres3.Offset(1, 0)
                Exit For
            End If
        Next kom2
    Next kom1
End Sub
```
