# Wyszukiwanie binarne

## Opis problemu

{% content-ref url="../../../../algorytmy/wyszukiwanie/wyszukiwanie-binarne.md" %}
[wyszukiwanie-binarne.md](../../../../algorytmy/wyszukiwanie/wyszukiwanie-binarne.md)
{% endcontent-ref %}

## Wersja iteracyjna

### Implementacja

```python
def binary_search_iterative(array: list, number: int) -> int:
    left = 0
    right = len(array) - 1
    
    while left < right:
        middle = (left + right) // 2
        
        if number < array[middle]:
            right = middle
        elif number > array[middle]:
            left = middle + 1
        else:
            return middle

    if left < len(array) and array[left] == number:
        return left

    return -1
    

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = 8

index = binary_search_iterative(array, number)

print(index)
```

### Link do implementacji

{% embed url="https://ideone.com/pFIHSC" %}
Wyszukiwanie binarne - wersja iteracyjna
{% endembed %}

### Opis implementacji

TODO

## Wersja rekurencyjna

### Implementacja

```python
def binary_search_recursive(array: list, number: int, left: int, right: int) -> int:
    if left < right:
        middle: int = (left + right) // 2
        
        if number < array[middle]:
            return binary_search_recursive(array, number, left, middle)
        elif number > array[middle]:
            return binary_search_recursive(array, number, middle + 1, right)
        else:
            return middle
    elif left < len(array) and array[left] == number:
        return left

    return -1
    
    
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = 8

index = binary_search_recursive(array, number, 0, len(array))

print(index)
```

### Link do implementacji

{% embed url="https://ideone.com/eYCLlP" %}
Wyszukiwanie binarne - wersja rekurencyjna
{% endembed %}

### Opis implementacji

TODO
