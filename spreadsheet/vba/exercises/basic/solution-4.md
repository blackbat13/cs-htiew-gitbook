# Rozwiązanie 4

## Treść zadania

Napisz funkcję `IleParzystych` zliczającą ile komórek z podanego zakresu zawiera liczby parzyste.

## Rozwiązanie

```vb
Function IleParzystych(zakres As Range) As Integer
    Dim wynik As Integer
    
    wynik = 0

    For Each kom In zakres
        If kom.Value Mod 2 = 0 Then
            wynik = wynik + 1
        End If
    Next kom
    
    IleParzystych = wynik
End Function
```
