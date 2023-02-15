# Odległość Levenshteina (edycyjna)

## Opis problemu

Odległość edycyjna to liczba operacji zamiany litery, usunięcia litery i wstawienia litery, które trzeba wykonać, by zmienić jeden tekst w drugi.

### Specyfikacja

#### Dane

- **tekst1**, **tekst2** - dwa teksty, ciągi znaków liter angielskiego

#### Wynik

- Odległość Levenshteina pomiędzy **tekst1** a **tekst2**.

### Funkcje pomocnicze

- **Długość(tekst)** - zwraca długość tekstu
- **Min(a, b, c)** - zwraca najmniejszą z trzech podanych wartości

## Rozwiązanie

### Pseudokod

```
funkcja OdległośćLevenshteina(tekst1, tekst2):
    1. macierz[0..Długość(tekst1)][0..Długość[tekst2]] := macierz wypełniona zerami
    2. Dla i := 1 do Długość(tekst1), wykonuj:
        3. Dla j := 1 do Długość(tekst2), wykonuj:
            4. Jeżeli tekst1[i] == tekst2[i], to
                5. koszt := 0
            6. w przeciwnym przypadku:
                7. koszt := 1
            8. macierz[i][j] = Min(macierz[i - 1][j - 1] + koszt, macierz[i - 1][j] + 1, macierz[i][j - 1] + 1)

    9. Zwróć macierz[Długość(tekst1)][Długość(tekst2)]
```

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/text/levenshtein-distance.md" %}
[levenshtein-distance.md](../../programming/c++/algorithms/text/levenshtein-distance.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/text/levenshtein-distance.md" %}
[levenshtein-distance.md](../../programming/python/algorithms/text/levenshtein-distance.md)
{% endcontent-ref %}
