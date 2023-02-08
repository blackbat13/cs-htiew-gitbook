# Jednoczesne wyszukiwanie minimum i maksimum

## Opis problemu

{% content-ref url="../../../../algorithms/searching/jednoczesne-znajdowanie-minimum-i-maksimum.md" %}
[jednoczesne-znajdowanie-minimum-i-maksimum.md](../../../../algorithms/searching/jednoczesne-znajdowanie-minimum-i-maksimum.md)
{% endcontent-ref %}

## Podejście naiwne

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def find_min_max(array: list) -> (int, int):
    min = array[0]
    max = array[0]
    
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
        elif array[i] > max:
            max = array[i]

    return min, max
    

array = [3, 6, 1, 9, 10, 4, -4, 6, 12, 5, 11]

min, max = find_min_max(array)

print(f'Minimum: {min}, Maximum: {max}')
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/abPu9T" %}
Jednoczesne wyszukiwanie minimum i maksimum - podejście naiwne
{% endembed %}

## Podejście optymalne

{% code overflow="wrap" lineNumbers="true" %}
```python
def find_min_max(array: list) -> (int, int):
    min_candidates = []
    max_candidates = []
    
    for i in range(1, len(array), 2):
        if array[i - 1] < array[i]:
            min_candidates.append(array[i - 1])
            max_candidates.append(array[i])
        else:
            min_candidates.append(array[i])
            max_candidates.append(array[i - 1])

    if len(array) % 2 != 0:
        min_candidates.append(array[len(array) - 1])
        max_candidates.append(array[len(array) - 1])

    min = min_candidates[0]
    max = max_candidates[0]
    
    for i in range(1, len(min_candidates)):
        if min > min_candidates[i]:
            min = min_candidates[i]
        if max < max_candidates[i]:
            max = max_candidates[i]

    return min, max
    
    
array = [3, 6, 1, 9, 10, 4, -4, 6, 12, 5, 11]

min, max = find_min_max(array)

print(f'Minimum: {min}, Maximum: {max}')
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/CtHqmV" %}
Jednoczesne wyszukiwanie minimum i maksimum - podejście optymalne
{% endembed %}
