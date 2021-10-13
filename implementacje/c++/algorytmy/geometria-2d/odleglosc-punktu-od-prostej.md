# Odległość punktu od prostej

## Opis problemu

{% content-ref url="../../../../geometria-2d/odleglosc-punktu-od-prostej.md" %}
[odleglosc-punktu-od-prostej.md](../../../../geometria-2d/odleglosc-punktu-od-prostej.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>
#include <cmath>

using namespace std;

/// Computes distance of the given point from the line given by two points
double pointLineDistance(double lineX1, double lineY1, double lineX2, double lineY2, double pointX, double pointY) {
    double a = lineY2 - lineY1;
    double b = lineX2 - lineX1;
    double result = abs(a * (lineX1 - pointX) + b * (pointY - lineY1)) / sqrt(a * a + b * b);
    return result;
}

int main() {
    double distance;
    distance = pointLineDistance(-3, -4, 7, 6, -5, -8);
    
    cout << "Distance of the point (-5, -8) from the line ((-3, -4), (7, 6)) is " << distance << endl;
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/0G86jv" %}
Odległość punktu od prostej
{% endembed %}

### Opis implementacji

TODO
