# Wszystkie dzielniki

## Opis problemu

{% content-ref url="../../../../algorithms/integers/divisors.md" %}
[divisors.md](../../../../algorithms/integers/divisors.md)
{% endcontent-ref %}

## Rozwiązanie zupełnie naiwne

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def divisors(n: int):
	for i in range(1, n + 1):
		if n % i == 0:
			print(i)
 
 
n = 12
 
divisors(n)
```
{% endcode %}

## Rozwiązanie naiwne

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def divisors(n: int):
	for i in range(1, (n // 2) + 1):
		if n % i == 0:
			print(i)
 
	if n > 1:
		print(n)
		
		
n = 12
 
divisors(n)
```
{% endcode %}

## Rozwiązanie optymalne

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
from math import sqrt, ceil


def divisors(n: int):
	for i in range(1, ceil(sqrt(n))):
		if n % i == 0:
			print(i)
			if i != (n // i):
				print(n // i)
 
 
n = 12
 
divisors(n)
```
{% endcode %}
