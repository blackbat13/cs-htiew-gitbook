# Gazeta

## Opis

Gazeta Bitek w Bajtkowie cieszy się dużą popularnością, nawet w swojej oryginalnej, papierowej wersji.
Co za tym idzie wiele osób wysyła do redakcji swoje ogłoszenia do umieszczenia w kolejnym wydaniu.
Do tej pory stawka była jasna: stała kwota za każde ogłoszenie, w zależności od liczby znaków.
Wydawca gazety Bitek zauważył jednak, że różne znaki zużywają inne ilości tuszu, co oznacza, że koszt ich druku także się różni!
Postanowił więc zaktualizować cennik i określić koszt każdego znaku. Teraz opłata za wiadomość jest równa sumie kosztów każdego znaku z tej wiadomości.

Twoim zadaniem jest policzyć, ile będzie wynosić opłata za dany wyraz wedle nowego cennika.


Źródło: [https://onlinejudge.org/external/113/11340.pdf](https://onlinejudge.org/external/113/11340.pdf)

### Specyfikacja

#### Dane

* $$n$$ - liczba znaków
* $$(z_1, c_1), (z_2, c_2), ..., (z_n, c_n)$$ - cennik: pary znak oraz cena znaku, podana w groszach
* $$wyraz$$ - ciąg znaków, bez spacji i innych białych znaków

#### Wynik

* Opłata za $$wyraz$$, podana w złotówkach, wedle nowego cennika. Zakładamy, że każdy znak z wyrazu pojawi się w cenniku.

### Przykład

#### Dane

```
5
a 5
l 25
m 30
k 50
o 10
t 1
alamakota
```

#### Wynik

```
1.36
```

{% hint style="info" %}
#### Wyjaśnienie

W wyrazie **alamakota** możemy wyróżnić:

* $$4$$ litery **a**
* $$1$$ literę **l**
* $$1$$ literę **m**
* $$1$$ literę **k**
* $$1$$ literę **o**
* $$1$$ literę **t**

Daje nam to:
$$4*5+1*25+1*30+1*50+1*10+1*1=136$$ groszy, czyli $$1.36$$ złoty.
{% endhint %}