# Wydawanie reszty

## Opis problemu

TODO

### Specyfikacja

#### Dane

* $$n$$ — liczba naturalna, ilość dostępnych nominałów
* $$nom[1..n]$$ — tablica dostępnych nominałów (liczb całkowitych) o rozmiarze $$n$$&#x20;
* $$kw$$ — liczba naturalna, kwota do wydania

#### Wynik

* Minimalna liczba potrzebnych monet/banknotów do wydania kwoty $$kw$$ przy użyciu nominałów $$nom$$.

### Przykład

TODO

## Rozwiązanie zachłanne

TODO

### Pseudokod

```
funkcja Reszta(n, nom, kw):
    1. Sortujemy tablicę nom od największych do najmniejszych (malejąco)
    2. wynik := 0
    3. Od i := 1 do n, wykonuj:
        4. Dopóki kw >= nom[i], to:
            5. kw := kw - nom[i]
            6. wynik := wynik + 1
            
    7. Zwróć wynik
```

#### Optymalizacja

```
funkcja Reszta(n, nom, kw):
    1. Sortujemy tablicę nom od największych do najmniejszych (malejąco)
    2. wynik := 0
    3. Od i := 1 do n, wykonuj:
        4. Jeżeli kw >= nom[i], to:
            5. wynik := wynik + kw div nom[i]
            6. kw := kw mod nom[i]
            
    7. Zwróć wynik
```

{% hint style="info" %}
**div** oznacza dzielenie całkowite

**mod** oznacza resztę z dzielenia
{% endhint %}

### Złożoność

$$O(n)$$ - liniowa

## Rozwiązanie dynamiczne

TODO

### Pseudokod

TODO

### Złożoność

TODO

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/algorytmy-na-liczbach-calkowitych/wydawanie-reszty.md" %}
[wydawanie-reszty.md](../../programowanie/c++/algorytmy/algorytmy-na-liczbach-calkowitych/wydawanie-reszty.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/algorytmy-na-liczbach-calkowitych/zachlanne-wydawanie-reszty.md" %}
[zachlanne-wydawanie-reszty.md](../../programowanie/python/algorytmy/algorytmy-na-liczbach-calkowitych/zachlanne-wydawanie-reszty.md)
{% endcontent-ref %}
