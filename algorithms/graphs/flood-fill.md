---
description: Wypełnianie obszarów
---

# Flood fill

## Opis problemu

Flood fill jest algorytmem pozwalającym na wypełnienie/odwiedzenie pewnego zamkniętego obszaru. Przykładem może być kolorowanie obszarów zamkniętych w programach graficznych.

### Specyfikacja

TODO

### Przykład 1 - rekurencyjne wypełnianie obszaru pól połączonych ze sobą w linii prostej, poziomo lub pionowo.

![By André Karwath aka Aka - Own work, CC BY-SA 2.5, https://commons.wikimedia.org/w/index.php?curid=481651](../../.gitbook/assets/Recursive\_Flood\_Fill\_4\_\(aka\).gif)

### Przykład 2 - rekurencyjne wypełnianie obszaru pól połączonych ze sobą w dowolnym kierunku, także na ukos.

![By André Karwath aka Aka - Own work, CC BY-SA 2.5, https://commons.wikimedia.org/w/index.php?curid=481652](../../.gitbook/assets/Recursive\_Flood\_Fill\_8\_\(aka\).gif)

### Rozwiązanie

TODO

### Pseudokod

```
funkcja FloodFill(x, y):
    1. Jeżeli pole (x, y) jest oznaczone jako odwiedzone, to:
        2. Zakończ
        
    3. Oznacz pole (x, y) jako odwiedzone
    
    4. FloodFill(x + 1, y)
    5. FloodFill(x - 1, y)
    6. FloodFill(x, y + 1)
    7. FloodFill(x, y - 1)
```

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/graphs/flood-fill.md" %}
[flood-fill.md](../../programming/c++/algorithms/graphs/flood-fill.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/grafy/flood-fill.md" %}
[flood-fill.md](../../programming/python/algorithms/grafy/flood-fill.md)
{% endcontent-ref %}
