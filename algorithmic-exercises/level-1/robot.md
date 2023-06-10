# Kłódka

Masz robota, który może poruszać się wyłącznie w lewo i prawo na osi *x*. Początkowo robot znajduje się na pozycji $$0$$ i może wykonać następujące instrukcje:

* LEWO - porusz się o jedną jednostkę w lewo,
* PRAWO - porusz się o jedną jednostkę w prawo,
* JAK W $$i$$ - porusz się tak samo jak w $$i$$-tej instrukcji. $$i$$ zawsze będzie liczbą naturalną nie większą niż numer instrukcji, w której występuje. Instrukcje liczymy od jedynki. 

Zastanawiasz się, czy Twój robot działa poprawnie. Napisz program, który dla podanego zestawu instrukcji wypisze pozycję, na której znajdzie się robot.

Źródło: [https://onlinejudge.org/external/125/12503.pdf](https://onlinejudge.org/external/125/12503.pdf)

## Specyfikacja

### Dane

* $$n$$ - liczba naturalna, liczba instrukcji do wykonania, $$1\leq p\leq 100$$.
* $$n$$ linii zawierających jedną z instrukcji tak jak opisano wcześniej.

### Wynik

* Liczba całkowita oznaczająca pozycję robota po wykonaniu wszystkich instrukcji.

## Przykład 1

### Dane

```
3
LEWO
PRAWO
JAK W 2
```

**Wynik:** $$1$$

## Przykład 2

### Dane

```
5
LEWO
JAK W 1
JAK W 2
JAK W 1
JAK W 4
```

**Wynik:** $$-3$$
