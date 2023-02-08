# Test doskonałości

## Opis problemu

{% content-ref url="../../../../algorithms/integers/perfect-test.md" %}
[perfect-test.md](../../../../algorithms/integers/perfect-test.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def is_perfect(n: int) -> bool:
    sum = 0
    
    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum == n


n = 6

if is_perfect(n):
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/4EALRV" %}
Test doskonałości
{% endembed %}
