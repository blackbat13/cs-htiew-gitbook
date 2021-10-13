# Rozwiązanie

## Zadanie 1

TODO

## Zadanie 2

TODO

## Zadanie 3

Odpowiedź: **3**.

## Zadanie 4



|  n  | fun(n) |
| :-: | :----: |
|  1  |    0   |
|  2  |    1   |
|  3  |  **3** |
|  4  |  **5** |
|  5  |  **8** |
|  6  | **11** |

## Zadanie 5

```
funkcja fun_iter(n):
    1. Tworzymy tablicę S[1..n]
    2. S[1] := 0
    3. Dla i := 2 do n, wykonuj:
        4. Jeżeli n mod 2 = 0, to:
            5. S[i] := i - 1 + 2 * S[i / 2]
        6. W przeciwnym przypadku:
            7. S[i] := i - 1 + S[(i - 1) / 2] + S[(i + 1) / 2]
    8. Wypisz S[n]
```
