# Sito Eratostenesa

## Opis problemu

{% content-ref url="../../../../algorithms/integers/eratosthenes-sieve.md" %}
[eratosthenes-sieve.md](../../../../algorithms/integers/eratosthenes-sieve.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
from math import ceil, sqrt


def sieve(n: int) -> list:
    primes = [False, False] + [True] * (n - 1)

    for i in range(2, ceil(sqrt(n))):
        if not primes[i]:
            continue

        for j in range(2 * i, n + 1, i):
            primes[j] = False

    return primes


def print_prime_numbers(primes: list):
    for i in range(len(primes)):
        if primes[i]:
            print(i)


n = 100

primes = sieve(n)

print_prime_numbers(primes)
```
{% endcode %}
