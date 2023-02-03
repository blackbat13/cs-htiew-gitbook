# Test pierwszości

## Opis problemu

{% content-ref url="../../../../algorytmy/algorytmy-na-liczbach-calkowitych/test-pierwszosci.md" %}
[test-pierwszosci.md](../../../../algorytmy/algorytmy-na-liczbach-calkowitych/test-pierwszosci.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```cpp
#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }

    for (int i = 2; i <= sqrt(n); i++) {
        if(n % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int n = 7;

    bool result = isPrime(n);
    
    if (result) {
        cout << n << " is prime" << endl;
    } else {
        cout << n << " is not prime" << endl;
    }

    return 0;
}
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/0vg44U" %}
Test pierwszości
{% endembed %}
