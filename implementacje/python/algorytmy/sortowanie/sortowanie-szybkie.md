# Sortowanie szybkie

## Opis problemu

{% content-ref url="../../../../sortowanie/sortowanie-szybkie.md" %}
[sortowanie-szybkie.md](../../../../sortowanie/sortowanie-szybkie.md)
{% endcontent-ref %}

## Implementacja

```python
def quick_sort(array: list, left: int, right: int):
    if right <= left:
        return

    pivot = array[(left + right) // 2]
    i = left
    j = right
    
    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i > j:
            break

        array[i], array[j] = array[j], array[i]

        i += 1
        j -= 1

    quick_sort(array, left, j)
    quick_sort(array, i, right)


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]

quick_sort(array, 0, len(array) - 1)

print(array)
```

### Link do implementacji

{% embed url="https://ideone.com/z29zNR" %}
Sortowanie szybkie
{% endembed %}

### Opis implementacji

TODO
