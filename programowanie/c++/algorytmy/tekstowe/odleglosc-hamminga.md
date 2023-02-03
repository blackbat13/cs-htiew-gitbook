# Odległość Hamminga

## Opis problemu

{% content-ref url="../../../../algorytmy/tekstowe/odleglosc-hamminga.md" %}
[odleglosc-hamminga.md](../../../../algorytmy/tekstowe/odleglosc-hamminga.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```cpp
#include <iostream>

using namespace std;

int hammingDistance(string a, string b) {
    int distance = 0;
    
    for (int i = 0; i < a.length(); i++) {
        if (a[i] != b[i]) {
            distance++;
        }
    }

    return distance;
}

int main() {
    string a = "karolin";
    string b = "kerstin";
    
    int distance = hammingDistance(a, b);
    
    cout << distance << endl;

    return 0;
}
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/OVl4FY" %}
Odległość Hamminga
{% endembed %}
