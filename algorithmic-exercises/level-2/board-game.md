# Gra planszowa

Bajtek zaprojektował nową grę planszową. Gra składa się z jednej planszy o $$n$$ polach i jednej $$n$$-ściennej kości z wartościami od $$1$$ do $$n$$ oraz pionka do gry. Na planszy znajduje się $$n$$ pól ułożonych jedno obok drugiego, w efekcie tworząc jedną długą linię. Na każdym polu znajduje się jedna liczba całkowita: liczba punktów przypisanych do tego pola. Pierwsze pole ma zawsze przypisaną wartość $$0$$.

Zasady gry są proste. Gracz stawia swój pionek na pierwszym polu na planszy i wykonuje rzut kością. Następnie przemieszcza pionka o tyle pól, ile wypadło oczek na kości. Ruch pionka wykonywany jest wielokrotnie, zawsze o tyle samo pól, aż pionek wyjdzie poza planszę. Wartości z odwiedzonych przez pionka pól są sumowane i stanowią wynik danego gracza.

Dla przykładu załóżmy, że mamy planszę o długości $$5$$ z wartościami $$[0, 6, -1, 2, 4]$$. Rzut kością wskazał liczbę $$2$$, więc pionek odwiedzi trzy pola: pierwsze, trzecie oraz piąte (po kolejnym ruchu wyjdzie już poza planszę). Wartości tych pól to odpowiednio: $$0$$, $$-1$$ oraz $$4$$, więc wynik gracza wynosi $$0+(-1)+4=3$$ punkty.

Bajtek ma duże doświadczenie w rzucaniu różnymi kostkami i dokładnie wie jak sprawić, by wypadło tyle oczek ile sobie zażyczy. Nie wie jednak, ile powinien wyrzucić aby dla danej planszy zdobyć maksymalny wynik, dlatego zwrócił się o pomoc do Ciebie!

## Dane

Na wejściu znajduje się liczba $$n$$ ($$1\lq n\lq 10^6$$) oznaczająca długość planszy. Następnie podanych jest $$n$$ liczb całkowitych z przedziału $$<-1000, 1000>$$, każda w osobnej linii.

## Wynik

Dwie liczby całkowite: maksymalny możliwy do uzyskania wynik oraz liczba oczek na kości (z zakresu $$<1, n>$$) potrzebna do uzyskania tego wyniku. Jeżeli maksymalny wynik można uzyskać na kilka sposobów, wypisz dowolny z nich.

## Przykład

### Dane

```
5
0
6
-1
2
4
```

### Wynik

```
12
1
```