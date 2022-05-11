# C++

## Implementacja

```cpp
#include <cstdio>
#include <iostream>
#include <set>

using namespace std;

int main() {
    int n, crd;
    set<int> cards;
    int result = 0;

    scanf("%d", &n); 

    for (int i = 0; i < n; i++) {
        scanf("%d", &crd);
        cards.insert(crd);
    };

    for(auto el: cards) {
        result = max(result, el - result);
    }

    printf("%d\n", result);
    
    return 0;
}
```