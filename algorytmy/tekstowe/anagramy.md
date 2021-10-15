# Anagramy

## Opis problemu

TODO

{% hint style="info" %}
Dwa wyrazy nazywamy **anagramami**, jeżeli składają się dokładnie z takich samych znaków, ale ułożonych w innej kolejności.
{% endhint %}

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna, długość tekstu.
* $$tekst1[1..n]$$ - ciąg znaków o długości $$n$$, numerowanych od jedynki, składający się wyłącznie z małych liter alfabetu angielskiego.
* $$tekst2[1..n]$$ - ciąg znaków o długości $$n$$, numerowanych od jedynki, składający się wyłącznie z małych liter alfabetu angielskiego.

#### Wynik

* $$True$$ - jeżeli $$tekst1$$ i $$tekst2$$ są anagramami.
* $$False$$ - w przeciwnym przypadku.

### Przykład

#### Dane

```
n := 8
tekst1 := "markotny"
tekst2 := "romantyk"
```

**Wynik**: $$True$$ 

## Rozwiązanie 1

Aby dwa wyrazy były anagramami, muszą składać się dokładnie z takich samych liter. Oznacza to także, że każda litera musi występować w każdym z wyrazów dokładnie tyle samo razy. W związku z tym pierwsze rozwiązanie jest proste: policzmy, ile razy każda litera występuje w pierwszym wyrazie, następnie zróbmy to samo dla drugiego wyrazu i porównajmy wyniki. Jeżeli będą takie same, to dwa wyrazy są anagramami.

Jak jednak policzyć, ile razy dana litera występuje w wyrazie? Zauważmy, że nasze wyrazy składają się jedynie z małych liter alfabetu angielskiego. Oznacza to, że mamy dokładnie 26 znaków. Możemy więc przygotować tablicę przechowującą 26 liczników - po jednym dla każdej litery. Litery natomiast ponumerujemy od 1, startując od a. Ilość wystąpień litery a zapiszemy w pierwszym liczniku, ilość wystąpień litery b zapiszemy w drugim liczniku itd.

### Pseudokod

```
funkcja TestujAnagramy(n, tekst1, tekst2):
    1. liczniki1 := tablica [1..26] wypełniona wartościami 0
    2. liczniki2 := tablica [1..26] wypełniona wartościami 0
    3. Od i := 1 do n, wykonuj:
        4. indeks1 := numer znaku tekst1[i]
        5. liczniki1[indeks] := liczniki1[indeks] + 1
        6. indeks2 := numer znaku tekst2[i]
        7. liczniki2[indeks] := liczniki2[indeks] + 1
    8. Jeżeli liczniki1 = liczniki2, to:
        9. Zwróć True
    10. w przeciwnym przypadku:
        11. Zwróć False
```

### Złożoność

$$O(n)$$ - liniowa

## Rozwiązanie 2

Innym rozwiązaniem jest posortowanie obu wyrazów i porównanie ich.

### Pseudokod

```
funkcja TestujAnagramy(n, tekst1, tekst2):
    1. Sortuj(tekst1)
    2. Sortuj(tekst2)
    3. Jeżeli tekst1 = tekst2, to:
        4. Zwróć True
    5. w przeciwnym przypadku:
        6. Zwróć False 
```

### Złożoność

$$O(n)$$ - liniowa, jeżeli wykorzystamy optymalny algorytm sortowania (np. sortowanie przez zliczanie).

$$O(n\log{n})$$ - liniowo logarytmiczna, jeżeli użyjemy standardowej metody sortowania (np. sortowanie szybkie). 

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/tekstowe/anagramy.md" %}
[anagramy.md](../../programowanie/c++/algorytmy/tekstowe/anagramy.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/tekstowe/anagramy.md" %}
[anagramy.md](../../programowanie/python/algorytmy/tekstowe/anagramy.md)
{% endcontent-ref %}

