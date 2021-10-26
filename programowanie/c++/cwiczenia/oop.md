# Programowanie obiektowe

## Zadanie 1

Napisz program zgodny z poniższą specyfikacją. Do reprezentacji ułamków i wykonywania na nich operacji wykorzystaj własną implementację klasy.

### Specyfikacja

#### Dane

* $$l1, m1$$ - licznik i mianownik pierwszego ułamka, liczby całkowite
* $$op$$ - znak operacji: $$+$$, $$-$$, $$*$$ lub $$/$$
* $$l2, m2$$ - licznik i mianownik drugiego ułamka, liczby całkowite

#### Wynik

* Wynik działania operacji $$\frac{l1}{m2}\ op\ \frac{l2}{m2}$$ przedstawiony w formie ułamka zwyczajnego (maksymalnie skróconego), wypisany w formacie `licznik / mianownik`, np. `3 / 4`

### Przykład 1

#### Dane

```
l1 := 5
m1 := 8
op := '+'
l2 := 5
m2 := 8
```

#### Wynik

```
5 / 4
```

### Przykład 2

#### Dane

```
l1 := -1
m1 := 2
op := '*'
l2 := 2
m2 := 4
```

#### Wynik

```
-1 / 4
```
