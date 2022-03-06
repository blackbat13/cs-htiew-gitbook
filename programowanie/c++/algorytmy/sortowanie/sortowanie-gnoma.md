# Sortowanie gnoma

## Opis implementacji

{% content-ref url="../../../../algorytmy/sortowanie/sortowanie-gnoma.md" %}
[sortowanie-gnoma.md](../../../../algorytmy/sortowanie/sortowanie-gnoma.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

/// Sort array of specified length in ascending order
/// \param array - array to sort
/// \param n - length of the given array
void gnomeSort(int array[], int n) {
    int i = 0;
    while (i < n) {
        if (i == 0 || array[i] >= array[i - 1]) {
            i++;
        } else {
            swap(array[i], array[i - 1]);
            i--;
        }
    }
}

/// Prints given array
/// \param array - array to print
/// \param n - length of the given array
void printArray(int array[], int n) {
    for(int i = 0; i < n; ++i) {
        cout << array[i] << " ";
    }
 
    cout << endl;
}

int main() {
    int array[10] = {7, 3, 0, 1, 5, 2, 5, 19, 10, 5};
    int n = 10;
    
    gnomeSort(array, n);

    printArray(array, n);

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/3CxK1W" %}
Sortowanie gnoma
{% endembed %}