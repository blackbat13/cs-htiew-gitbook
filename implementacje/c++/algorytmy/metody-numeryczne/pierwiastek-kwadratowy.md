# Pierwiastek kwadratowy

## Opis problemu

{% content-ref url="../../../../algorytmy/metody-numeryczne/pierwiastek-kwadratowy.md" %}
[pierwiastek-kwadratowy.md](../../../../algorytmy/metody-numeryczne/pierwiastek-kwadratowy.md)
{% endcontent-ref %}

## Metoda Herona

### Implementacja

```cpp
#include <iostream>
#include <cmath>

using namespace std;

/// Counts square root of n with precision p using Heron method
/// \param n - number to count square root of
/// \param p - precision
/// \return square root of n with precision p
double squareRoot(double n, double p) {
    double x1 = n / 2;
    double x2 = (x1 + n / x1) / 2.0;
    while (fabs(x2 - x1) > p) {
        x1 = (x2 + n / x2) / 2.0;
        swap(x1, x2);
    }

    return x2;
}

int main() {
    cout << squareRoot(2, 0.00001);
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/I39nGk" %}
Pierwiastek kwadratowy - metoda Herona
{% endembed %}

### Opis implementacji

TODO
