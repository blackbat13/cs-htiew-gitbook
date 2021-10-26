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

## Zadanie 2

Napisz program zgodny z poniższą specyfikacją. Do reprezentacji liczb i wykonywania na nich operacji wykorzystaj własną implementację klasy.
Możesz założyć, że wartości wszystkich liczb w systemie dziesiętnym zmieszczą się w typie `int`.

### Specyfikacja

#### Dane

* $$l1, p1$$ - liczba $$l1$$ reprezentowana w podstawie $$p1$$, $$2 \leq p1 \leq 16$$
* $$l2, p2$$ - liczba $$l2$$ reprezentowana w podstawie $$p2$$, $$2 \leq p2 \leq 16$$
* $$p3$$ - docelowa podstawa, $$2 \leq p3 \leq 16$$

#### Wynik

* Suma podanych wartości przedstawiona w podstawie $$p3$$

### Przykład

#### Dane

```
l1 := 1010
p1 := 2
l2 := 5
p2 := 10
p3 := 8
```

#### Wynik

```
17
```

{% hint style="info" %}
**Wyjaśnienie**

$$1010_2+5_{10}=17_8$$
{% endhint %}