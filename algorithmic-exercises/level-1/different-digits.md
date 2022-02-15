# Różne cyfry

## Opis

Dla zadanego przedziału określ ile liczb w tym przedziale składa się wyłącznie z różnych cyfr, tzn. w ich zapisie cyfry się nie powtarzają. Np. liczba $$123$$ składa się z różnych cyfr, natomiast liczba $$100$$ już nie, ponieważ cyfra $$0$$ się powtarza.

Źródło: [https://onlinejudge.org/external/125/12527.pdf](https://onlinejudge.org/external/125/12527.pdf)

### Specyfikacja

#### Dane

* $$a, b$$ - liczby całkowite z przedziału $$[1,5000]$$

#### Wynik

* Ilość wszystkich liczb z przedziału $$[a,b]$$, które składają się wyłącznie z różnych cyfr. 

### Przykład

#### Dane

```
a := 87
b := 104
```

#### Wynik

```
14
```

{% hint style="info" %}
#### Wyjaśnienie

Z przedziału $$[87,104]$$ następujące liczby składają się wyłącznie z różnych cyfr:

$$87,89,90,91,92,93,94,95,96,97,98,102,103,104$$ 
{% endhint %}
