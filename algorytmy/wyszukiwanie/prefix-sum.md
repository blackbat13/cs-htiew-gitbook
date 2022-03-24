# Sumy prefiksowe

## Opis problemu



### Specyfikacja

#### Dane

* $$n$$ — liczba naturalna, liczebność zbioru
* $$A[1..n]$$ — $$n-elementowa$$ tablica liczb całkowitych, indeksowana od jedynki
* $$m$$ — liczba naturalna, liczba zapytań
* $$(p_1, k_1), (p_2, k_2), ..., (p_m, k_m)$$ — $$m$$ par liczb naturalnych z zakresu $$[1..n]$$, zapytań o sumy przedziałów

#### Wynik

* $$sum_1, sum_2, ..., sum_m$$ — $$k$$ liczb naturalnych, dla każdego zapytania $$(p_i, k_i)$$ suma wartości pod indeksami od $$p_i$$ do $$k_i$$, tzn. $$sum_i = A[p_i] + A[p_i + 1] + A[p_i + 2] + ... + A[k_i]$$.

### Przykład

#### Dane

```
n := 10
A[1..10] := [4, 8, 2, 6, 1, 0, 8, 4, 2, 3]
m := 3

p_1 := 3
k_1 := 5

p_2 := 6
k_2 := 7

p_3 := 1
k_3 := 1
```

#### Wynik

```
sum_1 = 9
sum_2 = 8
sum_3 = 4
```

{% hint style="info" %}
**Wyjaśnienie**

$$sum_1 = A[3] + A[4] + A[5] = 2 + 6 + 1 = 9$$
$$sum_2 = A[6] + A[7] = 0 + 8 = 8$$
$$sum_3 = A[1] = 4$$
{% endhint %}