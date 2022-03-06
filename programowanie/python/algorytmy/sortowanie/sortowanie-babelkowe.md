# Sortowanie bąbelkowe

## Opis problemu

{% content-ref url="../../../../algorytmy/sortowanie/sortowanie-babelkowe.md" %}
[sortowanie-babelkowe.md](../../../../algorytmy/sortowanie/sortowanie-babelkowe.md)
{% endcontent-ref %}

## Implementacja

```python
def bubble_sort(array: list):
	sorted = False
	i = 0
	while not sorted:
		sorted = True
		for j in range(len(array) - 1, i, -1):
			if array[j - 1] > array[j]:
				array[j], array[j - 1] = array[j-1], array[j]
				sorted = False
		i += 1


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]

bubble_sort(array)

print(array)
```

### Link do implementacji

{% embed url="https://ideone.com/1WKZb9" %}
Sortowanie bąbelkowe
{% endembed %}