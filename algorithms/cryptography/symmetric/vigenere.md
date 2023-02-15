# Szyfr Vigenere'a

## Opis problemu

### Specyfikacja

#### Dane

- **jawny/szyfrogram** - tekst do zaszyfrowania/odszyfrowania, składający się z małych liter alfabetu angielskiego
- **klucz** - ciąg znaków składający się z małych liter alfabetu angielskiego

### Funkcje pomocnicze

- **Pozycja(litera)** - zwraca liczbę od $$1$$ do $$26$$ - pozycję przekazanej jako argument litery w alfabecie angielskim
- **Alfabet(pozycja)** - zwraca literę na zadanej pozycji w alfabecie angielskim
- **Długość(tekst)** - zwraca długość tekstu

## Szyfrowanie

### Pseudokod

```
funkcja SzyfrujVigenere(jawny, klucz):
    1. szyfrogram := ""
    2. kluczIndeks := 1
    3. Dla i := 1 do Długość(jawny), wykonuj:
        4. nowaPozycja := Pozycja(jawny[i]) + Pozycja(klucz[kluczIndeks])
        5. Jeżeli nowaPozycja > 26, to:
            6. nowaPozycja := nowaPozycja - 26
        7. nowaLitera := Alfabet(nowaPozycja)
        8. szyfrogram := szyfrogram + nowaLitera
        9. kluczIndeks := kluczIndeks + 1
        10. Jeżeli kluczIndeks > Długość(klucz), to:
            11. kluczIndeks := 1

    12. Zwróć szyfrogram 
```

## Deszyfrowanie

### Pseudokod

```
funkcja DeszyfrujVigenere(szyfrogram, klucz):
    1. jawny := ""
    2. kluczIndeks := 1
    3. Dla i := 1 do Długość(szyfrogram), wykonuj:
        4. nowaPozycja := Pozycja(jawny[i]) - Pozycja(klucz[kluczIndeks])
        5. Jeżeli nowaPozycja < 1, to:
            6. nowaPozycja := 26 + nowaPozycja
        7. nowaLitera := Alfabet(nowaPozycja)
        8. jawny := jawny + nowaLitera
        9. kluczIndeks := kluczIndeks + 1
        10. Jeżeli kluczIndeks > Długość(klucz), to:
            11. kluczIndeks := 1

    12. Zwróć jawny 
```

## Implementacja

### C++

{% content-ref url="../../../programming/c++/algorithms/cryptography/vigenere.md" %}
[vigenere.md](../../../programming/c++/algorithms/cryptography/vigenere.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../../programming/python/algorithms/cryptography/vigenere.md" %}
[vigenere.md](../../../programming/python/algorithms/cryptography/vigenere.md)
{% endcontent-ref %}
