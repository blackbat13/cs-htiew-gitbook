# Liczby Fibonacciego

## Opis problemu

{% content-ref url="../../../../algorytmy-na-liczbach-calkowitych/liczby-fibonacciego.md" %}
[liczby-fibonacciego.md](../../../../algorytmy-na-liczbach-calkowitych/liczby-fibonacciego.md)
{% endcontent-ref %}

## Podejście rekurencyjne

### Implementacja

```cpp
#include <iostream>
using namespace std;

/// Count n'th fibonacci number using recursive method
/// \param n - index of fibonacci number to count
/// \return n'th fibonacci number
int fib(int n) {
    if (n <= 2) {
        return 1;
    }

    return fib(n - 1) + fib(n - 2);
}

int main() {
    int n = 10;
    int result = fib(n);

    cout << "fib(" << n << ") = " << fib(n) << endl;

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/mZ2lJX" %}
Liczby Fibonacciego - podejście rekurencyjne
{% endembed %}

### Opis implementacji

TODO

## Podejście iteracyjne

### Implementacja

```cpp
#include <iostream>
using namespace std;

/// Count n'th fibonacci number using iterative method
/// \param n - index of fibonacci number to count
/// \return n'th fibonacci number
int fib(int n) {
    if (n <= 2) {
        return 1;
    }

    int f1 = 1, f2 = 1;
    for (int i = 3; i <= n; i++) {
        int f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
    }

    return f2;
}

int main() {
    int n = 10;
    int result = fib(n);

    cout << "fib(" << n << ") = " << fib(n) << endl;

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/3PU7Fv" %}
Liczby Fibonacciego - podejście iteracyjne
{% endembed %}

### Opis implementacji

TODO
