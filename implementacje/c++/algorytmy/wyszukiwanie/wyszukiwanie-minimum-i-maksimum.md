# Wyszukiwanie minimum i maksimum

## Opis problemu

{% content-ref url="../../../../algorytmy/wyszukiwanie/wyszukiwanie-maksimum.md" %}
[wyszukiwanie-maksimum.md](../../../../algorytmy/wyszukiwanie/wyszukiwanie-maksimum.md)
{% endcontent-ref %}

## Wyszukiwanie wartości minimum i maksimum

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Finds minimum value in array
/// \param n - size of the array
/// \param tab - array
/// \return minimum value in tab
int findMin(int n, int tab[]) {
    int min = tab[0];
    
    for(int i = 1; i < n; i++) {
        if(tab[i] < min) {
            min = tab[i];
        }
    }
    
    return min;
}

/// Finds maximum value in array
/// \param n - size of the array
/// \param tab - array
/// \return maximum value in tab
int findMax(int n, int tab[]) {
    int max = tab[0];
    
    for(int i = 1; i < n; i++) {
        if(tab[i] > max) {
            max = tab[i];
        }
    }
    
    return max;
}

int main() {
    int tab[10] = {8, 2, 9, 10, 5, 4, 2, 7, 18, 0};
    int n = 10;
    
    int min = findMin(n, tab);
    int max = findMax(n, tab);
    
    cout << "Min: " << min << endl;
    cout << "Max: " << max << endl;
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/kIt9au" %}
Znajdowanie wartości min i maks
{% endembed %}

### Opis implementacji

TODO

## Wyszukiwanie indeksów wartości minimum i maksimum

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Finds index of the minimum value in array
/// \param n - size of the array
/// \param tab - array
/// \return index of the minimum value in tab
int findMinIndex(int n, int tab[]) {
    int minInd = 0;
    
    for(int i = 1; i < n; i++) {
        if(tab[i] < tab[minInd]) {
            minInd = i;
        }
    }
    
    return minInd;
}

/// Finds index of the maximum value in array
/// \param n - size of the array
/// \param tab - array
/// \return index of the maximum value in tab
int findMaxIndex(int n, int tab[]) {
    int maxInd = 0;
    
    for(int i = 1; i < n; i++) {
        if(tab[i] > tab[maxInd]) {
            maxInd = i;
        }
    }
    
    return maxInd;
}

int main() {
    int tab[10] = {8, 2, 9, 10, 5, 4, 2, 7, 18, 0};
    int n = 10;
    
    int minInd = findMinIndex(n, tab);
    int maxInd = findMaxIndex(n, tab);
    
    cout << "Min Index: " << minInd << endl;
    cout << "Max Index: " << maxInd << endl;
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/YHUIyv" %}
Wyszukiwanie indeksów wartości min i maks
{% endembed %}

### Opis implementacji

TODO
