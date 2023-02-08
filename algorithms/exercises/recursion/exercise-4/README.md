# Ćwiczenie 4

## Opis

Dany jest następujący pseudokod, zgodny z poniższą częściową specyfikacją:

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna, $$n>0$$ 

### Pseudokod

```
funkcja fun(n):
    1. Jeżeli n = 1, to
        2. Zwróć 0 i zakończ
    3. Jeżeli n mod 2 = 0, to
        4. Zwróć n - 1 + 2 * fun(n / 2) i zakończ
    5. Jeżeli n mod 2 = 1, to
        6. Zwróć n - 1 + fun((n - 1) / 2) + fun((n + 1) / 2)
```

{% hint style="info" %}
**mod** oznacza resztę z dzielenia
{% endhint %}

## Zadania

### Zadanie 1

Wykonanie funkcji rekurencyjnej można przedstawić w postaci _drzewa wywołań rekurencyjnych_ ilustrującego wszystkie wywołania funkcji po jej uruchomieniu dla zadanego argumentu. Narysuj takie drzewo dla wywołania `fun(5)`.

### Zadanie 2

Narysuj _drzewo wywołań rekurencyjnych_ dla wywołania `fun(7)`.

### Zadanie 3

Ile razy zostanie wykonane wywołanie `fun(1)` podczas obliczania `fun(7)`?.

### Zadanie 4

Uzupełnij poniższą tabelę, podając wartości funkcji `fun` dla wskazanych argumentów.

|  n  | fun(n) |
| :-: | :----: |
|  1  |    0   |
|  2  |    1   |
|  3  |        |
|  4  |        |
|  5  |        |
|  6  |        |

### Zadanie 5

Napisz **iteracyjną** wersję funkcji `fun` (bez użycia rekurencji).