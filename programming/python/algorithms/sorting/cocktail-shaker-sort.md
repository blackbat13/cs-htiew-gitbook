# Sortowanie koktajlowe

## Opis problemu

{% content-ref url="../../../../algorithms/sorting/cocktail-shaker-sort.md" %}
[cocktail-shaker-sort.md](../../../../algorithms/sorting/cocktail-shaker-sort.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def cocktail_shaker_sort(array: list):
    for i in range(len(array) // 2 + 1):
        for j in range(i, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        
        for j in range(len(array) - 1 - i, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]

cocktail_shaker_sort(array)
    
print(array)
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/C38hze" %}
Sortowanie koktajlowe
{% endembed %}