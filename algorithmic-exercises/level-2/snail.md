# Ślimak

## Opis

Ślimak znajduje się na dole studni o wysokości 6cm. W trakcie dnia ślimak może się wspiąć o 3cm do góry, ale w nocy zsuwa się o 1cm w trakcie snu. Ślimak się niestety męczy, a jego stopień zmęczenia wynosi $$10\%$$, co oznacza że każdego kolejnego dnia wspina się o $$10\%*3=0.3$$ centymetry mniej niż dnia poprzedniego. Każdego dnia odejmujemy tyle samo, tzn. $$10\%$$ wysokości wspinaczki z **pierwszego** dnia.

Której doby ślimak wydostanie się ze studni, tzn. wysokość, na której się znajdzie po wspinaczce będzie **większa** od wysokości studni? Obliczmy to na poniższej tabelce.

| Doba | Początkowa wysokość | Długość wspinaczki | Wysokość po wspinaczce | Wysokość po zsunięciu |
|:----:|:-------------------:|:------------------:|:----------------------:|:---------------------:|
|   1  |          0          |          3         |            3           |           2           |
|   2  |          2          |         2.7        |           4.7          |          3.7          |
|   3  |         3.7         |         2.4        |         **6.1**        |          ---          |

Jak widać, ślimak wydostanie się w trakcie $$3$$ doby.

Twoim zadaniem jest rozwiązanie tego zadania w ogólnym przypadku. W zależności od parametrów zadania ślimak może wydostać się ze studni albo opaść na jej dno. Musisz określić, która z tych dwóch sytuacji będzie miała miejsce i w trakcie której doby.

Źródło: [https://onlinejudge.org/external/5/573.pdf](https://onlinejudge.org/external/5/573.pdf)

### Specyfikacja

#### Dane

* $$H$$ - liczba naturalna, wysokość studni, $$1\leq H\leq 100$$.
* $$U$$ - liczba naturalna, wysokość, na którą początkowo wspina się ślimak w trakcie dnia, $$1\leq U\leq 100$$.
* $$D$$ - liczba naturalna, odległość, którą ślimak pokonuje zsuwając się w nocy, $$1\leq D\leq 100$$.
* $$F$$ - liczba naturalna, stopień zmęczenia wyrażony w procentach, $$1\leq F\leq 100$$.

**Uwaga:** ślimak nigdy nie wspina się o wartość ujemną w trakcie dnia. Może co najwyżej zmęczyć się tak bardzo, że nie będzie się już w ogóle wspinał, tylko zsuwał w nocy.

#### Wynik

* Komunikat "Ucieczka" jeżeli ślimak wyszedł ze studni, lub "Dno", jeżeli ślimak opadł na dno, oraz numer doby, w której nastąpiła dana sytuacja.

### Przykład 1

#### Dane

```
6 3 1 10
```

**Wynik:** *Ucieczka 3*

### Przykład 2

#### Dane

```
10 2 1 50
```

**Wynik:** *Dno 4*

### Przykład 3

#### Dane

```
50 5 3 14
```

**Wynik:** *Dno 7*

### Przykład 4

#### Dane

```
50 6 4 1
```

**Wynik:** *Dno 68*

### Przykład 5

#### Dane

```
50 6 3 1
```

**Wynik:** *Ucieczka 20*

### Przykład 6

#### Dane

```
1 1 1 1
```

**Wynik:** *Dno 2*
