# Rozwiązanie 7

## Treść zadania

Napisz funkcję `Fibonacci` zgodną z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna

#### Wynik

* Liczba Fibonacciego o indeksie $$n$$.

## Rozwiązanie

```vb
Function Fibonacci(n As Integer) As Long
    Dim a As Long
    Dim b As Long
    Dim temp As Long
    
    a = 0
    b = 1

    For i = 1 To n
        temp = a + b
        a = b
        b = temp
    Next i
    
    Fibonacci = a
End Function
```
