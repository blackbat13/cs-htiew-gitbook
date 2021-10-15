# Rozkład na czynniki pierwsze

## Opis problemu

{% content-ref url="../../../../algorytmy/algorytmy-na-liczbach-calkowitych/rozklad-na-czynniki-pierwsze.md" %}
[rozklad-na-czynniki-pierwsze.md](../../../../algorytmy/algorytmy-na-liczbach-calkowitych/rozklad-na-czynniki-pierwsze.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

/// Given integer n print its prime factors
/// \param n - number to check
void distribute(int n) {
    int i = 2;
    
    while(n > 1) {
        if(n % i == 0) {
            cout << i << " ";
            n /= i;
        } else {
            i++;
        }
    }
}

int main() {
    int n = 124;

    cout << "Prime factors of " << n << ": ";
    distribute(n);

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/BiEykR" %}
Rozkład liczby na czynniki pierwsze
{% endembed %}

### Opis implementacji

TODO
