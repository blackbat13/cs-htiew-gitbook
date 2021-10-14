# Wyszukiwanie binarne

## Opis problemu

{% content-ref url="../../../../algorytmy/wyszukiwanie/wyszukiwanie-binarne.md" %}
[wyszukiwanie-binarne.md](../../../../algorytmy/wyszukiwanie/wyszukiwanie-binarne.md)
{% endcontent-ref %}

## Wersja iteracyjna

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Perform iterative binary search on given array
/// \param array - array to search in, sorted ascending
/// \param length - length of array
/// \param number - element to find
/// \return index of element in array, or -1 if not found
int binarySearchIterative(int array[], int length, int number) {
    int left = 0;
    int right = length - 1;
    int middle;

    while (left < right) {
        middle = (left + right) / 2;
        if (number <= array[middle]) {
            right = middle;
        } else {
            left = middle + 1;
        }
    }

    if (array[left] == number) {
        return left;
    }

    return -1;
}

int main() {
    int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int number = 8;
    int index;
    
    index = binarySearchIterative(array, 10, number);
    
    if (index == -1) {
        cout << "Number not found in array" << endl;
    } else {
        cout << "Index of given number is " << index << endl;
    }

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/l5xQXm" %}
Wyszukiwanie binarne - wersja iteracyjna
{% endembed %}

### Opis implementacji

TODO

## Wersja rekurencyjna

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Perform recursive binary search on given array
/// \param array - array to search in, sorted ascending
/// \param number - element to find
/// \param left
/// \param right
/// \return index of element in array, or -1 if not found
int binarySearchRecursive(int array[], int number, int left, int right) {
    int middle;

    if (left < right) {
        middle = (left + right) / 2;
        if (number <= array[middle]) {
            return binarySearchRecursive(array, number, left, middle);
        } else {
            return binarySearchRecursive(array, number, middle + 1, right);
        }
    } else if (array[left] == number) {
        return left;
    }

    return -1;
}

int main() {
    int array[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int number = 8;
    int index;
    
    index = binarySearchRecursive(array, number, 0, 10);
    
    if (index == -1) {
        cout << "Number not found in array" << endl;
    } else {
        cout << "Index of given number is " << index << endl;
    }

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/c250gS" %}
Wyszukiwanie binarne - wersja rekurencyjna
{% endembed %}

### Opis implementacji

TODO
