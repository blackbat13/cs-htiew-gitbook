# Sortowanie szybkie

## Opis problemu

{% content-ref url="../../../../sortowanie/sortowanie-szybkie.md" %}
[sortowanie-szybkie.md](../../../../sortowanie/sortowanie-szybkie.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

/// Sorts the array using quick sort algorithm
/// \param tab- array to sort
/// \param left - beginning of range to sort, inclusive
/// \param right - end of range to sort, inclusive
void quickSort(int tab[], int left, int right) {
    if (right <= left) {
        return;
    }

    int pivot = tab[(left + right) / 2];
    int i = left, j = right;
    while (i <= j) {
        while (tab[i] < pivot) {
            i++;
        }

        while (pivot < tab[j]) {
            j--;
        }

        if (i > j) {
            break;
        }

        swap(tab[i], tab[j]);

        i++;
        j--;
    }

    quickSort(tab, left, j);
    quickSort(tab, i, right);
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
    int tab[10] = {7, 2, -2, 7, 7, 293, 1, 5, 94, -5};
    int n = 10;
    
    quickSort(tab, 0, n - 1);
     
    printArray(tab, n);
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/W2ZQsj" %}
Sortowanie szybkie
{% endembed %}

### Opis implementacji

TODO
