# Palindrom

## Opis problemu

{% content-ref url="../../../../tekstowe/palindrom.md" %}
[palindrom.md](../../../../tekstowe/palindrom.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>

using namespace std;

/// Check if given string is a palindrome
/// \param str - string to check
/// \return true if str is a palindrome, false otherwise
bool isPalindrome(string str) {
    string reversed = "";
    for (int i = 0; i < str.length(); i++) {
        reversed = str[i] + reversed;
    }

    return str == reversed;
}

int main() {
    string str;
    str = "kajak";

    if (isPalindrome(str)) {
        cout << str << " is a palindrome." << endl;
    } else {
        cout << str << " is not a palindrome." << endl;
    }

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/UUUAe6" %}
Test palindromu
{% endembed %}

### Opis implementacji

TODO

