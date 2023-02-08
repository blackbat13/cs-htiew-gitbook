# Wydawanie reszty

## Opis problemu

{% content-ref url="../../../../algorithms/integers/atm-problem/README.md" %}
[README.md](../../../../algorithms/integers/atm-problem/README.md)
{% endcontent-ref %}

## Podejście zachłanne

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def change_greedy(amount: int, coins: []) -> int:
    result = 0
    i = 0
    
    while amount > 0:
        result += int(amount / coins[i])
        amount %= coins[i]
        i += 1

    return result


coins = [200, 100, 50, 20, 10, 5, 2, 1]
amount = 589

result = change_greedy(amount, coins)

print("Greedy algorithm")
print(f"Amount {amount} can be given out using {result} coins")
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/DQPy9c" %}
Wydawanie reszty - podejście zachłanne
{% endembed %}

## Podejście dynamiczne

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def change_dynamic(amount: int, coins: []) -> None:
    partial_results = []
    used_coins = []
    infinity = 10000000

    for i in range(0, amount + 1):
        partial_results.append(infinity)
        used_coins.append(infinity)

    partial_results[0] = 0

    for coin_value in coins:
        for i in range(0, amount - coin_value + 1):
            if partial_results[i] + 1 < partial_results[i + coin_value]:
                partial_results[i + coin_value] = partial_results[i] + 1
                used_coins[i + coin_value] = coin_value

    if partial_results[amount] == infinity:
        print("Cannot give out specified value using given coins")
        return

    print(f"Amount {amount} can be given out using {partial_results[amount]} coins")
    print("Used coins:")
    
    i = amount
    while i > 0:
        print(used_coins[i])
        i -= used_coins[i]


coins = [1, 2, 7, 10]
amount = 14

print("Dynamic algorithm")
change_dynamic(amount, coins)
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/piFFpG" %}
Wydawanie reszty - podejście dynamiczne
{% endembed %}

### Opis implementacji

Funkcja `change_dynamic` (**linia 1**) przyjmuje dwa parametry: kwotę do wydania (`amount`) i listę dostępnych nominałów (`coins`).

Na początku funkcji przygotowujemy stosowne listy do przechowywania wartości częściowych wyników (**linia 2**) i wykorzystanych nominałów (**linia 3**). Tworzymy także pomocniczą zmienną `infinity`, do której przypisujemy odpowiednio dużą wartość liczbową, którą będziemy traktować jako nieskończoność (**linia 4**).

W linii **14** przechodzimy pętlą przez wszystkie nominały, które są wczytywane od użytkownika w linii **15**. 

Dla każdego nominału przechodzimy przez odpowiednie pola tablicy (linia **16**). W zależności od wartości pola, dokonujemy zmiany (linie **17-19**).

Jeżeli po przetworzeniu wszystkich nominałów ostatnie pole tablicy wciąż ma wartość równą zmiennej `infinity` (linia **21**), to wypisujemy odpowiedni komunikat o braku możliwości wydania podanej kwoty i kończymy działanie funkcji.
