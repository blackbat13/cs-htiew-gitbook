# Test pierwszości

## Opis problemu

{% content-ref url="../../../../algorithms/integers/prime-test.md" %}
[prime-test.md](../../../../algorithms/integers/prime-test.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    sqrt_n = int(math.sqrt(n))
    
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False

    return True


n = 7

if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/PgfLBw" %}
Test pierwszości
{% endembed %}
