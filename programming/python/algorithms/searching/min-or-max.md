# Wyszukiwanie minimum i maksimum

## Opis problemu

{% content-ref url="../../../../algorithms/searching/min-or-max.md" %}
[min-or-max.md](../../../../algorithms/searching/min-or-max.md)
{% endcontent-ref %}

## Wyszukiwanie wartości minimum i maksimum

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def find_min(n: int, tab: list) -> int:
    min_val = tab[0]
    
    for i in range(1, n):
        if tab[i] < min_val:
            min_val = tab[i]
    
    return min_val


def find_max(n: int, tab: list) -> int:
    max_val = tab[0]
    
    for i in range(1, n):
        if tab[i] > max_val:
            max_val = tab[i]
    
    return max_val


tab = [8, 2, 9, 10, 5, 4, 2, 7, 18, 0]
n = 10
    
min_val = find_min(n, tab)
max_val = find_max(n, tab)
    
print("Min:", min_val)
print("Max:", max_val)
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/DxxLsK" %}
Wyszukiwanie wartości minimum i maksimum
{% endembed %}

## Wyszukiwanie indeksów wartości minimum i maksimum

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def find_min_ind(n: int, tab: list) -> int:
    min_ind = 0
    
    for i in range(1, n):
        if tab[i] < tab[min_ind]:
            min_ind = i
    
    return min_ind


def find_max_ind(n: int, tab: list) -> int:
    max_ind = 0
    
    for i in range(1, n):
        if tab[i] > tab[max_ind]:
            max_ind = i
    
    return max_ind


tab = [8, 2, 9, 10, 5, 4, 2, 7, 18, 0]
n = 10
    
min_ind = find_min_ind(n, tab)
max_ind = find_max_ind(n, tab)
    
print("Min index:", min_ind)
print("Max index:", max_ind)
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/Yy748p" %}
Wyszukiwanie indeksów wartości min i maks
{% endembed %}
