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
    1. Przod(w)
    2. Jeżeli n > 0, to:
        3. Lewo(45)
        4. DrzewoBinarne(n - 1, w / 2)
        5. Prawo(90)
        6. DrzewoBinarne(n - 1, w / 2)
        7. Lewo(45)
    8. Tyl(w)
```

### Schemat blokowy

```mermaid
flowchart TD
	START(["DrzewoBinarne(n, w)"]) --> K1["Przod(w)"]
	K1 --> K2{n > 0}
	K2 -- PRAWDA --> K3["Lewo(45)\nDrzewoBinarne(n - 1, w / 2)\nPrawo(90)\nDrzewoBinarne(n - 1, w / 2)\nLewo(45)"]
	K3 --> K8["Tyl(w)"]
	K2 -- FAŁSZ --> K8
	K8 --> STOP([STOP])
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
