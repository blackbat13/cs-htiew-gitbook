# Sortowanie przez wstawianie

## Opis problemu

{% content-ref url="../../../../algorytmy/sortowanie/sortowanie-przez-wstawianie.md" %}
[sortowanie-przez-wstawianie.md](../../../../algorytmy/sortowanie/sortowanie-przez-wstawianie.md)
{% endcontent-ref %}

## Implementacja

```python
def insertion_sort(array: list):
    for i in range(1, len(array)):
        j = i
        
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]

insertion_sort(array)

print(array)
```

### Link do implementacji

{% embed url="https://ideone.com/ublO4B" %}
Sortowanie przez wstawianie
{% endembed %}

### Opis implementacji

TODO
