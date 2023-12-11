# Liczby całkowite

W pliku **integers.txt** znajduje się $$100$$ **różnych** liczb naturalnych z zakresu $$[2,200]$$. Każda linia w pliku zawiera jedną liczbę.

{% file src="../../../../.gitbook/assets/integers/integers.txt" %}
integers.txt
{% endfile %}

W pliku *integers_test.txt* znajduje się $$10$$ **różnych** liczb całkowitych. Każda linia w pliku zawiera jedną liczbę.

{% file src="../../../../.gitbook/assets/integers/integers_test.txt" %}
integers_test.txt
{% endfile %}

Napisz program/programy rozwiązujące poniższe zadania.

## Zadanie 1

Podaj najmniejszą i największą wartość z pliku, oraz ich pozycję (numer wiersza) w pliku.

Wynik dla pliku *integers_test.txt*:

```
Minimum: 6 Pozycja: 1
Maksimum: 29 Pozycja: 10
```

## Zadanie 2

Podaj sumę i średnią (z zaokrągleniem do dwóch miejsc po przecinku) wszystkich wartości z pliku.

Wynik dla pliku *integers_test.txt*:

```
Suma: 190
Średnia: 19.00
```

## Zadanie 3

Podaj ile jest w pliku wartości parzystych. 

Wynik dla pliku *integers_test.txt*:

```
4
```

## Zadanie 4

Podaj najmniejszą i największą wartość **parzystą** z pliku.

Wynik dla pliku *integers_test.txt*:

```
Minimum parzyste: 6
Maksimum parzyste: 28
```

## Zadanie 5

Podaj ile jest liczb z pliku, które są wielokrotnością jednocześnie liczb 3 i 5.

Wynik dla pliku *integers_test.txt*:

```
1
```

## Zadanie 6

Dla każdej pary sąsiednich wartości policz ich największy wspólny dzielnik. Podaj największą i najmniejszą wartość takiego dzielnika.

Wynik dla pliku *integers_test.txt*:

```
Maksimum NWD: 3
Minimum NWD: 1
```

## Zadanie 7

Policz najmniejszą wspólną wielokrotność dla wszystkich liczb w pliku mniejszych od 20.

Wynik dla pliku *integers_test.txt*:

```
NWW: 360
```

## Zadanie 8

Sprawdź, ile liczb w pliku jest liczbami pierwszymi.

Wynik dla pliku *integers_test.txt*:

```
2
```

## Zadanie 9

Dla każdej liczby z pliku wyznacz sumę jej cyfr. Znajdź liczbę o największej sumie cyfr oraz liczbę o najmniejszej sumie cyfr. Podaj te liczby oraz ich sumę cyfr.

Wynik dla pliku *integers_test.txt*:

```
Minimalna suma cyfr: 3 Liczba: 21
Maksymalna suma cyfr: 11 Liczba: 29
```

## Zadanie 10

Znajdź **wszystkie** pary liczb w pliku, które są względem siebie liczbami wzajemnie pierwszymi (tzn. ich największy wspólny dzielnik to 1). Jako wynik podaj pary o najmniejszej i największej sumie.

Wynik dla pliku *integers_test.txt*:

```
Para o największej sumie: (28, 29)
Para o najmniejszej sumie: (8, 9)
```

## Zadanie 11

Dla każdej liczby z pliku sprawdź, czy jest ona doskonała (tzn. czy jest równa sumie swoich dzielników właściwych, tj. wszystkich dzielników oprócz siebie samej). Podaj wszystkie liczby doskonałe z pliku.

Wynik dla pliku *integers_test.txt*:

```
6
28
```

## Zadanie 12

Podaj medianę wartości z pliku (wartość środkową w uporządkowanej rosnąco liście wszystkich liczb).

Wynik dla pliku *integers_test.txt*:

```
22
```

## Zadanie 13

Znajdź liczbę, która pojawia się najczęściej w pliku i podaj liczbę jej wystąpień. Jeżeli jest kilka takich liczb, podaj najmniejszą z nich.

Wynik dla pliku *integers_test.txt*:

```
Najpopularniejsza liczba: 6
Liczba wystąpień: 1
```

## Zadanie 14

Policz, ile jest liczb w pliku, które są potęgą liczby 2.

Wynik dla pliku *integers_test.txt*:

```
1
```

## Zadanie 15

Dla każdej liczby z pliku wyznacz jej reprezentację binarną (w postaci ciągu zer i jedynek). Podaj, ile liczb w swojej reprezentacji binarnej ma: 

- więcej zer niż jedynek,
- mniej zer niż jedynek,
- tyle samo zer co jedynek.

Wynik dla pliku *integers_test.txt*:

```
Więcej zer: 2
Mniej zer: 7
Tyle samo: 1
```

## Zadanie 16

Podaj wszystkie liczby z pliku, które są iloczynem **dwóch** liczb pierwszych.

Wynik dla pliku *integers_test.txt*:

```
4
```

## Zadanie 17

Podaj ile liczb z pliku jest **silnią** jakiejś liczby naturalnej.

Wynik dla pliku *integers_test.txt*:

```
2
```

## Zadanie 18

Podaj ile liczb z pliku jest **kwadratem** jakiejś liczby naturalnej.

Wynik dla pliku *integers_test.txt*:

```
9
```
