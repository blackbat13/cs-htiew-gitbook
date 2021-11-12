# Rozwiązania

## Część I

### Zadanie 2

#### 2.1

```
[n = 2758]

1. [s = 0]

3. [s = 0 + (2758 mod 10) = 0 + 8 = 8]
4. [n = 2758 div 10 = 275]
5. 275 != 0 - OK

3. [s = 8 + (275 mod 10) = 8 + 5 = 13]
4. [n = 275 div 10 = 27]
5. 27 != 0 - OK

3. [s = 13 + (27 mod 10) = 13 + 7 = 20]
4. [n = 27 div 10 = 2]
5. 2 != 0 - OK

3. [s = 20 + (2 mod 10) = 20 + 2 = 22]
4. [n = 2 div 10 = 0]
5. 0 != 0 - NIE, koniec pętli

6. 22 mod 3 = 0 - NIE

8. OK
9. false

Wynik: false
```

```
[n = 1935]

1. [s = 0]

3. [s = 0 + (1935 mod 10) = 0 + 5 = 5]
4. [n = 1935 div 10 = 193]
5. 193 != 0 - OK

3. [s = 5 + (193 mod 10) = 5 + 3 = 8]
4. [n = 193 div 10 = 19]
5. 19 != 0 - OK

3. [s = 8 + (19 mod 10) = 8 + 9 = 17]
4. [n = 19 div 10 = 1]
5. 1 != 0 - OK

3. [s = 17 + (1 mod 10) = 17 + 1 = 18]
4. [n = 1 div 10 = 0]
5. 0 != 0 - NIE, koniec pętli

6. 18 mod 3 = 0 - OK
7. true

Wynik: true
```

## Część II

### Zadanie 5

{% file src="../../../.gitbook/assets/2016_p_zad5.xlsx" %}
Excel
{% endfile %}

### Zadanie 6

{% file src="../../../.gitbook/assets/2016_p_zad6.accdb" %}
Access
{% endfile %}
