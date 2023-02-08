# Najdłuższy spójny podciąg rosnący

## Opis problemu

{% content-ref url="../../../../algorithms/searching/longest-growing-substring.md" %}
[longest-growing-substring.md](../../../../algorithms/searching/longest-growing-substring.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def longest_growing_substring_length(n: int, tab: list) -> int:
    mx = 1
    length = 1
    
    for i in range(1, n):
        if tab[i] > tab[i-1]:
            length += 1
            if length > mx:
                mx = length
        else:
            length = 1
    
    return mx


tab = [4, 9, 7, 2, 4, 7, 9, 3, 8, 6]
n = 10

result = longest_growing_substring_length(n, tab)
print(result)
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/66djuO" %}
Długość najdłuższego spójnego podciągu rosnącego
{% endembed %}