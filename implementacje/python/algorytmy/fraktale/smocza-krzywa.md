# Smocza krzywa

## Opis problemu

{% content-ref url="../../../../fraktale/smocza-krzywa.md" %}
[smocza-krzywa.md](../../../../fraktale/smocza-krzywa.md)
{% endcontent-ref %}

## Implementacja

```python
import turtle


def dragon_curve(rank, sign, length):
    if rank > 0:
        turtle.left(45 * sign)
        dragon_curve(rank - 1, 1, length)
        turtle.right(90 * sign * -1)
        dragon_curve(rank - 1, -1, length)
        turtle.left(45 * sign)
    else:
        turtle.forward(length)


turtle.speed(0)
turtle.penup()
turtle.back(150)
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.pendown()

dragon_curve(10, 1, 5)

turtle.done()
```

### Link do implementacji

{% embed url="https://replit.com/@damiankurpiewski/Dragon-Curve#main.py" %}

### Opis implementacji

TODO
