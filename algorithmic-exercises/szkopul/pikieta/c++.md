# C++

## Implementacja

```cpp
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

int main() {
    int n;
    unsigned long long int result, div, number;
    unsigned long long int allFactors[50005] = {};
    vector<unsigned long long int> currentFactors;
    
    scanf("%d", &n);

    for(int i = 0; i < n; i++) {
        scanf("%llu", &number);
        div = 2;
        currentFactors.clear();
        while(number > 1) {
            while(number % div == 0) {
                number /= div;
                currentFactors.push_back(div);
            }

            div++;
        }

        for(int j = 0; j < currentFactors.size(); j++) {
            if(allFactors[currentFactors[j]] > 0) {
                allFactors[currentFactors[j]]--;
            }
        }

        for(int j = 0; j < currentFactors.size(); j++) {
            allFactors[currentFactors[j]]++;
        }
    }

    result = 1;

    for(int i = 0; i <= 50000; i++) {
        result *= (allFactors[i] + 1);
        result %= 12345678;
    }

    if (result < n) {
        result += 12345678;
    }
    
    result -= n;        

    result %= 12345678;

    printf("%llu\n", result);
    
    return 0;
}
```