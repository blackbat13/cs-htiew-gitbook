# Punkt na odcinku

## Opis problemu

{% content-ref url="../../../../algorithms/2d-geometry/point-on-segment.md" %}
[point-on-segment.md](../../../../algorithms/2d-geometry/point-on-segment.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def det3(matrix: list) -> int:
    return matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[1][0] * matrix[2][1] * matrix[0][2] + matrix[2][0] * \
           matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1] * matrix[2][0] - matrix[0][1] * matrix[1][0] * \
           matrix[2][2] - matrix[0][0] * matrix[1][2] * matrix[2][1]


def point_on_segment(a: dict, b: dict, c: dict) -> bool:
    matrix = [
         [a["x"], a["y"], 1],
         [b["x"], b["y"], 1],
         [c["x"], c["y"], 1]]
    
    if det3(matrix) != 0:
        return False

    return min(a["x"], b["x"]) <= c["x"] <= max(a["x"], b["x"]) and min(a["y"], b["y"]) <= c["y"] <= max(a["y"], b["y"])


a = {"x": 1, "y": 1}
b = {"x": 5, "y": 5}
c = {"x": 2, "y": 2}

result = point_on_segment(a, b, c)

if result:
	print(f"Point ({c['x']}, {c['y']}) on segment [({a['x']}, {a['y']}), ({b['x']}, {b['y']})]")
else:
	print(f"Point ({c['x']}, {c['y']}) not on segment [({a['x']}, {a['y']}), ({b['x']}, {b['y']})]")
```
{% endcode %}
