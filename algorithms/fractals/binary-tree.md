# Drzewo binarne

## Opis problemu

TODO

### Specyfikacja

#### Dane

* $$n$$ - stopień drzewa binarnego
* $$w$$ - początkowa długość gałęzi (pnia)

#### Wynik

* Drzewo binarne stopnia $$n$$ i początkowej długości $$w$$.

### Prezentacja

{% file src="../../.gitbook/assets/Drzewo Binarne (1).pdf" %}
Drzewo binarne - wprowadzenie
{% endfile %}

## Rozwiązanie

### Prezentacja

{% file src="../../.gitbook/assets/Drzewo Binarne - algorytm (1).pdf" %}
Drzewo binarne - algorytm
{% endfile %}

### Pseudokod

```
funkcja DrzewoBinarne(n, w):
    1. Idź do przodu o w
    2. Jeżeli n > 0, to:
        3. Obróć się w lewo
        4. Wywołaj DrzewoBinarne(n - 1, w / 2)
        5. Obróć się w prawo
        6. Wywołaj DrzewoBinarne(n - 1, w / 2)
        7. Obróć się w lewo (do początkowego ustawienia)
    8. Idź do tyłu o w
```

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/fractals/binary-tree.md" %}
[binary-tree.md](../../programming/c++/algorithms/fractals/binary-tree.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/fractals/binary-tree.md" %}
[binary-tree.md](../../programming/python/algorithms/fractals/binary-tree.md)
{% endcontent-ref %}

### Blockly

{% content-ref url="../../programming/blockly/algorithms/fractals/binary-tree.md" %}
[binary-tree.md](../../programming/blockly/algorithms/fractals/binary-tree.md)
{% endcontent-ref %}
