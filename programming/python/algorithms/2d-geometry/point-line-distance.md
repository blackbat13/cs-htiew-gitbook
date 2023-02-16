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
