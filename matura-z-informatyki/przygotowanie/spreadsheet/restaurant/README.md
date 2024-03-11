# Restauracja

W pliku *restaurant.txt* znajdują się dane o zamówieniach pewnej restauracji z 2023 roku. Każda linia zawiera dane jednego zamówienia:

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

Znajdź, które godziny są najbardziej popularne wśród klientów, analizując czas zamówień. Wykonaj wykres prezentujący liczby zamówień dokonanych w każdej godzinie.

O godzinie 10 złożonych zostało 80 zamówień.

## Zadanie 3

Oblicz, ile zamówień zostało dokonanych w weekend (sobota-niedziela), a ile w dni robocze.

Dla pierwszych 10 zamówień z pliku, cztery zostały dokonane w weekend.

## Zadanie 4

Dla każdego miesiąca policz liczbę zamówień w następujących przedziałach cenowych: poniżej 50,00 zł, od 50,00 do 100,00 zł, od 100,01 do 150,00 zł i powyżej 150,00 zł. Dane przedstaw na wykresie.

Wynik dla stycznia:

| **Miesiąc** | **Liczba zamówień poniżej 50,00 zł** | **Liczba zamówień od 50,00 do   100,00 zł** | **Liczba zamówień od 100,01 do   150,00 zł** | **Liczba zamówień powyżej 150,00   zł** |
|:-----------:|:------------------------------------:|:-------------------------------------------:|:--------------------------------------------:|:---------------------------------------:|
|     styczeń     |                  $$20$$                  |                      $$19$$                     |                      $$16$$                      |                    $$17$$                   |

## Zadanie 5

Zbadaj, które kombinacje zamówień (np. napój ciepły + danie główne, przystawka + deser) są najpopularniejsze, tzn. były najczęściej zamawiane. Jeżeli jest kilka takich kombinacji, to podaj wszystkie.
