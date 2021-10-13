# Sito Eratostenesa

## Opis problemu

{% content-ref url="../../../../algorytmy-na-liczbach-calkowitych/sito-eratostenesa.md" %}
[sito-eratostenesa.md](../../../../algorytmy-na-liczbach-calkowitych/sito-eratostenesa.md)
{% endcontent-ref %}

## Implementacja

```python
def sieve(n: int) -> list:
    primes = [False, False]
    
    for i in range(2, n + 1):
        primes.append(True)

    for i in range(2, n):
        if not primes[i]:
            continue

        for j in range(2 * i, n + 1, i):
            primes[j] = False

    return primes


def print_prime_numbers(primes: list) -> None:
    for i in range(0, len(primes)):
        if primes[i]:
            print(i)


n = 100

primes = sieve(n)

print_prime_numbers(primes)
```

### Link do implementacji

{% embed url="https://ideone.com/uQ3J6y" %}
Sito Eratostenesa
{% endembed %}

### Opis implementacji

TODO
