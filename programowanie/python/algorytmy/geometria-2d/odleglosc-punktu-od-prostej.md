# Odległość punktu od prostej

## Opis problemu

{% content-ref url="../../../../algorytmy/geometria-2d/odleglosc-punktu-od-prostej.md" %}
[odleglosc-punktu-od-prostej.md](../../../../algorytmy/geometria-2d/odleglosc-punktu-od-prostej.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
from math import abs, sqrt


def point_line_distance(line_x1: float, line_y1: float, line_x2: float, line_y2: float, point_x: float, point_y: float) -> float:
    a = line_y2 - line_y1
    b = line_x2 - line_x1
    
    result = abs(a * (line_x1 - point_x) + b * (point_y - line_y1)) / sqrt(a * a + b * b)
    
    return result


distance = point_line_distance(-3, -4, 7, 6, -5, -8)
    
print("Distance of the point (-5, -8) from the line ((-3, -4), (7, 6)) is", distance)
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/AeowcV" %}
Odległość punktu od prostej
{% endembed %}
