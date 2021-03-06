# Sortowanie grzebieniowe

## Opis problemu

{% content-ref url="../../../../algorytmy/sortowanie/sortowanie-grzebieniowe.md" %}
[sortowanie-grzebieniowe.md](../../../../algorytmy/sortowanie/sortowanie-grzebieniowe.md)
{% endcontent-ref %}

## Implementacja

```python
def comb_sort(array: list, n: int):
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                sorted = False

            i += 1


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
n = 10

comb_sort(array, n)
    
print(array)
```

### Link do implementacji

{% embed url="https://ideone.com/gzuvFP" %}
Sortowanie koktajlowe
{% endembed %}