# Sortowanie koktajlowe

## Opis problemu

{% content-ref url="../../../../algorytmy/sortowanie/sortowanie-koktajlowe.md" %}
[sortowanie-koktajlowe.md](../../../../algorytmy/sortowanie/sortowanie-koktajlowe.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

/// Sorts array in ascending order
/// \param array - array to sort
/// \param length - length of given array
void cocktailShakerSort(int array[], int n) {
    for (int i = 0; i <= n / 2; i++) {
        for (int j = i; j < n - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                swap(array[j], array[j + 1]);
            }
        }

        for (int j = n - 1 - i; j > i; j--) {
            if (array[j] < array[j - 1]) {
                swap(array[j], array[j - 1]);
            }
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
    
    cocktailShakerSort(array, n);
    
    printArray(array, n);

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/JvEapG" %}
Sortowanie koktajlowe
{% endembed %}

### Opis implementacji

TODO
