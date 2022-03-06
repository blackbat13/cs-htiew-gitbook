# Sortowanie przez scalanie

## Opis problemu

{% content-ref url="../../../../algorytmy/sortowanie/sortowanie-przez-scalanie.md" %}
[sortowanie-przez-scalanie.md](../../../../algorytmy/sortowanie/sortowanie-przez-scalanie.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

/// Merge two sorted ascending part of array
///   [left, division) and [division, right)
/// Resulting merged array will also be sorted
void merge(int array[], int left, int right, int division) {
    int mergedLength = right - left;
    int merged[merged_length];
    int index1 = left;
    int index2 = division;

    for(int i = 0; i < mergedLength ; i++) {
        if(index1 >= division) {
            merged[i] = array[index2];
            index2++;
        } else if(index2 >= right) {
            merged[i] = array[index1];
            index1++;
        } else if(array[index1] <= array[index2]) {
            merged[i] = array[index1];
            index1++;
        } else {
            merged[i] = array[index2];
            index2++;
        }
    }

    for(int i = left; i < right; i++) {
        array[i] = merged[i-left];
    }
}

/// Sort ascending array in range [left, right)
void mergeSort(int array[], int left, int right) {
    if(right - left <= 1) {
        return;
    }

    int division = (left + right)/2;
    mergeSort(array, left, division);
    mergeSort(array, division, right);

    merge(array, left, right, division);
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
    
    mergeSort(array, 0, n);

    printArray(array, n);

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/1Pv3RF" %}
Sortowanie przez scalanie
{% endembed %}