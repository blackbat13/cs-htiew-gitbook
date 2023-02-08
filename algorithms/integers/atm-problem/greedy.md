# Rozwiązanie zachłanne

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

## Implementacja

### C++

{% content-ref url="../../../programming/c++/algorithms/integers/change.md" %}
[change.md](../../../programming/c++/algorithms/integers/change.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../../programming/python/algorithms/integers/change.md" %}
[change.md](../../../programming/python/algorithms/integers/change.md)
{% endcontent-ref %}
