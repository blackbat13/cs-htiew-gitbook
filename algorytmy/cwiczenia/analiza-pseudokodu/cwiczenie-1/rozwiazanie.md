# Rozwiązanie

## Zadanie 1

```
[x = 10, y = 3]

1. [q = 0]
2. [r = 10]

3. Dopóki 3 <= 10 - OK
    4. [q = 0 + 1 = 1]
    5. [r = 10 - 3 = 7]
    
3. Dopóki 3 <= 7 - OK
    4. [q = 1 + 1 = 2]
    5. [r = 7 - 3 = 4]
    
3. Dopóki 3 <= 4 - OK
    4. [q = 2 + 1 = 3]
    5. [r = 4 - 3 = 1]
    
3. Dopóki 3 <= 1 - NIE (koniec pętli)

6. Wypisz 3
7. Wypisz 1    
```

**Wynik**: $$q=3,\ r=1$$

## Zadanie 2

```
[x = 50, y = 15]

1. [q = 0]
2. [r = 50]

3. Dopóki 15 <= 50 - OK
    4. [q = 0 + 1 = 1]
    5. [r = 50 - 15 = 35]
    
3. Dopóki 15 <= 35 - OK
    4. [q = 1 + 1 = 2]
    5. [r = 35 - 15 = 20]
    
3. Dopóki 15 <= 20 - OK
    4. [q = 2 + 1 = 3]
    5. [r = 20 - 15 = 5]
    
3. Dopóki 15 <= 5 - NIE (koniec pętli)

6. Wypisz 3
7. Wypisz 5
```

**Wynik**: $$q=3,\ r=5$$

## Zadanie 3

#### Wynik

* $$q$$ - wynik dzielenia całkowitego $$x$$ przez $$y$$ (`q = x div y`)
* $$r$$ - wynik reszty z dzielenia $$x$$ przez $$y$$ (`r = x mod y`)
