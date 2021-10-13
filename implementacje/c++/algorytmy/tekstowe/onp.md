---
description: Obliczanie wartości wyrażenia ONP
---

# ONP

## Opis problemu

{% content-ref url="../../../../tekstowe/odwrotna-notacja-polska.md" %}
[odwrotna-notacja-polska.md](../../../../tekstowe/odwrotna-notacja-polska.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>
#include <stack>

using namespace std;

/// Computes result of "a op b" where op is +, -, * or /
/// \param a - first number
/// \param b - second number
/// \param op - operator
/// \return result of "a op b"
double compute(double a, double b, char op) {
    switch(op) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        case '/':
            return a / b;
    }
}

/// Calculate the value of a given Reverse Polish Notation string
/// \param rpn - string containing the Reverse Polish Notation, we assume that it's correct
/// \return value of Reverse Polish Notation
double calculateRPN(string rpn) {
    stack<double> rpnStack;
    double a, b, result;

    for (int i = 0; i < rpn.length(); i++) {
        if (isdigit(rpn[i])) {
            rpnStack.push(rpn[i] - '0');
        } else {
            b = rpnStack.top();
            rpnStack.pop();
            a = rpnStack.top();
            rpnStack.pop();
            
            result = compute(a, b, rpn[i])
            rpnStack.push(result);
        }
    }

    return rpnStack.top();
}

int main() {
    string rpn;
    double result;
    
    rpn = "27+3/13-4*+2/";
    
    result = calculateRpn(rpn);

    cout << "Value of rpn string " << rpn << " is: " << calculateRpn(rpn) << endl;

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/BXv5Qf" %}
Obliczanie wartości wyrażenia ONP
{% endembed %}

### Opis implementacji

Funkcja `calculateRPN` (**linia 27**) oblicza wartość wyrażenia ONP podanego w formie ciągu znaków. Zakładamy, że podane wyrażenie jest poprawne, a każdy znak reprezentuje jednocyfrową liczbę lub operację. 

Na początku tworzymy stos do przechowywania wyników kolejnych obliczeń (**linia 28**), oraz pomocnicze zmienne do przechowywania bieżących wartości ze stosu oraz wyniku pośrednich operacji (**linia 29**). 

Następnie przechodzimy pętlą po każdym znaku wyrażenia ONP (**linia 31**). Jeżeli przetwarzany aktualnie znak jest cyfrą (**linia 32**), to dodajemy jego liczbową wartość na stos (**linia 33**). W przeciwnym przypadku mamy do czynienia z operatorem. Pobieramy więc dwie ostatnie wartości ze stosu, zarazem je z niego usuwając (**linie 35-38**). Następnie korzystamy z pomocniczej funkcji `compute` by obliczyć wynik operacji (linia 40), który następnie wrzucamy na stos (**linia 41**).

Po przetworzeniu wszystkich znaków z wyrażenia ONP na stosie powinna zostać dokładnie jedna wartość, którą zwracamy jako wynik funkcji (**linia 45**).
