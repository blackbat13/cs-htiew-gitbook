# Kod ASCII

## Opis problemu

{% content-ref url="../../../../kompresja/kod-ascii.md" %}
[kod-ascii.md](../../../../kompresja/kod-ascii.md)
{% endcontent-ref %}

## Podstawowa tablica ASCII

### Implementacja

```cpp
#include <iostream>
using namespace std;

int main() {
    char c;
    
    for(int i = 0; i <= 127; i++) {
        c = (char)i;
        cout << i << " = " << c << endl;
    }
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/fnVCCi" %}
Podstawowa tablica ASCII
{% endembed %}

### Opis implementacji

TODO

## Rozszerzona tablica ASCII

### Implementacja

```cpp
#include <iostream>
using namespace std;

int main() {
    unsigned char c;
    
    for(int i = 0; i <= 255; i++) {
        c = (unsigned char)i;
        cout << i << " = " << c << endl;
    }
    
    return 0;
}
```

### Opis implementacji

TODO
