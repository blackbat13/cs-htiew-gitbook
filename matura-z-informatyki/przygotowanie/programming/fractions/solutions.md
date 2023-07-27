# Rozwiązania

## Zadanie 1

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
from math import gcd


def zadanie1():
    path = "input/ulamki.txt"
    with open(path, "r") as file:
        ulamki = [list(map(int, str.split(" "))) for str in file.read().split("\n")]
        with open("skrocone.txt", "w") as out_file:
            for ulamek in ulamki:
                dzielnik = gcd(ulamek[0], ulamek[1])
                ulamek[0] //= dzielnik
                ulamek[1] //= dzielnik
                print(f"{ulamek[0]} {ulamek[1]}", file=out_file)
```
{% endcode %}

### Wynik

{% code overflow="wrap" lineNumbers="true" %}
```
1 3
15 8
21 11
16 1
9 1
9 5
3 1
3 4
10 11
23 20
3 2
10 17
5 7
3 2
22 15
1 5
24 7
25 8
12 1
7 3
5 2
1 16
1 1
6 1
7 10
13 5
3 11
19 2
15 8
1 1
1 17
7 11
27 11
1 16
13 5
6 1
15 13
1 7
1 1
2 1
7 20
25 1
5 3
18 11
8 1
7 1
18 1
21 19
10 11
6 1
6 5
29 9
1 3
7 18
7 4
9 8
1 1
28 3
3 10
1 1
11 4
26 1
2 3
2 3
28 13
3 7
13 10
5 16
26 5
19 3
5 3
25 13
8 3
10 1
25 11
3 7
27 1
2 9
3 4
9 10
13 1
11 8
26 19
5 7
13 10
7 18
2 1
1 1
29 17
17 20
19 7
14 9
7 1
14 1
3 5
23 19
2 1
1 20
9 7
4 3
```
{% endcode %}

## Zadanie 2

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
from math import gcd


def zadanie2():
    path = "input/ulamki.txt"
    with open(path, "r") as file:
        ulamki = [list(map(int, str.split(" "))) for str in file.read().split("\n")]
        licznik = ulamki[0][0]
        mianownik = ulamki[0][1]
        ulamki.pop(0)
        for ulamek in ulamki:
            m1 = mianownik
            m2 = ulamek[1]
            licznik *= m2
            mianownik *= m2
            ulamek[0] *= m1
            ulamek[1] *= m1
            licznik += ulamek[0]

        dzielnik = gcd(licznik, mianownik)
        licznik //= dzielnik
        mianownik //= dzielnik
        print(licznik, mianownik)
```
{% endcode %}

### Wynik

```
Suma: 7271917729 21162960
```

## Zadanie 3

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
from math import gcd


def zadanie3():
    path = "input/ulamki.txt"
    with open(path, "r") as file:
        ulamki = [list(map(int, str.split(" "))) for str in file.read().split("\n")]
        licznik = ulamki[0][0]
        mianownik = ulamki[0][1]
        ulamki.pop(0)
        for ulamek in ulamki:
            licznik *= ulamek[0]
            mianownik *= ulamek[1]

        dzielnik = gcd(licznik, mianownik)
        licznik //= dzielnik
        mianownik //= dzielnik
        print(licznik, mianownik)
```
{% endcode %}

### Wynik

```
Iloczyn: 98818570351733115048023210625 95321577472
```
