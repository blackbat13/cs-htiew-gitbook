# Sortowanie przez wybieranie

## Opis problemu

{% content-ref url="../../../../algorytmy/sortowanie/sortowanie-przez-wybieranie.md" %}
[sortowanie-przez-wybieranie.md](../../../../algorytmy/sortowanie/sortowanie-przez-wybieranie.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>
using namespace std;

/// Finds the minimum value in the specified range [from, to) and returns its index
/// \param array - array to search
/// \param from - beginning of range to search in, inclusive
/// \param to - end of range to search in, exclusive
int findMin(int array[], int from, int to) {
    int minValue = array[from], minIndex = from;
    for (int i = from + 1; i < to; i++) {
        if (array[i] < min_value) {
            minValue = array[i];
            minIndex = i;
        }
    }

    return minIndex;
}

/// Sorts array of specified length in ascending order
/// \param array - array to sort
/// \param n - length of the given array
void selectionSort(int array[], int n) {
    for(int i = 0; i < n; i++) {
        int minIndex = findMin(array, i, n);

        swap(array[i], array[minIndex]);
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
    
    selectionSort(array, 10);

    printArray(array, n);

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/aDJvwT" %}
Sortowanie przez wybieranie
{% endembed %}