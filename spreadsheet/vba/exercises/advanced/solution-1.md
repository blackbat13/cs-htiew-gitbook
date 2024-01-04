# Rozwiązanie 1

## Treść zadania

Napisz funkcję `SzukajMax`, która dla podanego zakresu komórek, znajdzie i zwróci jako wynik adres komórki zawierającej wartość maksymalną. Jeżeli kilka komórek zawiera tę wartość, funkcja powinna zwrócić adres pierwszej z nich.

## Rozwiązanie

```vb
Function SzukajMax(zakres As Range) As String
    maks = Application.WorksheetFunction.Max(zakres)
    
    For Each kom In zakres
        If kom.Value = maks Then
            SzukajMax = kom.Address
            Exit For
        End If
    Next kom
End Function
```
