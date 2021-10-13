# Sortowanie przez zliczanie

## Opis problemu

{% content-ref url="../../../../sortowanie/sortowanie-przez-zliczanie.md" %}
[sortowanie-przez-zliczanie.md](../../../../sortowanie/sortowanie-przez-zliczanie.md)
{% endcontent-ref %}

## Implementacja

```python
def count_occurrences(array: [], max_number: int) -> []:
    occurrences = [0 for _ in range(max_number + 1)]

    for number in array:
        occurrences[number] += 1
        
    return occurrences


def counting_sort(array: list):
    occurrences = count_occurrences(array, 100)

    array.clear()
    
    for i in range(len(occurrences)):
        for j in range(occurrences[i]):
            array.append(i)


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]

counting_sort(array)

print(array)
```

### Link do implementacji

{% embed url="https://ideone.com/NYyWxx" %}
Sortowanie przez zliczanie
{% endembed %}

### Opis implementacji

TODO

Lista `occurrences` służy do zliczania liczby wystąpień poszczególnych wartości w liście `array`. Na początku wypełniamy ją zerami (**linia 3**) od pozycji 0 do pozycji wyznaczonej przez maksymalny element (zmienna `max_number`).

Po utworzeniu listy liczników przechodzimy do zliczania. Dla każdego elementu (zmienna `number`) w liście `array `(**linia 5**) zwiększamy przypisany do tego elementu licznik (**linia 6**).

Po zliczeniu wszystkich elementów, czyścimy sortowaną listę za pomocą polecenia `clear()` (**linia 8**), by móc ją wypełnić posortowanymi wartościami.

Następnie przechodzimy przez wszystkie liczniki na liście `occurrences` (**linia 9**) i dla każdego licznika tyle razy ile wynosi jego wartość (**linia 10**) dodajemy odpowiednią liczbę do sortowanej listy (**linia 11**).
