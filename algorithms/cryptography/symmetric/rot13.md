# Szyfr ROT13

## Opis problemu

### Specyfikacja

#### Dane

- **jawny/szyfrogram** - tekst do zaszyfrowania/odszyfrowania, składający się z małych liter alfabetu angielskiego

### Funkcje pomocnicze

- **Pozycja(litera)** - zwraca liczbę od $$1$$ do $$26$$ - pozycję przekazanej jako argument litery w alfabecie angielskim
- **Alfabet(pozycja)** - zwraca literę na zadanej pozycji w alfabecie angielskim

## Szyfrowanie

### Pseudokod

```
funkcja SzyfrujRot13(jawny):
    1. szyfrogram := ""
    2. Dla i := 1 do Długość(jawny), wykonuj:
        3. nowaPozycja := Pozycja(jawny[i]) + 13
        4. Jeżeli nowaPozycja > 26, to:
            5. nowaPozycja := nowaPozycja - 26
        6. nowaLitera := Alfabet(nowaPozycja)
        7. szyfrogram := szyfrogram + nowaLitera

    8. Zwróć szyfrogram 
```

## Deszyfrowanie

### Pseudokod

```
funkcja DeszyfrujRot13(szyfrogram):
    1. jawny := ""
    2. Dla i := 1 do Długość(szyfrogram), wykonuj:
        3. nowaPozycja := Pozycja(szyfrogram[i]) - 13
        4. Jeżeli nowaPozycja < 1, to:
            5. nowaPozycja := 26 + nowaPozycja
        6. nowaLitera := Alfabet(nowaPozycja)
        7. jawny := jawny + nowaLitera

    8. Zwróć jawny 
```

## Implementacja

### C++

{% content-ref url="../../../programming/c++/algorithms/cryptography/rot13.md" %}
[rot13.md](../../../programming/c++/algorithms/cryptography/rot13.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../../programming/python/algorithms/cryptography/rot13.md" %}
[rot13.md](../../../programming/python/algorithms/cryptography/rot13.md)
{% endcontent-ref %}
