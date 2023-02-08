# Wyszukiwanie binarne

## Opis problemu

{% content-ref url="../../../../algorithms/searching/binary-search.md" %}
[binary-search.md](../../../../algorithms/searching/binary-search.md)
{% endcontent-ref %}

## Wersja iteracyjna

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```cpp
#include <iostream>

using namespace std;

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
    
    int index = binarySearchIterative(array, 10, number);
    
    if (index == -1) {
        cout << "Number not found in array" << endl;
    } else {
        cout << "Index of given number is " << index << endl;
    }

    return 0;
}
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/l5xQXm" %}
Wyszukiwanie binarne - wersja iteracyjna
{% endembed %}

## Wersja rekurencyjna

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```cpp
#include <iostream>

using namespace std;

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
    
    int index = binarySearchRecursive(array, number, 0, 10);
    
    if (index == -1) {
        cout << "Number not found in array" << endl;
    } else {
        cout << "Index of given number is " << index << endl;
    }

    return 0;
}
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/c250gS" %}
Wyszukiwanie binarne - wersja rekurencyjna
{% endembed %}
