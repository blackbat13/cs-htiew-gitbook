# Smocza krzywa

## Opis problemu

{% content-ref url="../../../../algorytmy/fraktale/smocza-krzywa.md" %}
[smocza-krzywa.md](../../../../algorytmy/fraktale/smocza-krzywa.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include "turtle.hpp"

const int SIZE = 900;

Turtle turtle(SIZE, SIZE);

void dragonCurve(int rank, int sign, int length) {
    if (rank > 0) {
        turtle.turnLeft(45 * sign);
        dragonCurve(rank - 1, 1, length);
        turtle.turnRight(90 * sign * -1);
        dragonCurve(rank - 1, -1, length);
        turtle.turnLeft(45 * sign);
    }
    else {
        turtle.forward(length);
    }
}

int main() {
    dragonCurve(12, 1, 5);
    
    turtle.saveBMP("smocza_krzywa.bmp");

    return 0;
} 
```

### Link do implementacji

{% embed url="https://replit.com/@damiankurpiewski/DragonCurve#main.cpp" %}

### Opis implementacji

TODO
