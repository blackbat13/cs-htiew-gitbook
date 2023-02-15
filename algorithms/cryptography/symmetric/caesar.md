# Szyfr Cezara

## Opis problemu

### Specyfikacja

#### Dane

- **jawny/szyfrogram** - tekst do zaszyfrowania/odszyfrowania, składający się z małych liter alfabetu angielskiego
- **klucz** - liczba naturalna z zakresu $$<0,25>$$

### Funkcje pomocnicze

- **Pozycja(litera)** - zwraca liczbę od $$1$$ do $$26$$ - pozycję przekazanej jako argument litery w alfabecie angielskim
- **Alfabet(pozycja)** - zwraca literę na zadanej pozycji w alfabecie angielskim

## Szyfrowanie

### Pseudokod

```
funkcja SzyfrujCezar(jawny, klucz):
    1. szyfrogram := ""
    2. Dla i := 1 do Długość(jawny), wykonuj:
        3. nowaPozycja := Pozycja(jawny[i]) + klucz
        4. Jeżeli nowaPozycja > 26, to:
            5. nowaPozycja := nowaPozycja - 26
        6. nowaLitera := Alfabet(nowaPozycja)
        7. szyfrogram := szyfrogram + nowaLitera

    8. Zwróć szyfrogram 
```

## Deszyfrowanie

### Pseudokod

```
funkcja DeszyfrujCezar(szyfrogram, klucz):
    1. jawny := ""
    2. Dla i := 1 do Długość(szyfrogram), wykonuj:
        3. nowaPozycja := Pozycja(szyfrogram[i]) - klucz
        4. Jeżeli nowaPozycja < 1, to:
            5. nowaPozycja := 26 + nowaPozycja
        6. nowaLitera := Alfabet(nowaPozycja)
        7. jawny := jawny + nowaLitera

    8. Zwróć jawny 
```

## Implementacja

### C++

{% content-ref url="../../../programming/c++/algorithms/cryptography/caesar.md" %}
[caesar.md](../../../programming/c++/algorithms/cryptography/caesar.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../../programming/python/algorithms/cryptography/caesar.md" %}
[caesar.md](../../../programming/python/algorithms/cryptography/caesar.md)
{% endcontent-ref %}
