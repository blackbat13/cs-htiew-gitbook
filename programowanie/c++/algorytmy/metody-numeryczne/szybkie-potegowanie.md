# Szybkie potęgowanie

## Opis problemu

{% content-ref url="../../../../algorytmy/metody-numeryczne/szybkie-potegowanie.md" %}
[szybkie-potegowanie.md](../../../../algorytmy/metody-numeryczne/szybkie-potegowanie.md)
{% endcontent-ref %}

## Rozwiązanie iteracyjne

```cpp
#include <iostream>

using namespace std;

/// Count a^n using the binary representation of n
/// \param a - number to rise
/// \param n - power
/// \return a^n
int fastExp(int a, int n) {
    int w = 1;

    while (n > 0) {
        if (n % 2 == 1) {
            w *= a;
        }

        a *= a;
        n /= 2;
    }

    return w;
}

int main() {
    int a = 2;
    int n = 10;
    int result = fastExp(a, n);
    
    cout << a << "^" << n << " = " << result << endl;
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/pdUCOO" %}
Szybkie potęgowanie - wersja iteracyjna
{% endembed %}

## Rozwiązanie rekurencyjne

```cpp
#include <iostream>

using namespace std;

/// Count a^n using the binary representation of n
/// \param a - number to rise
/// \param n - power
/// \return a^n
int fastExp(int a, int n) {
    if (n == 0) {
        return 1;
    }

    int result = fastExp(a, n / 2);

    if (n % 2 == 1) {
        return result * result * a;
    } else {
        return result * result;
    }
}

int main() {
    int a = 2;
    int n = 10;
    int result = fastExp(a, n);
    
    cout << a << "^" << n << " = " << result << endl;
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/zE3iXb" %}
Szybkie potęgowanie - wersja rekurencyjna
{% endembed %}