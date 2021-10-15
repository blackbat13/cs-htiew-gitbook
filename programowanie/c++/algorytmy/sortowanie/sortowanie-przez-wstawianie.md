# Sortowanie przez wstawianie

## Opis problemu

{% content-ref url="../../../../algorytmy/sortowanie/sortowanie-przez-wstawianie.md" %}
[sortowanie-przez-wstawianie.md](../../../../algorytmy/sortowanie/sortowanie-przez-wstawianie.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

/// Sorts array of specified length in ascending order
/// \param array - array to sort
/// \param n - length of the given array
void insertionSort(int array[], int n) {
    for (int i = 1; i < n; i++) {
        int j = i;
        while (j > 0 && array[j] < array[j - 1]) {
            swap(array[j], array[j - 1]);
            j--;
        }
    }
}

/// Prints given array
/// \param array - array to print
/// \param n - length of the given array
void printArray(int array[], int n) {
    for(int i = 0; i < 10; ++i) {
        cout << array[i] << " ";
    }
 
    cout << endl;
}

int main() {
    int array[10] = {7, 3, 0, 1, 5, 2, 5, 19, 10, 5};
    int n = 10;
    
    insertionSort(array, n);

    printArray(array, n);

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/EGDR98" %}
Sortowanie przez wstawianie
{% endembed %}

### Opis implementacji

TODO
