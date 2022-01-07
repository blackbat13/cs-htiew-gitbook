# Rozwiązania

## Część II

### Zadanie 4

#### Python

##### 4a

```python
file = open("anagram.txt")

data = file.read().split("\n")

file.close()

#  print(data)

# Dla każdej linii/wiersza z pliku wejściowego
for line in data:
    # Tworzymy listę wyrazów z linii
    words = line.split(" ")
    length = len(words[0])  # Przyjmujemy długość pierwszego wyrazu jako "właściwą"
    ok = True  # Zakładamy, że wszystko jest ok - takie same długości wyrazów
    for w in words:  # Przechodzimy przez wszystkie wyrazy w linii i szukamy kontrprzykładu
        if len(w) != length:
            ok = False
            break  # opcjonalnie

    if ok:  # Jeżeli jest ok - wszystkie wyrazy mają taką samą długość w wierszu
        print(line)
```

##### 4b

```python
file = open("anagram.txt")

data = file.read().split("\n")

file.close()

#  print(data)

# Dla każdej linii/wiersza z pliku wejściowego
for line in data:
    # Tworzymy listę wyrazów z linii
    words = line.split(" ")
    word_sorted = sorted(words[0])  # Zapamiętujemy posortowaną reprezentację pierwszego wyrazu
    ok = True  # Zakładamy, że wszystko jest ok - anagramy
    for w in words:  # Przechodzimy przez wszystkie wyrazy w linii i szukamy kontrprzykładu
        if sorted(w) != word_sorted:
            ok = False
            break  # opcjonalnie

    if ok:  # Jeżeli jest ok - wszystkie wyrazy w wierszu są anagramami
        print(line)
```

### Zadanie 6

{% file src="../../../.gitbook/assets/2010_zad6.accdb" %}
Access
{% endfile %}