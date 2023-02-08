# Suma dwóch liczb

## Opis problemu

{% content-ref url="../../../../algorithms/searching/sum-of-two.md" %}
[sum-of-two.md](../../../../algorithms/searching/sum-of-two.md)
{% endcontent-ref %}

## Rozwiązanie naiwne

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def sum_of_two(n : int, tab : list, k : int):
    for i in range(n):
        for j in range(i+1, n):
            if tab[i] + tab[j] == k:
                print(tab[i], tab[j])
                return
                
    print(-1)
    

n = 10
tab = [1, 2, 4, 6, 8, 9, 10, 12, 13, 15]
k = 18

sum_of_two(n, tab, k)
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/7iwqRc" %}
Suma dwóch - rozwiązanie naiwne
{% endembed %}

## Rozwiązanie optymalne

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def sum_of_two(n : int, tab : list, k : int):
    left = 0
    right = n - 1
    
    while left < right and tab[left] + tab[right] != k:
        if tab[left] + tab[right] < k:
            left += 1
        else:
            right -= 1
            
    if left < right:
        print(tab[left], tab[right])
    else:
        print(-1)
     
           
n = 10
tab = [1, 2, 4, 6, 8, 9, 10, 12, 13, 15]
k = 18

sum_of_two(n, tab, k)
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/qarXHf" %}
Suma dwóch - rozwiązanie optymalne
{% endembed %}
