# Wyznacznik macierzy 3x3

## Opis problemu

{% content-ref url="../../../../macierze/wyznacznik-macierzy-3x3.md" %}
[wyznacznik-macierzy-3x3.md](../../../../macierze/wyznacznik-macierzy-3x3.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;


int det3(int matrix[3][3]) {
    return matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[1][0] * matrix[2][1] * matrix[0][2] + matrix[2][0] * \
           matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1] * matrix[2][0] - matrix[0][1] * matrix[1][0] * \
           matrix[2][2] - matrix[0][0] * matrix[1][2] * matrix[2][1];
}

int main() {
    int matrix[3][3] = {
                        {1, 2, 3}, 
                        {4, 5, 6}, 
                        {7, 8, 9}};
       
    int result = det3(matrix);

    cout << result << endl;
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/3XInAf" %}

### Opis implementacji

TODO
