# Rozwiązanie 5

## Treść zadania

Napisz funkcję `ZliczWyrazy`, która dla podanego tekstu zwróci liczbę wyrazów w nim zawartych. Za wyraz uznajemy ciąg znaków nie zawierający spacji, a wyrazy są oddzielone pojedynczą spacją.

## Rozwiązanie

```vb
Function ZliczWyrazy(tekst As String) As Integer
    Dim poz, wynik As Integer

    poz = 1
    wynik = 0
    
    While poz > 0 And poz < Len(tekst)
        poz = InStr(poz, tekst, " ")
        If poz > 0 Then
            poz = poz + 1
        End If
        
        wynik = wynik + 1
    Wend
    
    ZliczWyrazy = wynik
End Function
```
