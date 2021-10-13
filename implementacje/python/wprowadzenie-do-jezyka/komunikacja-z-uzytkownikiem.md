---
description: Obsługa wejścia i wyjścia
---

# Komunikacja z użytkownikiem

## Wyjście

Wypisanie prostego komunikatu:

```python
print("Witaj Świecie!")
```

## Wejście

Wczytanie tekstu:

```python
imie = input("Podaj swoje imie: ")
```

 Jak widać na powyższym przykładzie, do wczytania tekstu od użytkownika służy funkcja `input()`. Do funkcji możemy przekazać opcjonalny parametr: tekst, jaki zostanie wyświetlony użytkownikowi. Jako wynik funkcja zwraca całą linię tekstu wczytaną z wejścia.

 Za pomocą funkcji `input()` możemy wczytać linię tekstu z konsoli. Jeżeli chcemy, aby użytkownik podał nam liczbę, to nie możemy tego co prawda wymusić, ale możemy przetworzyć wczytany tekst na liczbę za pomocą funkcji `int()`.

Wczytanie liczby:

```python
wiek = int(input("Podaj swój wiek: "))
```
