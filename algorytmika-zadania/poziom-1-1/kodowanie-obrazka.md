# Kodowanie obrazka

## Opis

Grafika komputerowa stanowi bardzo ważny dział informatyki.
Na komputerach przechowujemy wiele zdjęć, więc ich efektywne reprezentowanie w pamięci komputera to podstawa.
W tym zadaniu rozważymy szczególny przypadek kodowania grafik.
Grafika jest przedstawiona jako prostokątna tablica drukowanych liter alfabetu angielskiego.
Każda litera koduje jeden region.
Identyczne regiony są kodowane przez takie same litery.

Twoim zadaniem jest policzyć, ile bajtów pamięci potrzeba na reprezentację tak przedstawionej grafiki w pamięci komputera.
Zasada jest prosta: najważniejszy region reprezentujemy za pomocą 2 bajtów, a wszystkie pozostałe za pomocą jednego bajta.

**Najważniejszy** region to taki, który występuje **najczęściej**, tzn. w opisie grafiki litera reprezentująca ten region występuje najwięcej razy.
Jeżeli kilka regionów ma taką samą, największą liczbę wystąpień, to wszystkie z nich uznajemy za najważniejsze.


Źródło: [https://onlinejudge.org/external/115/11588.pdf](https://onlinejudge.org/external/115/11588.pdf)

### Specyfikacja

#### Dane

* $$h, w$$ - wymiary tablicy, jej wysokość i szerokość
* $$pix[h][w]$$ - opis grafiki, tablica dwuwymiarowa o wymiarach $$h\times w$$, której każdym elementem jest wielka litera alfabetu angielskiego

#### Wynik

* Liczba bajtów potrzebna do reprezentacji podanej grafiki

### Przykład

#### Dane

```
1
5 4
ABCD
ABCA
EFAC
BCAG
AZIP
```

#### Wynik

```
26
```

{% hint style="info" %}
#### Wyjaśnienie

Najczęściej występującym regionem jest region **A**.
Występuje on dokładnie $$6$$ razy.
Oznacza to, że region **A** kodujemy za pomocą $$2$$ bajtów, a wszystkie pozostałe (których jest $$14$$), za pomocą $$1$$ bajta.
Stąd otrzymujemy wynik: $$6*2 + 14*1 = 12 + 14 = 26$$
{% endhint %}