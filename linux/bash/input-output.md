# Obsługa wejścia-wyjścia

## Wyjście

### Przykład 1

```bash
#!/bin/bash

echo "Hello World!"
```

### Przykład 2

```bash
#!/bin/bash

# Tworzymy zmienna
powitanie="Hello World!"

# Wypisujemy wartosc zmiennej
echo $powitanie
```

### Przykład 3

```bash
#!/bin/bash

powitanie="Hello World!"

# Tekst z interpretowaniem symboli
echo "Komunikat: $powitanie"

# Czysty tekst
echo 'Komunikat: $powitanie'

# Ignorowanie specjalnego znaczenia znaku
echo "Komunikat: \$powitanie"
```

## Wejście

### Przykład 1

```bash
#!/bin/bash

echo "Wpisz swoj nick:"

# Wartosci z wejscia wczytujemy poleceniem read
read username

echo "Podano: $username"
echo
echo "Podaj 3 liczby:"

read num1 num2 num3
echo "Podano: $num1, $num2, $num3"

# Korzystamy z read w formie prompt
read -p "Tekst: " tekst
echo $tekst
```

### Przykład 2

```bash
#!/bin/bash

echo "Polecenie: $0"
echo "Pierwszy parametr: $1"
echo "Drugi parametr: $2"
echo "Wszystkie parametry: $@"
```