# Znajdowanie lidera w zbiorze

## Opis problemu

Lider to element, który stanowi **większość** danego zbioru, a dokładniej stanowi **ponad połowę** zbioru. 

### Specyfikacja

#### Dane:

* $$n$$ — liczba naturalna, liczebność zbioru
* $$A[1..n]$$ — $$n-elementowy$$ zbiór liczb całkowitych, indeksowany od jedynki

#### Wynik:

* Lider podanego zbioru, lub -1, jeżeli lider nie istnieje.

{% hint style="info" %}
#### Lider zbioru

**Liderem** zbioru $$n-elementowego$$ nazywamy element, którego ilość wystąpień w zbiorze jest większa niż $$\frac{n}{2}$$.

Jeżeli taki element nie istnieje, to zbiór nie ma lidera.
{% endhint %}

### Przykład 1

#### Dane:

```
n := 10
A := [4, 1, 4, 4, 2, 3, 4, 3, 4, 4]
```

**Wynik**: 4

{% hint style="info" %}
#### Wyjaśnienie

Najczęściej występującym elementem w powyższym zbiorze jest wartość $$4$$, która występuje dokładnie $$6$$ razy, co **jest wartością większą** od $$n/2=10/2=5$$.
{% endhint %}

### Przykład 2

#### Dane:

```
n := 10
A := [4, 1, 4, 4, 2, 3, 4, 3, 4, 1]
```

**Wynik**: $$-1$$ (brak lidera)

{% hint style="info" %}
#### Wyjaśnienie

Najczęściej występującym elementem w powyższym zbiorze jest wartość $$4$$, która występuje dokładnie $$5$$ razy, co **nie jest** **wartością większą** od $$n/2=10/2=5$$.
{% endhint %}

## Rozwiązanie naiwne

W celu stwierdzenia, że dany element jest liderem zbioru, potrzebujemy wiedzieć, ile razy w zbiorze występuje. Gdybyśmy więc policzyli dla każdego elementu zbioru jego liczebność (liczbę wystąpień) w zbiorze, to bylibyśmy w stanie stwierdzić, czy zbiór posiada lidera, a jeśli tak, to jaki element jest tym liderem. Przechodzimy więc przez kolejne elementy zbioru i zliczamy ich wystąpienia. Oczywiście w ten sposób niektóre elementy policzymy wielokrotnie, ale właśnie dlatego jest to naiwne rozwiązanie.

### Pseudokod

```
funkcja SzukajLidera(n, A):
    1. Od i := 1 do n, wykonuj:
        2. ile := 0
        3. Od j := 1 do n, wykonuj:
            4. Jeżeli A[i] = A[j], to:
                5. ile := ile + 1
        6. Jeżeli ile > n/2, to:
            7. Zwróc A[i], zakończ
    8. Zwróc -1
```

### Złożoność

$$O(n^2)$$ — kwadratowa

## Rozwiązanie optymalne

W rozwiązaniu optymalnym należy zacząć od pewnego spostrzeżenia. Jeżeli weźmiemy jakiś zbiór i usuniemy z niego dwa **różne** elementy, to powstały w ten sposób zbiór będzie miał takiego samego lidera. Dzięki tej obserwacji możemy "skreślać" parami różne elementy, aż nie zostanie nam nic do skreślenia. Oczywiście nie będziemy fizycznie wykreślać elementów z tablicy. To "skreślanie" zrealizujemy za pomocą odpowiedniego zliczania i zapamiętywania tzw. *kandydata na lidera*. Zaczniemy od przyjęcia pierwszego elementu z tablicy jako kandydata na lidera. Zliczymy także jego liczbę dotychczasowych "nieskreślonych" powtórzeń. Następnie przejdziemy przez kolejne wartości z tablicy. Jeżeli w którymś momencie nasz licznik się wyzeruje, to przyjmiemy obecny element jako nowego kandydata i licznik ustawimy na jeden. Jeżeli natomiast licznik będzie większy od zera, należy porównać kandydata z obecnym elementem z tablicy. Jeżeli napotkamy wartość równą kandydatowi, to zwiększamy licznik wystąpień kandydata. Jeżeli natomiast napotkamy wartość różną od kandydata, to będziemy symulować "skreślanie" poprzez zmniejszenie licznika wystąpień obecnego kandydata o jeden.

Gdy już przejdziemy przez wszystkie elementy tablicy to na koniec zostaniemy z jakimś kandydatem na lidera. Jeżeli zbiór ma lidera, to będzie nim ten kandydat. Może być jednak tak, że zbiór nie ma lidera. Dlatego pozostaje nam zliczyć liczbę wystąpień naszego kandydata w zbiorze, co realizujemy przechodząc element po elemencie. Na koniec sprawdzamy, czyli liczba wystąpień kandydata jest większa od połowy liczebności zbioru.

### Pseudokod

```
funkcja SzukajLidera(n, A)
    1. lider := A[1]
    2. ile := 1
    3. Od i := 2 do n, wykonuj:
        4. Jeżeli ile = 0, to:
            5. lider := A[i]
            6. ile := 1
        
        7. w przeciwnym przypadku, jeżeli lider = A[i]:
            8. ile := ile + 1
        
        9. w przeciwnym przypadku:
            10. ile := ile - 1
        
    11. ile := 0
    12. Od i := 1 do n, wykonuj:
        13. Jeżeli A[i] = lider, to:
            14. ile := ile + 1
        
    15. Jeżeli ile > n/2, to:
        16. Zwróć lider, zakończ
    
    17. w przeciwnym przypadku:
        18. Zwróć -1, zakończ
```

### Złożoność

$$O(n)$$ — liniowa

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/searching/majority.md" %}
[majority.md](../../programming/c++/algorithms/searching/majority.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/searching/majority.md" %}
[majority.md](../../programming/python/algorithms/searching/majority.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programming/kotlin/algorithms/searching/majority.md" %}
[majority.md](../../programming/kotlin/algorithms/searching/majority.md)
{% endcontent-ref %}