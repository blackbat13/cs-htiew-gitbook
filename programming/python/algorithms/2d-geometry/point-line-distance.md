# Odległość punktu od prostej

## Opis problemu

{% content-ref url="../../../../algorithms/2d-geometry/point-line-distance.md" %}
[point-line-distance.md](../../../../algorithms/2d-geometry/point-line-distance.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
from math import abs, sqrt


def point_line_distance(line_x1: float, line_y1: float, line_x2: float, line_y2: float, point_x: float, point_y: float) -> float:
    a = line_y2 - line_y1
    b = line_x2 - line_x1
    
    return abs(a * (line_x1 - point_x) + b * (point_y - line_y1)) / sqrt(a * a + b * b)


line_x1 = -3
line_y1 = -4
line_x2 = 7
line_y2 = 6
point_x = -5
point_y = -8

distance = point_line_distance(line_x1, line_y1, line_x2, line_y2, point_x, point_y)
    
print(distance)
```
{% endcode %}

### Opis implementacji

Funkcja `point_line_distance` przyjmuje jako argumenty współrzędne dwóch punktów (`line_x1`, `line_y1`, `line_x2`, `line_y2`) określających prostą oraz współrzędne punktu (`point_x`, `point_y`), dla którego obliczana jest odległość. Na początku obliczane są różnice między współrzędnymi drugiego punktu a pierwszego punktu prostej. Wartość `a` to różnica współrzędnymi $$y$$, a `b` to różnica pomiędzy współrzędnymi $$x$$.

Następnie obliczana jest odległość między punktem a prostą przy użyciu wzoru `abs(a * (line_x1 - point_x) + b * (point_y - line_y1)) / sqrt(a * a + b * b)`, gdzie:

- `a * (line_x1 - point_x) + b * (point_y - line_y1)` oblicza numeryczną wartość iloczynu skalarnego między wektorem normalnym do prostej a wektorem od pierwszego punktu prostej do badanego punktu,
- `abs(...)` oblicza wartość bezwzględną tego iloczynu skalarnego,
- `sqrt(a * a + b * b)` oblicza długość wektora normalnego do prostej.

Wynik obliczeń jest zwracany jako wartość odległości.

W przykładzie podane są konkretne wartości dla punktu `(point_x, point_y)` i prostych `(line_x1, line_y1, line_x2, line_y2)`. Funkcja `point_line_distance` jest wywoływana z tymi wartościami, a obliczona odległość jest wyświetlana przy użyciu funkcji `print`.

W wyniku wykonania tego kodu, zostanie wyświetlona odległość między punktem $$(-5, -8)$$ a prostą przechodzącą przez punkty $$(-3, -4)$$ i $$(7, 6)$$.
