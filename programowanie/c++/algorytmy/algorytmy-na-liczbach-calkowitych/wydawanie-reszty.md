# Wydawanie reszty

## Opis problemu

{% content-ref url="../../../../algorytmy/algorytmy-na-liczbach-calkowitych/atm-problem/README.md" %}
[README.md](../../../../algorytmy/algorytmy-na-liczbach-calkowitych/atm-problem/README.md)
{% endcontent-ref %}

## Podejście zachłanne

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Get minimal number of coins used to give out amount using greedy algorithm
/// \param amount - amount to give out
/// \param coins - array of available coins, sorted in descending order
/// \return minimum number of coins from array coins used to give out amount
int changeGreedy(int amount, int coins[]) {
    int result = 0;
    int i = 0;

    while (amount > 0) {
        result += amount / coins[i];
        amount %= coins[i];
        i++;
    }

    return result;
}

int main() {
    int amount, result;
    int coins[8] = {200, 100, 50, 20, 10, 5, 2, 1};
    amount = 589;
    
    result = changeGreedy(amount, coins);

    cout << "Algorytm zachlanny" << endl;
    cout << "Kwota " << amount << " moze zostac wydana przy uzyciu " << result << " monet/banknotow." << endl;

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/PQmCHG" %}
Zachłanne wydawanie reszty
{% endembed %}

### Opis implementacji

TODO

## Podejście dynamiczne

### Implementacja

```cpp
#include <iostream>
using namespace std;

/// Prints coins used in dynamic algorithm
void printUsedCoins(int usedCoins[], int amount) {
	while (amount > 0) {
        cout << usedCoins[amount] << " ";
        amount -= usedCoins[amount];
    }

    cout << endl;
}

/// Get minimal number of coins used to give out amount using dynamic algorithm
/// \param amount - amount to give out
void changeDynamic(int amount, int numberOfCoins, int coins[]) {
    int partialResults[amount + 1];
    int usedCoins[amount + 1];
    int coinValue;
    int infinity = 1000000;
    
    partialResults[0] = 0;
    
    for (int i = 1; i <= amount; i++) {
        partialResults[i] = infinity;
    }

    for (int j = 0; j < numberOfCoins; j++) {
        coinValue = coins[j];
        for (int i = 0; i <= amount - coinValue; i++) {
            if (partialResults[i] + 1 < partialResults[i + coinValue]) {
                partialResults[i + coinValue] = partialResults[i] + 1;
                usedCoins[i + coinValue] = coinValue;
            }
        }
    }

    if (partialResults[amount] == infinity) {
        cout << "Cannot give out specified value using given coins." << endl;
        return;
    }

    cout << "Amount " << amount << " can be given out using " << partialResults[amount] << " coins." << endl;
    cout << "Used coins: ";
    
    printUsedCoins(usedCoins, amount);
}

int main() {
    int amount, numberOfCoins;
    int coins[5] = {1, 2, 7, 10};
    numberOfCoins = 5;
    amount = 14;

    cout << "Dynamic algorithm" << endl;
    changeDynamic(amount, numberOfCoins, coins);

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/49zMho" %}
Wydawanie reszty - podejście dynamiczne
{% endembed %}

### Opis implementacji

TODO

