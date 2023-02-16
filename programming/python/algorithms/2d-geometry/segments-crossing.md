# Przecinanie się odcinków

## Opis problemu

{% content-ref url="../../../../algorithms/2d-geometry/segments-crossing.md" %}
[segments-crossing.md](../../../../algorithms/2d-geometry/segments-crossing.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def det3(matrix: list) -> int:
    return matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[1][0] * matrix[2][1] * matrix[0][2] + matrix[2][0] * \
           matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1] * matrix[2][0] - matrix[0][1] * matrix[1][0] * \
           matrix[2][2] - matrix[0][0] * matrix[1][2] * matrix[2][1]
           

def point_on_segment(a_x: int, a_y: int, b_x: int, b_y: int, c_x: int, c_y: int) -> bool:
    matrix = [
         [a_x, a_y, 1],
         [b_x, b_y, 1],
         [c_x, c_y, 1]]
    
    if det3(matrix) != 0:
        return False

    return min(a_x, b_x) <= c_x <= max(a_x, b_x) and min(a_y, b_y) <= c_y <= max(a_y, b_y):


def sgn(a: int) -> int:
    if a < 0:
        return -1
    elif a > 0:
        return 1
    else:
        return 0


def segment_crossing(a_x: int, a_y: int, b_x: int, b_y: int, c_x: int, c_y: int, d_x: int, d_y: int) -> bool:
    return point_on_segment(a_x, a_y, b_x, b_y, c_x, c_y) or \
            point_on_segment(a_x, a_y, b_x, b_y, d_x, d_y) or \
            point_on_segment(c_x, c_y, d_x, d_y, a_x, a_y) or \
            point_on_segment(c_x, c_y, d_x, d_y, b_x, b_y) or \
            sgn(det3([[a_x, a_y, 1], [b_x, b_y, 1], [c_x, c_y, 1]])) != sgn(
            det3([[a_x, a_y, 1], [b_x, b_y, 1], [d_x, d_y, 1]]))


a_x = 1
a_y = 1
b_x = 2
b_y = 2

c_x = 3
c_y = 3
d_x = 4
d_y = 4

result = segment_crossing(a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y)

if result:
	print(f"Odcinki [({a_x}, {a_y}), ({b_x}, {b_y})] oraz [({c_x}, {c_y}), ({d_x}, {d_y})] przecinają się")
else:
	print(f"Odcinki [({a_x}, {a_y}), ({b_x}, {b_y})] oraz [({c_x}, {c_y}), ({d_x}, {d_y})] nie przecinają się")
```
{% endcode %}
