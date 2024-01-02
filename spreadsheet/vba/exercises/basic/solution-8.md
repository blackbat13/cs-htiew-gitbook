# Rozwiązanie 8

## Treść zadania

Napisz funkcję `ZWielkiej` zgodną z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$wyraz$$ - ciąg znaków

#### Wynik

* Podany wyraz, w którym pierwsza litera jest wielka.

## Rozwiązanie

```vb
Function ZWielkiej(wyraz As String) As String
    Dim wynik As String
    Dim pierwsza As String
    
    pierwsza = Left(wyraz, 1)
    wynik = Right(wyraz, Len(wyraz) - 1)
    wynik = UCase(pierwsza) + wynik
    
    ZWielkiej = wynik
End Function

```
