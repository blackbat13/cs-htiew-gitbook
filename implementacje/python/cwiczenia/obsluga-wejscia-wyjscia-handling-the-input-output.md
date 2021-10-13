# Obsługa wejścia/wyjścia (Handling the input/output)

{% tabs %}
{% tab title="PL" %}
## Zadanie 1

Napisz program zgodny z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$imie$$ - ciąg znaków, małych i wielkich liter alfabetu angielskiego

#### Wynik

* Komunikat powitania w formie "_Witaj \[**imie**]!_"

### Przykład

#### Dane

```
imie := "Damian"
```

**Wynik**: "Witaj Damian!"

## Zadanie 2

Napisz program zgodny z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$a, b$$ - dwie liczby całkowite

#### Wynik

* Suma liczb $$a$$ i $$b$$ 

### Przykład

#### Dane

```
a := 2
b := 3
```

**Wynik**: $$5$$ 

## Zadanie 3

Napisz program zgodny z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$a, b$$ - dwie liczby całkowite, różne od zera

#### Wynik

* Wynik dzielenia liczb $$a$$ i $$b$$ 

### Przykład

#### Dane

```
a := 1
b := 2
```

**Wynik**: $$0.5$$ 

## Zadanie 4

Napisz program zgodny z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$a, b$$ - dwie liczby naturalne, większe od zera

#### Wynik

* Wynik dzielenia całkowitego oraz reszta z dzielenia liczb $$a$$ i $$b$$ 

### Przykład

#### Dane

```
a := 7
b := 3
```

**Wynik**: $$2$$, reszty $$1$$ 

## Zadanie 5

Napisz program zgodny z poniższą specyfikacją.

{% hint style="info" %}
**Podpowiedź**

Skorzystaj z funkcji **`sqrt`** z biblioteki **`cmath`**.
{% endhint %}

### Specyfikacja

#### Dane

* $$a$$ - liczba naturalna

#### Wynik

* Pierwiastek z $$a$$

### Przykład

#### Dane

```
a := 4
```

**Wynik**: $$2$$ 

## Zadanie 6

Napisz program zgodny z poniższą specyfikacją. Wykorzystaj funkcję **min**.

### Specyfikacja

#### Dane

* $$a, b$$ - dwie liczby całkowite

#### Wynik

* Mniejsza z liczb $$a$$ i $$b$$, lub dowolna gdy są sobie równe

### Przykład

#### Dane

```
a := 5
b := 3
```

**Wynik**: $$3$$ 

## Zadanie 7

Napisz program zgodny z poniższą specyfikacją. Wykorzystaj funkcję **max**.

### Specyfikacja

#### Dane

* $$a, b, c$$ - trzy liczby całkowite

#### Wynik

* Największa z liczb $$a$$, $$b$$ i $$c$$ , lub dowolna gdy są sobie równe

### Przykład

#### Dane

```
a := 3
b := 1
c := 3
```

**Wynik**: $$3$$ 

## Zadanie 8

Napisz program zgodny z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$sekundy$$ - liczba naturalna

#### Wynik

* Czas podany w czytelnej formie ** **$$H:M:S$$ ($$H$$ - godziny, $$M$$ - minuty, $$S$$ - sekundy)

### Przykład

#### Dane

```
sekundy := 9179
```

**Wynik**: $$2:32:59$$ 

{% hint style="info" %}
**Wyjaśnienie**

$$2H=7200S$$ 

$$32M=1920S$$ 

$$2H+32M+59S=7200S+1920S+59S=9179S$$ 
{% endhint %}
{% endtab %}

{% tab title="EN" %}
## Exercise 1

Write a program that complies with the specification below.

### Specification

#### Input

* $$name$$ - string of characters, upper and lower case letters of the English alphabet

#### Output

* A greeting message in the form of "**Hello \[name]!**"

### Example

#### Input

```
name := "Damian"
```

**Output**: "Hello Damian!"

## Exercise 2

Write a program that complies with the specification below

### Specification

#### Input

* $$a, b$$ - two integers

#### Output

* Sum of $$a$$ and $$b$$ 

### Example

#### Input

```
a := 2
b := 3
```

**Output**: $$5$$ 

## Exercise 3

Write a program that complies with the specification below

### Specification

#### Input

* $$a, b$$ - two non-zero integers

#### Output

* The result of dividing numbers $$a$$ and $$b$$ 

### Example

#### Input

```
a := 1
b := 2
```

**Output**: $$0.5$$ 

## Exercise 4

Write a program that complies with the specification below

### Specification

#### Input

* $$a, b$$ - two integers, greater than zero

#### Output

* The result of an integer division and the remainder of the division of numbers $$a$$ and $$b$$ 

### Example

#### Input

```
a := 7
b := 3
```

**Output**: $$2$$, remainder$$1$$ 

## Exercise 5

Write a program that complies with the specification belowWrite a program that complies with the specification below

{% hint style="info" %}
**Hint**

Use the **sqrt** function from the **math** library.
{% endhint %}

### Specification

#### Input

* $$a$$ - natural number

#### Output

* The root of $$a$$

### Example

#### Input

```
a := 4
```

**Output**: $$2$$ 

## Exercise 6

Write a program that complies with the specification below. Use the **min **function.

### Specification

#### Input

* $$a, b$$ - two integers

#### Output

* The smaller of the numbers $$a$$ and $$b$$, or any number, when they are equal to each other

### Example

#### Input

```
a := 5
b := 3
```

**Output**: $$3$$ 

## Exercise 7

Write a program that complies with the specification below. Use the **max **function.

### Specification

#### Dane

* $$a, b, c$$ - three integers

#### Wynik

* The largest of the numbers $$a$$, $$b$$ and $$c$$, or any when they are equal

### Example

#### Input

```
a := 3
b := 1
c := 3
```

**Output**: $$3$$ 

## Example 8

Write a program that complies with the specification below.

### Specification

#### Input

* $$seconds$$ - natural number

#### Output

* Time given in a legible form $$H:M:S$$ ($$H$$ - hours, $$M$$ - minutes, $$S$$ - seconds)

### Example

#### Input

```
seconds := 9179
```

**Output**: $$2:32:59$$ 

{% hint style="info" %}
**Explanation**

$$2H=7200S$$ 

$$32M=1920S$$ 

$$2H+32M+59S=7200S+1920S+59S=9179S$$ 
{% endhint %}
{% endtab %}
{% endtabs %}
