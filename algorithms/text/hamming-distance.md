# Odległość Hamminga

## Opis problemu

Odległość Hamminga to nic innego jak liczba pozycji, na których dwa teksty się między sobą różnią.

### Specyfikacja

#### Dane

- **tekst1**, **tekst2** - dwa teksty, ciągi znaków liter angielskiego, o tej samej długości

#### Wynik

- Odległość Hamminga pomiędzy **tekst1** a **tekst2**.

### Funkcje pomocnicze

- **Długość(tekst)** - zwraca długość tekstu

## Rozwiązanie

### Pseudokod

```
funkcja OdległośćHamminga(tekst1, tekst2):
    1. wynik := 0
    2. Dla i := 1 do Długość(tekst1), wykonuj:
        3. Jeżeli tekst1[i] != tekst2[i], to:
            4. wynik := wynik + 1
    5. Zwróć wynik
```

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/text/hamming-distance.md" %}
[hamming-distance.md](../../programming/c++/algorithms/text/hamming-distance.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/text/hamming-distance.md" %}
[hamming-distance.md](../../programming/python/algorithms/text/hamming-distance.md)
{% endcontent-ref %}
