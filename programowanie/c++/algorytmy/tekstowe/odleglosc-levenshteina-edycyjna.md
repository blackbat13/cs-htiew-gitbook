# Odległość Levenshteina (edycyjna)

## Opis problemu

{% content-ref url="../../../../algorytmy/tekstowe/odleglosc-levenshteina-edycyjna.md" %}
[odleglosc-levenshteina-edycyjna.md](../../../../algorytmy/tekstowe/odleglosc-levenshteina-edycyjna.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

/// Computes Levenshtein distance (edit distance) between the two words
/// \param a - first word
/// \param b - second word
/// \return Levenshtein distance between a and b
int levenshteinDistance(string a, string b) {
    int matrix[a.length() + 1][b.length() + 1];
    int cost;
    
    for (int i = 0; i < a.length(); i++) {
        matrix[i][0] = i;
    }

    for (int i = 0; i < b.length(); i++) {
        matrix[0][i] = i;
    }

    for (int i = 1; i <= a.length(); i++) {
        for (int j = 1; j <= b.length(); j++) {
            if (a[i - 1] == b[j - 1]) {
                cost = 0;
            } else {
                cost = 1;
            }

            matrix[i][j] = min(matrix[i - 1][j - 1] + cost, min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1));
        }
    }

    return matrix[a.length()][b.length()];
}

int main() {
    string a, b;
    int distance;
    
    a = "kitten";
    b = "sitting";
    
    distance = levenshteinDistance(a, b);
    
    cout << "Levenshtein distance between words " << a << " and " << b << " is " << distance << endl;
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/xVUojF" %}
Odległość Levenshteina
{% endembed %}

### Opis implementacji

TODO
