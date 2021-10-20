---
description: Sprawdzanie, czy wyraz jest palindromem
---

# Palindrom

## Opis problemu

TODO

{% hint style="info" %}
**Palindrom **to wyraz, który czytany od lewej do prawej i od prawej do lewej jest taki sam.
{% endhint %}

### Specyfikacja

#### Dane:

* $$n$$ - długość tekstu
* $$tekst[1..n]$$ - ciąg znaków o długości $$n$$, numerowanych od jedynki&#x20;

#### Wynik:

* $$True$$ - jeżeli $$tekst$$ jest palindromem
* $$False$$ - w przeciwnym przypadku

### Przykład 1

#### Dane

```
n := 5
tekst := "kajak"
```

#### Wynik: $$True$$&#x20;

{% hint style="info" %}
**Wyjaśnienie**

Wyraz **kajak** czytany od tyłu to **kajak**, jest on więc palindromem.
{% endhint %}

### Przykład 2

#### Dane

```
n := 4
tekst := "tama"
```

**Wynik**: $$False$$&#x20;

{% hint style="info" %}
**Wyjaśnienie**

Wyraz **tama** czytany od tyłu to **amat**, nie jest on więc palindromem.
{% endhint %}

## Rozwiązanie

TODO

### Pseudokod

```
funkcja czyPalindrom(n, tekst):
    1. srodek := n div 2
    2. Od i := 1 do srodek, wykonuj:
        3. Jeżeli tekst[i] != tekst[n-i+1], to:
            4. Zwróć False, zakończ
    5. Zwróć True, zakończ
```

### Złożoność

$$O(n/2)\to O(n)$$ - liniowa&#x20;

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/tekstowe/palindrom.md" %}
[palindrom.md](../../programowanie/c++/algorytmy/tekstowe/palindrom.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/tekstowe/palindrom.md" %}
[palindrom.md](../../programowanie/python/algorytmy/tekstowe/palindrom.md)
{% endcontent-ref %}

