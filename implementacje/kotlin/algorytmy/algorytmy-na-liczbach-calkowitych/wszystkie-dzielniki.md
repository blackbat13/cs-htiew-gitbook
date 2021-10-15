# Wszystkie dzielniki

## Opis problemu

{% content-ref url="../../../../algorytmy/algorytmy-na-liczbach-calkowitych/wszystkie-dzielniki.md" %}
[wszystkie-dzielniki.md](../../../../algorytmy/algorytmy-na-liczbach-calkowitych/wszystkie-dzielniki.md)
{% endcontent-ref %}

## Rozwiązanie zupełnie naiwne

### Implementacja

```python
def divisors(n: int):
	for i in range(1, n + 1):
		if n % i == 0:
			print(i)
 
 
n = 12
 
divisors(n)
```

### Link do implementacji

{% embed url="https://ideone.com/bNjeR2" %}
Wszystkie dzielniki - podejście zupełnie naiwne
{% endembed %}

### Opis implementacji

TODO

## Rozwiązanie naiwne

### Implementacja

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

### Link do implementacji

{% embed url="https://ideone.com/1ZKypb" %}
Wszystkie dzielniki - podejście naiwne
{% endembed %}

### Opis implementacji

TODO

## Rozwiązanie optymalne

### Implementacja

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

### Link do implementacji

{% embed url="https://ideone.com/jZpx7E" %}
Wszystkie dzielniki - podejście optymalne
{% endembed %}

### Opis implementacji

TODO
