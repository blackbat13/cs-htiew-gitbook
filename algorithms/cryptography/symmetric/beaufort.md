# Szyfr Beauforta

## Opis problemu

### Specyfikacja

#### Dane

- **tekst** - tekst do zaszyfrowania/odszyfrowania, składający się z małych liter alfabetu angielskiego
- **klucz** - ciąg znaków składający się z małych liter alfabetu angielskiego

### Funkcje pomocnicze

- **Pozycja(litera)** - zwraca liczbę od $$1$$ do $$26$$ - pozycję przekazanej jako argument litery w alfabecie angielskim
- **Alfabet(pozycja)** - zwraca literę na zadanej pozycji w alfabecie angielskim

## Szyfrowanie i deszyfrowanie

### Pseudokod

```
funkcja Beaufort(twkst, klucz):
    1. wynik := ""
    2. kluczIndeks := 1
    3. Dla i := 1 do Długość(twkst), wykonuj:
        4. nowaPozycja := 27 - Pozycja(twkst[i]) + Pozycja[kluczIndeks]
        5. Jeżeli nowaPozycja > 26, to:
            6. nowaPozycja := nowaPozycja - 26
        7. nowaLitera := Alfabet(nowaPozycja)
        8. wynik := wynik + nowaLitera
        9. kluczIndeks := kluczIndeks + 1
        10. Jeżeli kluczIndeks > Długość(klucz), to:
            11. kluczIndeks := kluczIndeks - Długość(klucz)

    12. Zwróć wynik 
```

## Implementacja

### C++

{% content-ref url="../../../programming/c++/algorithms/cryptography/beaufort.md" %}
[beaufort.md](../../../programming/c++/algorithms/cryptography/beaufort.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../../programming/python/algorithms/cryptography/beaufort.md" %}
[beaufort.md](../../../programming/python/algorithms/cryptography/beaufort.md)
{% endcontent-ref %}
