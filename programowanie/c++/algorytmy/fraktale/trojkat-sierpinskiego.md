# Trójkąt Sierpińskiego

## Opis problemu

{% content-ref url="../../../../algorytmy/fraktale/trojkat-sierpinskiego.md" %}
[trojkat-sierpinskiego.md](../../../../algorytmy/fraktale/trojkat-sierpinskiego.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include "turtle.hpp"

const int SIZE = 900;

Turtle turtle(SIZE, SIZE);

void sierpinskiTriangle(int rank, int length) {
    if (rank == 0) {
        turtle.beginFill();
        for(int i = 0; i < 3; i++) {
            turtle.forward(length);
            turtle.turnLeft(120);
        }

        turtle.endFill();
        return;
    }

    for(int i = 0; i < 3; i++) {
        sierpinskiTriangle(rank - 1, length / 2);
        turtle.forward(length);
        turtle.turnLeft(120);
    }
}

int main() {
    turtle.penUp();
    turtle.goTo(-SIZE / 2, -SIZE / 2);
    turtle.penDown();

    sierpinskiTriangle(6, SIZE);
    
    turtle.saveBMP("trojkat_sierpinskiego.bmp");

    return 0;
} 
```

### Link do implementacji

{% embed url="https://replit.com/@damiankurpiewski/SierpinskiTriangle#main.cpp" %}

### Opis implementacji

TODO
