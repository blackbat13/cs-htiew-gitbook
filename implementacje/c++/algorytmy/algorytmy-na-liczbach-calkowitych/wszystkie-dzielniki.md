# Wszystkie dzielniki

## Opis problemu

{% content-ref url="../../../../algorytmy-na-liczbach-calkowitych/wszystkie-dzielniki.md" %}
[wszystkie-dzielniki.md](../../../../algorytmy-na-liczbach-calkowitych/wszystkie-dzielniki.md)
{% endcontent-ref %}

## Rozwiązanie zupełnie naiwne

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Prints all divisors of n
/// \param n - positive number
void divisors(int n) {
	for(int i = 1; i <= n; i++) {
		if(n % i == 0) {
			cout << i << endl;
		}
	}
}

int main() {
	int n = 12;
	
	divisors(n);
	
	return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/rRBAar" %}
Wszystkie dzielniki - podejście zupełnie naiwne
{% endembed %}

### Opis implementacji

Funkcja `divisors` (**linia 7**) wypisuje wszystkie dzielniki liczby podanej jako parametr. Na początku przechodzimy pętlą przez wszystkie potencjalne dzielniki od $$1$$ do $$n$$ włącznie (**linia 8**). W pętli sprawdzamy, czy reszta z dzielenia liczby $$n$$ i licznika pętli wynosi $$0$$ (**linia 9**), czyli czy n jest podzielne przez sprawdzaną wartość. Jeżeli tak jest, to znaleźliśmy dzielnik, więc go wypisujemy (**linia 10**).

W części głównej programu najpierw definiujemy dane wejściowe (**linia 16**), a następnie wywołujemy funkcję `divisors` (**linia 18**).

## Rozwiązanie naiwne

### Implementacja

```cpp
#include <iostream>

using namespace std;

/// Prints all divisors of n
/// \param n - positive number
void divisors(int n) {
	for (int i = 1; i <= n / 2; i++) {
		if (n % i == 0) {
			cout << i << endl;
		}
	}
	
	if (n > 1) {
		cout << n << endl;
	}
}

int main() {
	int n = 12;
	
	divisors(n);
	
	return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/SjvBS3" %}
Wszystkie dzielniki - podejście naiwne
{% endembed %}

### Opis implementacji

Funkcja `divisors` (**linia 7**) wypisuje wszystkie dzielniki liczby podanej jako parametr. Na początku przechodzimy pętlą przez wszystkie potencjalne dzielniki od $$1$$ do $$\lfloor n/2\rfloor$$ włącznie (**linia 8**). W pętli sprawdzamy, czy reszta z dzielenia liczby $$n$$ i licznika pętli wynosi $$0$$ (**linia 9**), czyli czy n jest podzielne przez sprawdzaną wartość. Jeżeli tak jest, to znaleźliśmy dzielnik, więc go wypisujemy (**linia 10**). Po wyjściu z pętli musimy jeszcze sprawdzić, czy $$n$$ jest większe od $$1$$ (**linia 14**). Jeżeli tak jest, to musimy wypisać jeszcze jeden dzielnik: $$n$$ (**linia 15**).

W części głównej programu najpierw definiujemy dane wejściowe (**linia 20**), a następnie wywołujemy funkcję `divisors` (**linia 22**).

## Rozwiązanie optymalne

### Implementacja

```cpp
#include <iostream>
#include <cmath>

using namespace std;

/// Prints all divisors of n
/// \param n - positive number
void divisors(int n) {
	for (int i = 1; i <= sqrt(n); i++) {
		if (n % i == 0) {
			cout << i << endl;
			if (i != n / i) {
				cout << n / i << endl;
			}
		}
	}
}

int main() {
	int n = 12;
	
	divisors(n);
	
	return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/tu3yX7" %}
Wszystkie dzielniki - podejście optymalne
{% endembed %}

### Opis implementacji

Funkcja `divisors` (**linia 7**) wypisuje wszystkie dzielniki liczby podanej jako parametr. Na początku przechodzimy pętlą przez wszystkie potencjalne dzielniki od $$1$$ do $$\sqrt{n}$$ włącznie (**linia 9**). W pętli sprawdzamy, czy reszta z dzielenia liczby $$n$$ i licznika pętli wynosi $$0$$ (**linia 10**), czyli czy n jest podzielne przez sprawdzaną wartość. Jeżeli tak jest, to znaleźliśmy dzielnik, więc go wypisujemy (**linia 11**). Po znalezieniu dzielnik musimy jeszcze sprawdzić, czy drugi dzielnik z "pary" jest różny od obecnego (**linia 12**). Jeżeli tak, to go też wypisujemy (**linia 13**).

W części głównej programu najpierw definiujemy dane wejściowe (**linia 20**), a następnie wywołujemy funkcję `divisors` (**linia 22**).
