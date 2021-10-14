# Anagramy

## Opis problemu

{% content-ref url="../../../../algorytmy/tekstowe/anagramy.md" %}
[anagramy.md](../../../../algorytmy/tekstowe/anagramy.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>
#include <algorithm>

using namespace std;

/// Check if two strings are anagrams
/// \param a - first string to check
/// \param b - second string to check
/// \return true if a and b are anagrams, false otherwise
bool areAnagrams(string a, string b) {
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    return a == b;
}

int main() {
    string a, b;
    
    a = "rokowanie";
    b = "korowanie";

    if (areAnagrams(a, b)) {
        cout << a << " and " << b << " are anagrams." << endl;
    } else {
        cout << a << " and " << b << " aren't anagrams." << endl;
    }

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/765IBp" %}
Test anagramów
{% endembed %}

### Opis implementacji

Funkcja `areAnagrams` (**linia 10**) sprawdza, czy dwa podane ciągi znaków są anagramami. Procedura jest prosta: najpierw sortujemy oba ciągi, wykorzystując do tego funkcję `sort` z biblioteki `algorithm` (**linie 11 i 12**). Następnie porównujemy posortowane ciągi znaków, zwracając w ten sposób wynik (**linia 13**).

W części głównej na początku definiujemy dane wejściowe (**linie 17-20**), a następnie wywołujemy funkcję `areAnagrams` (**linia 22**). W zależności od jej wyniku wypisujemy właściwy komunikat (**linie 23 i 25**).
