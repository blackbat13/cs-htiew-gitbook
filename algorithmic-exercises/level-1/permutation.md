# Permutacja

## Opis

Tablice w programowaniu to podstawa. Posortowane tablice to także podstawa. A czymże jest posortowana tablica, jak nie pewną **permutacją** tablicy początkowej?

Permutację tablicy można opisać podając docelową kolejność poszczególnych elementów tablicy, a także ich początkowy układ.
Twoje zadanie polega na wypisaniu permutowanej tablicy na podstawie takiego właśnie opisu.


Źródło: [https://onlinejudge.org/external/4/482.pdf](https://onlinejudge.org/external/4/482.pdf)

### Specyfikacja

#### Dane

* $$n$$ - liczba elementów tablicy
* $$p_1,p_2,...,p_n$$ - opis permutacji: docelowa kolejność elementów, unikalne (bez powtórzeń) liczby całkowite z przedziału $$[1,n]$$
* $$a_1,a_2,...,a_n$$ - wartości tablicy w jej początkowym ułożeniu, liczby całkowite

#### Wynik

* Zadana permutacja tablicy, tzn. taka, że element $$a_i$$ znajduje się na pozycji $$p_i$$.

### Przykład

#### Dane

```
5
3 5 2 1 4
20 41 84 93 12
```

#### Wynik

```
93 84 20 12 41  
```

{% hint style="info" %}
#### Wyjaśnienie

Opis permutacji określa nam docelową pozycję elementów:

* $$20$$ na miejscu $$3$$
* $$41$$ na miejscu $$5$$
* $$84$$ na miejscu $$2$$
* $$93$$ na miejscu $$1$$
* $$12$$ na miejscu $$4$$
{% endhint %}