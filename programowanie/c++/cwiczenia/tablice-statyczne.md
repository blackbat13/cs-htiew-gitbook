# Tablice statyczne

## Zadanie 1

Napisz program zgodny z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna
* $$a_1,a_2,\dots,a_n$$ - $$n$$ liczb całkowitych

#### Wynik

* $$a_n,a_{n-1},\dots,a_2,a_1$$ - podane liczby w odwrotnej kolejności

## Zadanie 2

Napisz program zgodny z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna
* $$t1[n],\ t2[n]$$ - dwie tablice liczb całkowitych

#### Wynik

* Tablica powstała poprzez dodanie do siebie wartości z tablic $$t1$$ i $$t2$$ 

### Przykład

#### Dane

```
n := 5
t1 := [4, 1, 7, 0, 2]
t2 := [2, 3, 1, 9, 6]
```

**Wynik**: $$[6, 4, 8, 9, 8]$$ 

{% hint style="info" %}
**Wyjaśnienie**

$$[4+2,\ 1+3,\ 7+1,\ 0+9,\ 2+6]$$ 
{% endhint %}

## Zadanie 2

Napisz program zgodny z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna

#### Wynik

* $$fib[n]$$ - tablica zawierająca $$n$$ kolejnych liczb Fibonacciego

### Przykład

#### Dane

```
n := 6
```

**Wynik**: $$[1,1,2,3,5,8]$$ 

## Zadanie 3

Napisz program zgodny z poniższą specyfikacją.

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna

#### Wynik

* $$mno[n][n]$$ - dwuwymiarowa tablica reprezentująca tabliczkę mnożenia liczb z zakresu $$[0,n-1]$$, gdzie $$mno[i][j]=i*j$$

### Przykład

#### Dane

```
n := 3
```

#### Wynik

```
mno := [[0, 0, 0],
        [0, 1, 2],
        [0, 2, 4]]
```
