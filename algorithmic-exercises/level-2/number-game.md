# Gra w liczby

## Opis

Wyobraź sobie prostą grę dla dzieci: dane jest kilka liczb napisanych na osobnych kartach, a celem jest takie ułożenie kart jedna obok drugiej, by powstała jak największa liczba.

Dla przykładu weźmy trzy liczby: $$90$$, $$101$$ i $$3$$.
Możemy je połączyć na kilka sposobów, w ten sposób tworząc nowe liczby: $$901013$$, $$903101$$, $$101903$$, $$101390$$, $$310190$$ and $$390101$$.
Jak możemy zauważyć mamy $$6$$ kombinacji. Największa liczba, którą możemy w ten sposób uzyskać to $$903101$$. Twoim celem jest znalezienie takiej największej liczby i wygranie gry!.


Źródło: [https://onlinejudge.org/external/109/10905.pdf](https://onlinejudge.org/external/109/10905.pdf)

### Specyfikacja

#### Wejście

* $$n$$ - liczba naturalna
* $$a_1, a_2, ..., a_n$$ - $$n$$ liczb naturalnych

#### Wyjście

* Największa liczba jaka może zostać utworzona poprzez połączenie ze sobą liczb $$a_1, a_2, ..., a_n$$ w wybranym porządku.

### Przykład 1

#### Wejście

```
4
123 124 56 90
```

#### Wyjście

```
9056124123
```

### Przykład 2

#### Wejście

```
5
123 124 56 90 9 
```

#### Wyjście

```
99056124123
```