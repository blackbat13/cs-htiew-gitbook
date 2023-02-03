# Krzywa Peano

## Opis problemu

{% content-ref url="../../../../algorytmy/fraktale/krzywa-peano.md" %}
[krzywa-peano.md](../../../../algorytmy/fraktale/krzywa-peano.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```cpp
#include "turtle.hpp"

const int SIZE = 900;

Turtle turtle(SIZE, SIZE);

void peanoCurve(int rank, int angle, int length) {
    if (rank > 0) {
        turtle.turnRight(angle);
        peanoCurve(rank - 1, -angle, length);
        turtle.forward(length);
        peanoCurve(rank - 1, angle, length);
        turtle.forward(length);
        peanoCurve(rank - 1, -angle, length);
        turtle.turnLeft(angle);
    }
}

int main() {
    peanoCurve(5, 90, 10);
    
    turtle.saveBMP("krzywa_peano.bmp");

    return 0;
} 
```
{% endcode %}

### Link do implementacji

{% embed url="https://replit.com/@damiankurpiewski/PeanoCurve#main.cpp" %}
