# Trójkąt Sierpińskiego

## Opis problemu

{% content-ref url="../../../../fraktale/trojkat-sierpinskiego.md" %}
[trojkat-sierpinskiego.md](../../../../fraktale/trojkat-sierpinskiego.md)
{% endcontent-ref %}

## Implementacja

```python
import turtle


def sierpinski_triangle(rank, length):
    if rank == 0:
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
        turtle.end_fill()
        return

    for _ in range(3):
        sierpinski_triangle(rank - 1, length / 2)
        turtle.forward(length)
        turtle.left(120)


turtle.speed(0)
turtle.penup()
turtle.back(200)
turtle.pendown()

sierpinski_triangle(4, 300)

turtle.done()
```

### Link do implementacji

{% embed url="https://replit.com/@damiankurpiewski/Sierpinski-Triangle#main.py" %}

### Opis implementacji

TODO
