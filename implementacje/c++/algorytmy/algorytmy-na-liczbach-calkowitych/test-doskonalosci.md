# Test doskonałości

## Opis problemu

{% content-ref url="../../../../algorytmy-na-liczbach-calkowitych/test-doskonalosci.md" %}
[test-doskonalosci.md](../../../../algorytmy-na-liczbach-calkowitych/test-doskonalosci.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>
#include <cmath>

using namespace std;

/// Check if n is perfect
/// \param n - number to check
/// \return true if n is perfect number, false otherwise
bool isPerfect(int n) {
    int sum = 0;

    for(int i = 1; i < n; i++) {
        if(n % i == 0) {
            sum += i;
        }
    }

    return sum == n;
}

int main() {
    int n = 6;
    
    if(isPerfect(n)) {
        cout << n << " is perfect" << endl;
    } else {
        cout << n << " is not perfect" << endl;
    }

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/1RcqQL" %}
Test doskonałości
{% endembed %}

### Opis implementacji

TODO
