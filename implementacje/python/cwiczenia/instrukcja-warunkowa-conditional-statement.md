# Instrukcja warunkowa (conditional statement)

{% tabs %}
{% tab title="PL" %}
## Zadanie 1

Napisz program zgodny z poniższą specyfikacją. Nie korzystaj z funkcji **abs, fabs**

### Specyfikacja

#### Dane

* $$a$$ - liczba całkowita

#### Wynik

* Wartość bezwzględna z $$a$$

### Przykład

#### Dane

```
a := -2
```

**Wynik**: $$2$$ 

## Zadanie 2

Napisz program zgodny z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$a$$ - liczba całkowita

#### Wynik

* Znak liczby $$a$$, tzn. $$1$$ gdy $$a$$ jest dodatnie, $$-1$$ gdy $$a$$ jest ujemne, $$0$$ gdy $$a$$ wynosi $$0$$ 

### Przykład 1

#### Dane

```
a := 5
```

**Wynik**: $$1$$ 

### Przykład 2

#### Dane

```
a := -5
```

**Wynik**: $$-1$$ 

### Przykład 3

#### Dane

```
a := 0
```

**Wynik**: $$0$$ 

## Zadanie 3

Napisz program zgodny z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$a, b$$ - dwie liczby całkowite

#### Wynik

* Wynik dzielenia liczb $$a$$ i $$b$$, lub komunikat, że nie można wykonać dzielenia.

### Przykład

#### Dane

```
a := 1
b := 2
```

**Wynik**: $$0.5$$ 

## Zadanie 4

Napisz program zgodny z poniższą specyfikacją. Nie korzystaj z funkcji **min, max**.

### Specyfikacja

#### Dane

* $$a, b, c$$ - trzy liczby całkowite

#### Wynik

* Największa z liczb $$a$$, $$b$$ i $$c$$ , lub dowolna gdy są sobie równe

### Przykład

#### Dane

```
a := 4
b := 1
c := 3
```

**Wynik**: $$4$$ 

## Zadanie 5

Napisz program zgodny z poniższą specyfikacją. Nie korzystaj z funkcji **min, max**.

### Specyfikacja

#### Dane

* $$a, b, c, d$$ - cztery liczby całkowite

#### Wynik

* Największa z liczb $$a, b, c$$ i $$d$$, lub dowolna gdy są sobie równe

### Przykład

#### Dane

```
a := 3
b := 1
c := 3
d := 5
```

**Wynik**: $$5$$ 

## Zadanie 6

Napisz program zgodny z poniższą specyfikacją. Zadbaj o czytelność programu.

### Specyfikacja

#### Dane

* $$a, b$$ - dwie liczby całkowite
* $$op$$ - znak jednej z dozwolonych operacji: $$+,-,*,/$$ 

#### Wynik

* Wynik działania$$a\ op\ b$$ (np. $$a+b$$), lub komunikat, że nie można wykonać dzielenia.

### Przykład

#### Dane

```
a := 3
b := 1
op := '+'
```

**Wynik**: $$4$$ 

## Zadanie 7

Napisz program zgodny z poniższą specyfikacją.

{% hint style="info" %}
**Rok przestępny** to taki, który:

* jest podzielny przez 4, ale nie jest podzielny przez 100, lub
* jest podzielny przez 400
{% endhint %}

### Specyfikacja

#### Dane

* $$rok$$ - liczba naturalna

#### Wynik

* Komunikat określający, czy podany rok jest przestępny czy też nie

### Przykład

#### Dane

```
rok := 2021
```

**Wynik**:  "Rok 2021 nie jest przestępny"
{% endtab %}

{% tab title="EN" %}
## Exercise 1

Write a program that complies with the specification below. Don't use **abs** function.

### Specification

#### Input

* $$a$$ - integer

#### Output

* The absolute value of $$a$$

### Example

#### Input

```
a := -2
```

**Output**: $$2$$ 

## Exercise 2

Write a program that complies with the specification below.

### Specification

#### Input

* $$a$$ - integer

#### Output

* The sign of the number $$a$$, i.e. $$1$$ when $$a$$ is positive, $$-1$$ when $$a$$ is negative, $$0$$ when $$a$$ is equal to $$0$$ 

### Example 1

#### Input

```
a := 5
```

**Output**: $$1$$ 

### Example 2

#### Input

```
a := -5
```

**Output**: $$-1$$ 

### Example 3

#### Input

```
a := 0
```

**Output**: $$0$$ 

## Exercise 3

Write a program that complies with the specification below.

### Specification

#### Input

* $$a, b$$ - two integers

#### Output

* The result of dividing numbers $$a$$ and $$b$$, or a message that division could not be performed.

### Example

#### Input

```
a := 1
b := 2
```

**Output**: $$0.5$$ 

## Exercise 4

Write a program that complies with the specification below. Don't use **min **and** max **functions.

### Specification

#### Input

* $$a, b, c$$ - three integers

#### Output

* The largest of the numbers $$a$$, $$b$$ and $$c$$, or any when they are equal.

### Example

#### Input

```
a := 4
b := 1
c := 3
```

**Output**: $$4$$ 

## Exercise 5

Write a program that complies with the specification below. Nie korzystaj z funkcji **min, max**.

### Specification

#### Input

* $$a, b, c, d$$ - four integers

#### Output

* The largest of the numbers $$a, b, c$$ and $$d$$, or any when they are equal.

### Example

#### Input

```
a := 3
b := 1
c := 3
d := 5
```

**Output**: $$5$$ 

## Exercise 6

Write a program that complies with the specification below. Zadbaj o czytelność programu.

### Specification

#### Input

* $$a, b$$ - two integers
* $$op$$ - sign of one of the allowed operations: $$+,-,*,/$$ 

#### Output

* Result of an operation $$a\ op\ b$$ (e.g. $$a+b$$), or a message that division could not be performed.

### Example

#### Input

```
a := 3
b := 1
op := '+'
```

**Output**: $$4$$ 

## Exercise 7

Write a program that complies with the specification below.

{% hint style="info" %}
A **leap year** is one that:

* is divisible by 4 but not divisible by 100, or
* is divisible by 400
{% endhint %}

### Specification

#### Input

* $$year$$ - natural number

#### Output

* A message stating whether the given year is a leap year or not

### Example

#### Input

```
year := 2021
```

**Output**:  "2021 is not a leap year"
{% endtab %}
{% endtabs %}
