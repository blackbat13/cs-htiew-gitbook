# Test doskonałości

## Opis problemu

{% content-ref url="../../../../algorithms/integers/perfect-test.md" %}
[perfect-test.md](../../../../algorithms/integers/perfect-test.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
from math import ceil, sqrt


def is_perfect(n: int) -> bool:
    digits_sum = 1
    
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            digits_sum += i
            
            if n // i != i:
                digits_sum += n // i

    return digits_sum == n


n = 6

if is_perfect(n):
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')
```
{% endcode %}
