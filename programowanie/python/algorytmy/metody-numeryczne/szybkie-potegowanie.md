# Szybkie potęgowanie

## Opis problemu

{% content-ref url="../../../../algorytmy/metody-numeryczne/szybkie-potegowanie.md" %}
[szybkie-potegowanie.md](../../../../algorytmy/metody-numeryczne/szybkie-potegowanie.md)
{% endcontent-ref %}

## Rozwiązanie iteracyjne

```python
def fast_exp(a: int, n: int) -> int:
    w = 1
    
    while n > 0:
        if n % 2 == 1:
            w *= a

        a *= a
        n = n // 2

    return w


a = 2
n = 10

result = fast_exp(a, n)

print(f"{a}^{n} = {result}")
```

### Link do implementacji

{% embed url="https://ideone.com/pSGzrA" %}
Szybkie potęgowanie - wersja iteracyjna
{% endembed %}

## Rozwiązanie rekurencyjne

```python
def fast_exp(a: int, n : int) -> int:
    if n == 0:
        return 1
        
    if n % 2 == 1:
        return fast_exp(a, n // 2) ** 2 * a
    else:
        return fast_exp(a, n // 2) ** 2

 
a = 2
n = 10

result = fast_exp(a, n)

print(f"{a}^{n} = {result}")
```

### Link do implementacji

{% embed url="https://ideone.com/3i2qdR" %}
Szybkie potęgowanie - wersja rekurencyjna
{% endembed %}