# Operacje arytmetyczne

## Podstawowe

```cpp
#include <iostream>

using namespace std;

int main() {
    int a = 5;
    int b = 2;
    
    int suma = a + b;
    int roznica = a - b;
    int iloczyn = a * b;
    int iloraz = a / b;

    return 0;
}
```

{% hint style="danger" %}
**Uwaga**

Wynik dzielenia liczb całkowitych będzie także liczbą całkowitą, tzn. wartością zaokrągloną w dół.
{% endhint %}

### Dzielenie rzeczywiste

W celu uzyskania rzeczywistego wyniku dzielenia dwóch zmiennych typu całkowitego, należy użyć rzutowania na typ rzeczywisty.

```cpp
#include <iostream>

using namespace std;

int main() {
    int a = 5;
    int b = 2;
    
    double iloraz = (double)a / (double)b;

    return 0;
}
```

Wynik dzielenia liczb rzeczywistych jest także liczbą rzeczywistą:

```cpp
#include <iostream>

using namespace std;

int main() {
    double a = 5;
    double b = 2;
    
    double iloraz = a / b;

    return 0;
}
```

### Reszta z dzielenia

```cpp
#include <iostream>

using namespace std;

int main() {
    int a = 5;
    int b = 2;
    
    int reszta = a % b;

    return 0;
}
```
