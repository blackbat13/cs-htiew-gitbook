# Najdłuższy wspólny podciąg

## Opis problemu

{% content-ref url="../../../../tekstowe/najdluzszy-wspolny-podciag.md" %}
[najdluzszy-wspolny-podciag.md](../../../../tekstowe/najdluzszy-wspolny-podciag.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

/// Find longest common subsequence of two strings
/// \param a - first string
/// \param b - second string
/// \return longest common subsequence of a and b
string longestCommonSubsequence(string a, string b) {
    int matrix[a.length() + 1][b.length() + 1];
    int value, i, j;
    string result = "";
    
    for (i = 0; i <= a.length(); i++) {
        matrix[i][0] = 0;
    }

    for (i = 0; i <= b.length(); i++) {
        matrix[0][i] = 0;
    }

    for (i = 1; i <= a.length(); i++) {
        for (j = 1; j <= b.length(); j++) {
            if (a[i - 1] == b[j - 1]) {
                matrix[i][j] = matrix[i - 1][j - 1] + 1;
            } else {
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1]);
            }
        }
    }

    value = matrix[a.length()][b.length()];
    i = a.length();
    j = b.length();
    
    while (value > 0) {
        if (matrix[i - 1][j] == value) {
            i--;
        } else if (matrix[i][j - 1] == value) {
            j--;
        } else {
            result = a[i - 1] + result;
            i--;
            j--;
            value--;
        }
    }

    return result;
}

int main() {
    string a, b, lcs;
    
    a = "kitten";
    b = "sitting";
    
    lcs = longestCommonSubsequence(a, b);
    
    cout << "Longest common subsequence of words " << a << " and " << b << " is " << lcs << endl;
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/ER5KsX" %}
Najdłuższy wspólny podciąg
{% endembed %}

### Opis implementacji

TODO
