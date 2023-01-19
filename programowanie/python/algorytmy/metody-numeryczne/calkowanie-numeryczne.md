# Całkowanie numeryczne

## Opis problemu

{% content-ref url="../../../../algorytmy/metody-numeryczne/calkowanie-numeryczne.md" %}
[calkowanie-numeryczne.md](../../../../algorytmy/metody-numeryczne/calkowanie-numeryczne.md)
{% endcontent-ref %}

## Metoda prostokątów

{% code overflow="wrap" lineNumbers="true" %}
```python
def f(x: float) -> float:
    return x * x + 2 * x


def rectangles_method(a: int, b: int, n: int) -> float:
    rectangle_width = (b - a) / n
    area = 0
    current_point = a

    for i in range(n):
        current_point += rectangle_width
        rectangle_height = f(current_point)
        area += rectangle_height * rectangle_width

    return area


a = 0
b = 10
n = 100
area = rectangles_method(a, b, n)
print(area)
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/RUaW5V" %}
Całkowanie numeryczne - metoda prostokątów
{% endembed %}

### Opis implementacji

TODO

## Metoda trapezów

{% code overflow="wrap" lineNumbers="true" %}
```python
def f(x: float) -> float:
    return x * x + 2 * x


def trapezes_method(a: int, b: int, n: int) -> float:
    trapeze_height = (b - a) / n
    area = 0
    current_point = a

    for i in range(n):
        trapeze_first_side = f(current_point)
        current_point += trapeze_height
        trapeze_second_side = f(current_point)
        area += ((trapeze_first_side + trapeze_second_side) * trapeze_height) / 2

    return area


a = 0
b = 10
n = 100
area = trapezes_method(a, b, n)
print(area)
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/DnRDEH" %}
Całkowanie numeryczne - metoda trapezów
{% endembed %}

### Opis implementacji

TODO
