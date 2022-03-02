# Obsługa wejścia i wyjścia

## Wyjście

Wypisanie prostego komunikatu:

```python
print("Witaj Świecie!")
```

### Tekst formatowany

Gdy chcemy w komunikacie umieścić wartości zmiennych, najłatwiej jest to zrobić używając tekstu formatowanego.
W tym celu przed cudzysłowem umieszczamy literę `f`, a w samym tekście używamy nawiasów klamrowych w miejscach, gdzie chcemy wstawić wartości zmiennych.

#### Przykład

```python
temp = 10

print(f"Dzisiaj jest {temp} stopni Celsjusza")
```

## Wejście

### Wczytanie tekstu 

```python
imie = input("Podaj swoje imie: ")
```

Jak widać na powyższym przykładzie, do wczytania tekstu od użytkownika służy funkcja `input()`. Do funkcji możemy przekazać opcjonalny parametr: tekst, jaki zostanie wyświetlony użytkownikowi. Jako wynik funkcja zwraca całą linię tekstu wczytaną z wejścia.

### Wczytanie liczby

Za pomocą funkcji `input()` możemy wczytać linię tekstu z konsoli. Jeżeli chcemy, aby użytkownik podał nam liczbę, to nie możemy tego co prawda wymusić, ale możemy przetworzyć wczytany tekst na liczbę za pomocą funkcji `int()`.

#### Przykład

```python
wiek = int(input("Podaj swój wiek: "))
```
