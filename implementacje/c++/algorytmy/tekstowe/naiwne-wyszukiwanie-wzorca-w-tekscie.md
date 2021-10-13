# Naiwne wyszukiwanie wzorca w tekście

## Opis problemu

{% content-ref url="../../../../tekstowe/naiwne-wyszukiwanie-wzorca-w-tekscie.md" %}
[naiwne-wyszukiwanie-wzorca-w-tekscie.md](../../../../tekstowe/naiwne-wyszukiwanie-wzorca-w-tekscie.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

/// Check if one string is a substring of the other
/// \param a - string to search for
/// \param b - string to search in
/// \return true if a is substring of b
bool isSubstring(string a, string b) {
    int i, j;

    for (i = 0; i < b.length() - a.length(); i++) {
        j = 0;
        while (j < a.length()) {
            if (a[j] == b[i + j]) {
                j++;
            } else {
                break;
            }
        }

        if (j == a.length()) {
            return true;
        }
    }

    return false;
}

int main() {
    string a, b;
    
    a = "kot";
    b = "alamakota";

    if (isSubstring(a, b)) {
        cout << a << " is substring of " << b << endl;
    } else {
        cout << a << " is not substring of " << b << endl;
    }

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/S5zJSH" %}
Naiwne wyszukiwanie wzorca w tekście
{% endembed %}

### Opis implementacji

TODO
