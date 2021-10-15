# Całkowanie numeryczne

## Opis problemu

{% content-ref url="../../../../algorytmy/metody-numeryczne/calkowanie-numeryczne.md" %}
[calkowanie-numeryczne.md](../../../../algorytmy/metody-numeryczne/calkowanie-numeryczne.md)
{% endcontent-ref %}

## Metoda prostokątów

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Function to integrate
double f(double x) {
    return x * x + 2 * x;
}


/// Compute area under function f
///   from a to b using n rectangles
/// \param a - start of range
/// \param b - end of range
/// \param n - number of rectangles to use
/// \return area under function f in range [a,b]
double rectanglesMethod(int a, int b, int n) {
    double width = (b - a)/(double)n;
    double area = 0;
    double currentPoint = a;
    double height;

    for(int i = 0; i < n; i++) {
        currentPoint += width;
        height = f(currentPoint);
        area += height * width;
    }

    return area;
}

int main() {
    int a, b, n;
    a = 1;
    b = 5;
    n = 100;

    cout << "Wynik metody prostokatow: " << rectanglesMethod(a,b,n) << endl;

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/0nciRF" %}
Całkowanie numeryczne - metoda prostokątów
{% endembed %}

### Opis implementacji

TODO

## Metoda trapezów

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Function to integrate
double f(double x) {
    return x * x + 2 * x;
}

/// Compute area under function f
///   from a to b using n trapezes
/// \param a - start of range
/// \param b - end of range
/// \param n - number of trapezes to use
/// \return area under function f in range [a,b]
double trapezesMethod(int a, int b, int n) {
    double height = (b - a)/(double)n;
    double area = 0;
    double currentPoint = a;
    double side1, side2;

    for(int i = 0; i < n; i++) {
        side1 = f(currentPoint);
        currentPoint += height;
        side2 = f(currentPoint);

        area += ((side1 + side2) * height) / 2.0;
    }

    return area;
}

int main() {
    int a, b, n;
    a = 1;
    b = 5;
    n = 100;

    cout << "Wynik metody trapezow: " << trapezesMethod(a,b,n) << endl;

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/6Fad9m" %}
Całkowanie numeryczne - metoda trapezów
{% endembed %}

### Opis implementacji

TODO
