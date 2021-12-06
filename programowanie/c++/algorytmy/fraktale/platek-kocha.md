# Płatek Kocha

## Opis problemu

{% content-ref url="../../../../algorytmy/fraktale/platek-kocha.md" %}
[platek-kocha.md](../../../../algorytmy/fraktale/platek-kocha.md)
{% endcontent-ref %}

## Implementacja 

```cpp
#include "turtle.hpp"

const int SIZE = 900;

Turtle turtle(SIZE, SIZE);

void kochCurve(int rank, int length) {
    if (rank > 0) {
        kochCurve(rank - 1, length);
        turtle.turnLeft(60);
        kochCurve(rank - 1, length);
        turtle.turnRight(120);
        kochCurve(rank - 1, length);
        turtle.turnLeft(60);
        kochCurve(rank - 1, length);
    }
    else {
        turtle.forward(length);
    }
}

void kochSnowflake(int rank, int length) {
    for(int i = 0; i < 3; i++) {
        kochCurve(rank, length);
        turtle.turnRight(120);
    }
}

int main() {
    kochSnowflake(5, 1);
    
    turtle.saveBMP("platek_kocha.bmp");

    return 0;
} 
```

### Link do implementacji

{% embed url="https://replit.com/@damiankurpiewski/KochSnowflake#main.cpp" %}

### Opis implementacji

TODO
