# Najdłuższy spójny podciąg rosnący

## Opis problemu

{% content-ref url="../../../../algorytmy/wyszukiwanie/najdluzszy-spojny-podciag-rosnacy.md" %}
[najdluzszy-spojny-podciag-rosnacy.md](../../../../algorytmy/wyszukiwanie/najdluzszy-spojny-podciag-rosnacy.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

int longestGrowingSubstringLength(int n, int tab[]) {
    int mx = 1;
    int length = 1;
    
    for(int i = 1; i < n; i++) {
        if (tab[i] > tab[i-1]) {
            length += 1;
            if (length > mx) {
                mx = length;
            }
        } else {
            length = 1;
        }
    }
    
    return mx;
}

int main() {
    int tab[10] = {4, 9, 7, 2, 4, 7, 9, 3, 8, 6};
    int n = 10;

    int result = longestGrowingSubstringLength(n, tab);
    
    cout << result << endl;
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/aU2dQW" %}
Długość najdłuższego spójnego podciągu rosnącego
{% endembed %}

### Opis implementacji

TODO
