# Sito Eratostenesa

## Opis problemu

{% content-ref url="../../../../algorytmy-na-liczbach-calkowitych/sito-eratostenesa.md" %}
[sito-eratostenesa.md](../../../../algorytmy-na-liczbach-calkowitych/sito-eratostenesa.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>
using namespace std;

/// Count prime numbers up to n
/// \param n - number op to which we count prime numbers
void eratosthenesSieve(int n) {
    bool prime[n+1];
    prime[0]=false;
    prime[1]=false;

    for(int i = 2; i <= n; i++) {
        prime[i] = true;
    }

    for(int i = 2; i < n; i++) {
        if(!prime[i]) {
            continue;
        }

        for(int j = 2*i; j <= n; j+=i) {
            prime[j] = false;
        }
    }

    cout << "Prime numbers from 1 to " << n << ":" << endl;
    for(int i = 2; i <= n; i++) {
        if(prime[i]) {
            cout << i << " ";
        }
    }

    cout << endl;
}

int main() {
    int n = 100;
    
    eratosthenesSieve(n);

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/f5kW3G" %}
Sito Eratostenesa
{% endembed %}

### Opis implementacji

TODO
