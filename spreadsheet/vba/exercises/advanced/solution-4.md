# Rozwiązanie 4

## Treść zadania

Komórki `A1:A10` zawierają imiona i nazwiska oddzielone pojedynczą spacją. Stwórz przycisk, który po kliknięciu umieści w kolumnie B imiona, a w kolumnie C nazwiska z odpowiadających komórek z kolumny A.

## Rozwiązanie

```vb
Sub Podziel_Click()
    Dim zakres1, zakres2, zakres3 As Range
    Dim poz As Integer
    
    Set zakres1 = Range("A1:A10")
    Set zakres2 = Range("B1")
    Set zakres3 = Range("C1")
    
    For Each kom In zakres1
        poz = InStr(kom.Value, " ")
        zakres2.Value = Left(kom.Value, poz)
        zakres3.Value = Right(kom.Value, Len(kom.Value) - poz)
        Set zakres2 = zakres2.Offset(1, 0)
        Set zakres3 = zakres3.Offset(1, 0)
    Next kom
End Sub
```
