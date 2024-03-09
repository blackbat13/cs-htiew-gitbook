# Restauracja

W pliku *restaurant.txt* znajdują się dane o zamówieniach pewnej restauracji. Każda linia zawiera dane jednego zamówienia:

- numer stolika: liczba naturalna od 1 do 10
- kwota zamówienia: liczba rzeczywista z dokładnością do 2 miejsc po przecinku
- rodzaj zamówienia: liczba naturalna od 1 do 31 opisana poniżej
- data zamówienia
- czas zamówienia

Dane są rodzielone średnikami. Pierwszy wiersz pliku zawiera nazwy kolumn.

{% file src="../../../../.gitbook/assets/restaurant/restaurant.txt" %}
restaurant.txt
{% endfile %}

Rodzaj zamówienia zakodowany jest za pomocą liczby naturalnej. Zapis binarny tej liczby na 5 bitach zawiera informacje o tym, co zostało zamówione. Jedynka na danym miejscu oznacza, że została zamówiona pozycja z menu odpowiadająca danemu miejscu. Idąc od bitu najmniej znaczącego, kolejne pozycje odpowiadają następującym kategoriom:

- napój ciepły
- napój zimny
- przystawka
- danie główne
- deser

{% hint style="info" %}
**Przykład**

Liczba $$10$$ zapisana na pięciu bitach to: $$01001$$

Co oznacza to, że zostały zamówione:

- pozycja 1 (napój ciepły)
- pozycja 4 (danie główne)
{% endhint %}

# Zadanie 1

Policz ile łącznie zostało zamówionych dań z poszczególnych kategorii (napój ciepły, napój zimny, przystawka, danie główne, deser).

Dla pierwszych 100 wierszy wynik to:

|      **Rodzaj**     | **Napój ciepły** | **Napój zimny** | **Przystawka** | **Danie główne** | **Deser** |
|:-------------------:|:----------------:|:---------------:|:--------------:|:----------------:|:---------:|
| **Liczba zamówień** |        $$49$$        |        $$59$$       |       $$48$$       |        $$56$$        |     $$50$$    |

