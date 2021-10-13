# Instrukcje charakterystyczne dla języka

W języku Python jest kilka instrukcji, które nie występują w innych językach programowania, a przynajmniej nie w takiej formie. Tutaj postaramy się przedstawić takie właśnie instrukcje.

## Instrukcje arytmetyczne

### Operator potęgowania `**`

```python
dwa_do_dziesiatej = 2 ** 10 # 1024
```

### Operator dzielenia całkowitego `//`

```python
piec_przez_dwa = 5 // 2 # 2
```

## Tworzenie list

W języku Python nowe listy są domyślnie puste. Możemy je wypełnić początkowymi wartościami, ale nie możemy im nadać początkowego rozmiaru. Instrukcja `lista = [10]` oznacza utworzenie listy z jednym elementem: liczbą 10, a nie utworzenie listy o rozmiarze 10, jak można pomyśleć na podstawie języka C++.

Jest jednak sposób na utworzenie listy o określonym rozmiarze: poprzez wypełnienie jej początkowymi wartościami. Możemy to oczywiście zrobić w pętli, ale Python daje nam prostszą konstrukcję tworzenia list: _list comprehension_.

### Utworzenie dziesięcio-elementowej listy wypełnionej zerami

```python
lista = [0 for _ in range(10)]
```

### Utworzenie dziesięcio-elementowej listy wypełnionej kolejnymi wartościami od 0 do 9 włącznie

```python
lista = [i for i in range(10)]
```

### Utworzenie listy z tekstu

```python
tekst = "a b c d e f"
lista = tekst.split(" ") # ["a", "b", "c", "d", "e", "f"]
```
