# Schemat Hornera

## Opis problemu

{% content-ref url="../../../../metody-numeryczne/schemat-hornera.md" %}
[schemat-hornera.md](../../../../metody-numeryczne/schemat-hornera.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>
using namespace std;

/// Compute value of the n-th degree polynomial for the given coefficients 
/// and x value using Horner method
/// \param coef - array of n+1 coefficients, where coef[i] is coefficient for the x^i
/// \param x 
/// \param n - degree of the polynomial
/// \return value of the polynomial
double hornerPolynomial(double coef[], double x, int n) {
    double result = 0;
    for(int i = n; i >= 0; i--) {
        result *= x;
        result += coef[i];
    }
    
    return result;
}

/// Prints given polynomial
/// \param coef - array of n+1 coefficients, where coef[i] is coefficient for the x^i
/// \param n - degree of the polynomial
void printPolynomial(double coef[], int n) {
    cout << "f(x) = " << coef[0];
    for(int i = 1; i <= n; i++) {
        cout << " + " << coef[i] << "x^" << i; 
    }
    
    cout << endl;
}

int main() {
    double coef[3] = {1, 2, 3};
    double x = 2;
    int n = 2;
    double result;
    
    printPolynomial(coef, n);
    result = hornerPolynomial(coef, x, n);
    cout << "f(" << x << ") = " << result << endl;
    
    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/b2FuJg" %}
Metoda Hornera obliczania wartości wielomianu
{% endembed %}

### Opis implementacji

Zacznijmy od funkcji pomocniczej `printPolynomial` (**linia 23**), której celem jest wyświetlenie wielomianu w czytelnej formie na ekranie. Nie jest ona niezbędną częścią algorytmu, ale może być pomocna przy weryfikacji poprawności wyniku. Funkcja przyjmuje dwa parametry: tablicę współczynników wielomianu `coef`, oraz stopień wielomianu `n`. W tablicy znajduje się dokładnie $$n+1$$** **liczb. Współczynniki są zapisane w kolejności od najmniejszej potęgi ( $$0$$ ) do największej ( $$n$$ ).

Na początku funkcji wypisujemy pierwszy współczynnik (**linia 24**). Następnie przechodzimy pętlą przez kolejne elementy tablicy (**linia 25**), wypisując współczynnik przy $$i$$-tej potędze przemnożony przez $$x$$ podniesione do potęgi $$i$$ .  

Przejdźmy teraz do właściwej implementacji algorytmu obliczania wartości wielomianu za pomocą schematu Hornera, czyli do funkcji `hornerPolynomial` (**linia 10**). Funkcja ta przyjmuje podobne parametry jak pomocnicza funkcja `printPolynomial`, ale ponadto przyjmuje także wartość $$x$$, którą mamy przyjąć podczas obliczeń. Współczynniki i stopień wielomianu podane są w takiej samej formie jak wcześniej.

Na początku tworzymy zmienną `result`, w której będziemy zapisywać wyniki obliczeń, i przypisujemy jej wartość $$0$$ (**linia 11**). Następnie przechodzimy pętlą przez kolejne współczynniki wielomianu, poczynając od współczynnika przy najwyższej potędze (**linia 12**). Zauważ, że korzystamy tutaj z pętli malejącej. W pętli wykonujemy dwie operacje: przemnażamy wynik dotychczasowych obliczeń przez wartość `x` **(linia 13**), a następnie dodajemy do wyniku wartość kolejnego współczynnika (**linia 14**). Po przejściu przez wszystkie współczynniki wystarczy zwrócić wynik obliczeń (**linia 17**).

W części głównej definiujemy wartości parametrów naszych obliczeń (**linie 33-35**), wypisujemy wielomian w czytelnej formie korzystając z pomocniczej funkcji `printPolynomial` (**linia 38**), obliczamy wartość wielomianu za pomocą funkcji `hornerPolynomial` (**linia 39**) i wypisujemy wynik na ekranie (**linia 40**).
