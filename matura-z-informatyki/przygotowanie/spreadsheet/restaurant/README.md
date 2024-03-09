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

## Zadanie 2

Wykorzystując dane o zamówieniach, oblicz łączne przychody restauracji z każdej kategorii menu oraz całkowite przychody ze wszystkich zamówień. 

## Zadanie 3

Znajdź, które godziny są najbardziej popularne wśród klientów, analizując czas zamówień. Wykonaj wykres prezentujący liczby zamówień dokonanych w każdej godzinie.

## Zadanie 4

Oblicz, ile zamówień zostało dokonanych w weekend (sobota-niedziela), a ile w dni robocze.

## Zadanie 5

Oblicz średnią wartość zamówienia z każdej kategorii dań dla każdego stolika. 

## Zadanie 6

Dla każdego miesiąca policz liczbę zamówień w następujących przedziałach cenowych: poniżej 50,00 zł, od 50,00 do 100,00 zł, od 100,01 do 150,00 zł i powyżej 150,00 zł. Dane przedstaw na wykresie.

## Zadanie 7

Zbadaj, które kombinacje zamówień (np. napój ciepły + danie główne, przystawka + deser) są najpopularniejsze, tzn. były najczęściej zamawiane. Jeżeli jest kilka takich kombinacji, to podaj wszystkie.
