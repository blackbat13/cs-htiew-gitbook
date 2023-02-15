# Szyfr Trithemius'a

## Opis problemu

### Specyfikacja

#### Dane

- **jawny/szyfrogram** - tekst do zaszyfrowania/odszyfrowania, składający się z małych liter alfabetu angielskiego

### Funkcje pomocnicze

- **Pozycja(litera)** - zwraca liczbę od $$1$$ do $$26$$ - pozycję przekazanej jako argument litery w alfabecie angielskim
- **Alfabet(pozycja)** - zwraca literę na zadanej pozycji w alfabecie angielskim
- **Długość(tekst)** - zwraca długość tekstu

## Szyfrowanie

### Pseudokod

```
funkcja SzyfrujTrithemius(jawny):
    1. szyfrogram := ""
    2. k := 0
    3. Dla i := 1 do Długość(jawny), wykonuj:
        4. nowaPozycja := Pozycja(jawny[i]) + k
        5. Jeżeli nowaPozycja > 26, to:
            6. nowaPozycja := nowaPozycja - 26
        7. nowaLitera := Alfabet(nowaPozycja)
        8. szyfrogram := szyfrogram + nowaLitera
        9. k := (k + 1) mod 26

    10. Zwróć szyfrogram 
```

## Deszyfrowanie

### Pseudokod

```
funkcja DeszyfrujTrithemius(szyfrogram):
    1. jawny := ""
    2. k := 0
    3. Dla i := 1 do Długość(szyfrogram), wykonuj:
        4. nowaPozycja := Pozycja(szyfrogram[i]) - k
        5. Jeżeli nowaPozycja < 1, to:
            6. nowaPozycja := 26 + nowaPozycja
        7. nowaLitera := Alfabet(nowaPozycja)
        8. jawny := jawny + nowaLitera
        9. k := (k + 1) mod 26

    10. Zwróć jawny 
```

## Implementacja

### C++

{% content-ref url="../../../programming/c++/algorithms/cryptography/trithemius.md" %}
[trithemius.md](../../../programming/c++/algorithms/cryptography/trithemius.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../../programming/python/algorithms/cryptography/trithemius.md" %}
[trithemius.md](../../../programming/python/algorithms/cryptography/trithemius.md)
{% endcontent-ref %}
