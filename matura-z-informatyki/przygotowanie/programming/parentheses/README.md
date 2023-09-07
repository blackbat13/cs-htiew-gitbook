# Nawiasy

Dany jest ciąg złożony z nawiasów okrągłych (), kwadratowych [] oraz klamrowych {}. Ciąg nawiasów nazwiemy **poprawnym**, gdy:

* jest pustym ciągiem,
* jeżeli $$A$$ i $$B$$ są poprawne, to $$AB$$ także jest poprawne,
* jeżeli $$A$$ jest poprawne, to $$(A)$$, $$[A]$$ oraz $$\{A\}$$ także są poprawne.

W pliku *parentheses.txt* znajduje się $$100$$ ciągów nawiasów, jak opisano powyżej, każdy zapisany w osobnym wierszu.

{% file src="../../../../.gitbook/assets/parentheses.txt" %}
parentheses.txt
{% endfile %}

Napisz program/programy rozwiązujące poniższe zadania.

## Zadanie 1

Podaj, ile ciągów nawiasów w pliku jest **poprawnych**.

## Zadanie 2

Wypisz ciągi nawiasów z pliku posortowane niemalejąco pod względem trzech kryteriów (jednocześnie, priorytet kryterium zgodny z kolejnością): liczby nawiasów okrągłych, liczby nawiasów kwadratowych oraz liczby nawiasów klamrowych. 

## Zadanie 3

Dla każdego ciągu nawiasów w pliku, podaj długość najdłuższego spójnego podciągu nawiasów otwierających oraz długość najdłuższego spójnego podciągu nawiasów zamykających.
