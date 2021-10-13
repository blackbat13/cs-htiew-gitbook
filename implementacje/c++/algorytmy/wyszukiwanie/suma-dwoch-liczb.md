# Suma dwóch liczb

## Opis problemu

{% content-ref url="../../../../wyszukiwanie/suma-dwoch-liczb.md" %}
[suma-dwoch-liczb.md](../../../../wyszukiwanie/suma-dwoch-liczb.md)
{% endcontent-ref %}

## Rozwiązanie naiwne

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Finds and prints two numbers from the array that give a specified sum
/// or prints -1 if no such numbers exists
/// \param n - number of elements in the array
/// \param tab - array of n elements sorted in ascending order
/// \param sum - the sum we are searching for
void sumOfTwoNaive(int n, int tab[], int sum) {
    for(int i = 0; i < n; i++) {
        for(int j = i+1; j < n; j++) {
            if(tab[i] + tab[j] == sum) {
                cout << tab[i] << ", " << tab[j] << endl;
                return;
            }
        }
    }
    
    cout << -1 << endl;
}

int main() {
    int n = 10;
    int tab[10] = {1, 2, 4, 6, 8, 9, 10, 12, 13, 15};
    int sum = 18;

    sumOfTwoNaive(n, tab, sum);

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/dHf2jV" %}
Suma dwóch - rozwiązanie naiwne
{% endembed %}

### Opis implementacji

TODO

## Rozwiązanie optymalne

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Finds and prints two numbers from the array that give a specified sum
/// or prints -1 if no such numbers exists
/// \param n - number of elements in the array
/// \param tab - array of n elements sorted in ascending order
/// \param sum - the sum we are searching for
void sumOfTwoOptimal(int n, int tab[], int sum) {
    int left = 0;
    int right = n-1;

    while(left < right && tab[left] + tab[right] != sum) {
        if(tab[left] + tab[right] < sum) {
            left++;
        } else {
            right--;
        }
    }

    if(left < right) {
        cout << tab[left] << ", " << tab[right] << endl;
    } else {
        cout << -1 << endl;
    }
}

int main() {
    int n = 10;
    int tab[10] = {1, 2, 4, 6, 8, 9, 10, 12, 13, 15};
    int sum = 18;

    sumOfTwoOptimal(n, tab, sum);
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/QuNr8P" %}
Suma dwóch - rozwiązanie optymalne
{% endembed %}

### Opis implementacji

TODO
