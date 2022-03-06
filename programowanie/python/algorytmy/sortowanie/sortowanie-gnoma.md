# Sortowanie gnoma

## Opis problemu

{% content-ref url="../../../../algorytmy/sortowanie/sortowanie-gnoma.md" %}
[sortowanie-gnoma.md](../../../../algorytmy/sortowanie/sortowanie-gnoma.md)
{% endcontent-ref %}

## Implementacja

```python
def gnome_sort(array: list, n: int):
    i = 0
    while i < n:
        if i == 0 or array[i] >= array[i - 1]:
            i += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
n = 10

gnome_sort(array, n)
    
print(array)
```

### Link do implementacji

{% embed url="https://ideone.com/sbsKNf" %}
Sortowanie gnoma
{% endembed %}