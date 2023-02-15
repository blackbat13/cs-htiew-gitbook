# Szyfr płotkowy

## Opis problemu

Szyfr płotkowy to jeden z prostych do przedstawienia na kartce papieru szyfrów symetrycznych. Idea polega na ułożeniu tekstu w kształt płotu o wysokości równej wartości klucza.

### Przykład 1

Tekst jawny: **ALAMAKOTA**.

Klucz: $$3$$

```
  A   O
 L M K T
A   A   A
```

Szyfrogram: **AOLMKTAAA**

### Przykład 2

Tekst jawny: **ALAMAKOTA**.

Klucz: $$4$$

```
   M
  A A    A
 L   K  T
A     O
```

Szyfrogram: **MAAALKTAO**

## Szyfrowanie

### Pseudokod

```
funckja SzyfrujPłotkowy(jawny, klucz):
    1. szyfrogram := ""
    2. Dla k := 1 do k, wykonuj:
        3. Jeżeli k = klucz, to:
            4. skok := klucz * 2
        5. w przeciwnym przypadku:
            6. skok = (klucz - k) * 2
        7. i := k
        8. Dopóki i <= Długość(jawny), wykonuj:
            9. szyfrogram := szyfrogram + jawny[i]
            10. i := i + skok

    11. Zwróć szyfrogram
```

## Deszyfrowanie

### Pseudokod

```
funkcja DeszyfrujPłotkowy(szyfrogram, klucz):
    1. jawny := szyfrogram
    2. j := 0
    3. Dla k := 1 do klucz, wykonuj:
        4. Jeżeli k = klucz, to:
            5. skok := klucz * 2
        6. w przeciwnym przypadku:
            7. skok := (klucz - k) * 2
        7. i := k
        8. Dopóki i < Długość(szyfrogram), wykonuj:
            9. jawny[i] := szyfrogram[j]
            10. j := j + 1
            11. i := i + skok

    12. Zwróć jawny
```

## Implementacja

### C++

{% content-ref url="../../../programming/c++/algorithms/cryptography/rail-fence.md" %}
[rail-fence.md](../../../programming/c++/algorithms/cryptography/rail-fence.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../../programming/python/algorithms/cryptography/rail-fence.md" %}
[rail-fence.md](../../../programming/python/algorithms/cryptography/rail-fence.md)
{% endcontent-ref %}
