# Rozwiązania

## Zadanie 1

Aby sprawdzić, czy liczba binarna jest parzysta, wystarczy spojrzeć na jej ostatnią (najmniej znaczącą) cyfrę.

```python
file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

count = 0 # Licznik liczb parzystych

for binary in binary_numbers:
    if binary[-1] == "0":  # Jeżeli ostatni znak liczby binarnej to 0
        count += 1   # zwiększamy licznik liczb parzystych
        
print(count)
```

## Zadanie 2

Aby sprawdzić, czy liczba binarna jest podzielna przez 4 wystarczy sprawdzić jej dwie ostatnie (najmniej znaczące) cyfry. Jeżeli są równe 0, to liczba jest podzielna przez 4.

```python
file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

count = 0 

for binary in binary_numbers:
    if binary[-1] == "0" and binary[-2] == "0":
        count += 1

print(count)
```

## Zadanie 3

Zamieniamy liczbę binarną na system dziesiętny i sprawdzamy podzielność przez 10 za pomocą operatora modulo (reszty z dzielenia).

{% tabs %}
{% tab title="Rozwiązanie 1" %}
```python
file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

count = 0

for binary in binary_numbers:
    decimal = 0  # Wartość w systemie 10
    power = 1  # Potęga 2
    # Idziemy pętlą od końca
    for i in range(len(binary) - 1, -1, -1):
        decimal += int(binary[i]) * power  # Przemnażamy cyfrę przez potęgę dwójki
        power *= 2  # Zwiększamy potęgę dwójki

    if decimal % 10 == 0:
        count += 1

print(count)
```
{% endtab %}

{% tab title="Rozwiązanie 2" %}
```python
file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

count = 0

for binary in binary_numbers:
    decimal = int(binary, 2)

    if decimal % 10 == 0:
        count += 1

print(count)
```
{% endtab %}
{% endtabs %}

## Zadanie 4

```python
file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

count = 0

for binary in binary_numbers:
    digit_counter = dict()  # Słownik do zliczania cyfr 0 i 1
    digit_counter["0"] = 0  # Inicjalizujemy liczniki zer i jedynek
    digit_counter["1"] = 0
    for digit in binary:  # Dla każdej cyfry w zapisie liczby binarnej
        digit_counter[digit] += 1   # Zwiększamy licznik dla danej cyfry

    if digit_counter["1"] == 1:
        count += 1

print(count)
```

## Zadanie 5

```python
file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

count = 0

for binary in binary_numbers:
    digit_counter = dict()  # Słownik do zliczania cyfr 0 i 1
    digit_counter["0"] = 0  # Inicjalizujemy liczniki zer i jedynek
    digit_counter["1"] = 0
    for digit in binary:  # Dla każdej cyfry w zapisie liczby binarnej
        digit_counter[digit] += 1   # Zwiększamy licznik dla danej cyfry

    if digit_counter["0"] > digit_counter["1"]:
        count += 1

print(count)
```

## Zadanie 6

```python
file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

min_dec = 10000000000000
min_bin = ""

max_dec = 0
max_bin = ""

for binary in binary_numbers:
    decimal = 0  # Wartość w systemie 10
    power = 1  # Potęga 2
    # Idziemy pętlą od końca
    for i in range(len(binary) - 1, -1, -1):
        decimal += int(binary[i]) * power  # Przemnażamy cyfrę przez potęgę dwójki
        power *= 2  # Zwiększamy potęgę dwójki

    if decimal < min_dec:
        min_dec = decimal
        min_bin = binary

    if decimal > max_dec:
        max_dec = decimal
        max_bin = binary

print("Największa:", max_bin)
print("Najmniejsza:", min_bin)
```

## Zadanie 7

{% tabs %}
{% tab title="Rozwiązanie 1" %}
```python
file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

dict_counter = dict()

for binary in binary_numbers:
    dict_counter[binary] = 1   # Przypisujemy dowolną wartość, żeby dodać liczbę do słownika

print(len(dict_counter)) # Wypisujemy długość słownika
```
{% endtab %}

{% tab title="Rozwiązanie 2" %}
```python
file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

set_counter = set()  # Zbiór unikalnych wartości

for binary in binary_numbers:
    set_counter.add(binary)  # Dodajemy liczbę binarną do zbioru

print(len(set_counter))  # Wypisujemy długość zbioru
```
{% endtab %}
{% endtabs %}

## Zadanie 8

```python
file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

dict_counter = dict()
dict_counter["00"] = 0
dict_counter["01"] = 0
dict_counter["10"] = 0
dict_counter["11"] = 0

for binary in binary_numbers:
    dict_counter[binary[-2] + binary[-1]] += 1   # Dodajemy do odpowiedniego licznika

print(dict_counter)
```

## Zadanie 9

{% tabs %}
{% tab title="Rozwiązanie 1" %}
```python
def to_decimal(binary):
    decimal = 0  # Wartość w systemie 10
    power = 1  # Potęga 2
    # Idziemy pętlą od końca
    for i in range(len(binary) - 1, -1, -1):
        decimal += int(binary[i]) * power  # Przemnażamy cyfrę przez potęgę dwójki
        power *= 2  # Zwiększamy potęgę dwójki

    return decimal


file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

max_length = 1  # Długość najdłuższego podciągu rosnącego
max_first_index = 0  # Indeks pierwszej wartości w najdłuższym podciągu rosnącym

current_length = 1  # Długość obecnie obliczanego ciągu
current_first_index = 0  # Indeks pierwszej wartości w obecnie obliczanym ciągu

for index in range(1, len(binary_numbers)):
    # Porównujemy obecną wartość z poprzednią
    if to_decimal(binary_numbers[index]) > to_decimal(binary_numbers[index - 1]):
        current_length += 1
    else:
        current_length = 1
        current_first_index = index

    if current_length > max_length:
        max_length = current_length
        max_first_index = current_first_index

print("Długość:", max_length)
print("Indeks pierwszego el.:", max_first_index)
print("Indeks ostatniego el.:", max_first_index + max_length - 1)
max_last_index = max_first_index + max_length
print(binary_numbers[max_first_index:max_last_index])
```
{% endtab %}

{% tab title="Rozwiązanie 2" %}
```python
file = open("liczby.txt")

binary_numbers = file.read().split("\n")

file.close()

max_length = 1  # Długość najdłuższego podciągu rosnącego
max_first_index = 0  # Indeks pierwszej wartości w najdłuższym podciągu rosnącym

current_length = 1  # Długość obecnie obliczanego ciągu
current_first_index = 0  # Indeks pierwszej wartości w obecnie obliczanym ciągu

for index in range(1, len(binary_numbers)):
    # Porównujemy obecną wartość z poprzednią
    if int(binary_numbers[index], 2) > int(binary_numbers[index - 1], 2):
        current_length += 1
    else:
        current_length = 1
        current_first_index = index

    if current_length > max_length:
        max_length = current_length
        max_first_index = current_first_index

print("Długość:", max_length)
print("Indeks pierwszego el.:", max_first_index)
print("Indeks ostatniego el.:", max_first_index + max_length - 1)
max_last_index = max_first_index + max_length
print(binary_numbers[max_first_index:max_last_index])
```
{% endtab %}
{% endtabs %}

## Zadanie 10

TODO
