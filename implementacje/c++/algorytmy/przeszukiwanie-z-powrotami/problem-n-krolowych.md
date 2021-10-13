# Problem n królowych

## Opis problemu

{% content-ref url="../../../../przeszukiwanie-z-powrotami/problem-n-krolowych.md" %}
[problem-n-krolowych.md](../../../../przeszukiwanie-z-powrotami/problem-n-krolowych.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

bool checkNewPosition(int x, int y, int positions[]) {
    for (int i = 0; i < x; i++) {
        if (positions[i] == y) {
            return false;
        }
            
        if (y - positions[i] == x - i) {
            return false;
        }
    }
    
    return true;
}

bool findSolution(int n, int queenId, int positions[]) {
    if (queenId == n) {
        return true;
    }

    for (int i = 0; i < n; i++) {
        if (!checkNewPosition(queenId, i, positions)) {
            continue;
        }

        positions[queenId] = i;
        
        if (findSolution(n, queenId + 1, positions)) {
            return true;
        }
    }
    
    return false;
}

void printCheckboard(int n, int positions[]) {
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if (positions[i] == j) {
                cout << "1 ";
            } else {
                cout << "0 ";
            }
        }
        
        cout << endl;
    }
}
    
int main() {
    int n = 5;
    int positions[n];

    bool result = findSolution(n, 0, positions);

    if (result) {
        printCheckboard(n, positions);
    } else {
        cout << "No result exists" << endl;
    }
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/JzMsxF" %}
Problem n-królowych
{% endembed %}

### Opis implementacji

TODO
