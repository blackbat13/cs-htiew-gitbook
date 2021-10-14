# Znajdowanie lidera w zbiorze

## Opis problemu

{% content-ref url="../../../../algorytmy/wyszukiwanie/znajdowanie-lidera-w-zbiorze.md" %}
[znajdowanie-lidera-w-zbiorze.md](../../../../algorytmy/wyszukiwanie/znajdowanie-lidera-w-zbiorze.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

/// Find majority element, if exist
/// \param array - array to search in
/// \param length - length of array
/// \return majority element in given array, if there is a majority
int findLeader(int array[], int length) {
    int currentCandidate, counter;
    counter = 0;
    
    for (int i = 0; i < length; i++) {
        if (counter == 0) {
            currentCandidate = array[i];
            counter = 1;
        } else {
            if (array[i] == currentCandidate) {
                counter++;
            } else {
                counter--;
            }
        }
    }

    return currentCandidate;
}

int main() {
    int array[10] = {1, 2, 5, 5, 7, 5, 5, 10, 5, 5};
    int majority;

    majority = findLeader(array, 10);
    cout << "Majority element is: " << majority << endl;

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/oeuyQq" %}
Znajdowanie lidera w zbiorze
{% endembed %}

### Opis implementacji

TODO
