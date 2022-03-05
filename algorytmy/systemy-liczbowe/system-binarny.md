# System binarny

## Wstęp

System binarny, zwany także systemem dwójkowym, to podstawowy system liczbowy dla komputerów. Liczby w tym systemie reprezentujemy korzystając z dwóch cyfr: $$0$$ i $$1$$. Pozwala to na stosunkowo łatwą techniczną interpretację przesyłanych danych, np. niskie i wysokie napięcie.

## Konwersja z dziesiętnego na binarny

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna.

#### Wynik

* Reprezentacja liczby $$n$$ w systemie binarnym.

### Przykład

| **div** | **mod** |
| :-----: | :-----: |
| $$25$$  |  $$1$$  |
| $$12$$  |  $$0$$  |
|  $$6$$  |  $$0$$  |
|  $$3$$  |  $$1$$  |
|  $$1$$  |  $$1$$  |
|  $$0$$  |         |

$$
25_{10}=11001_2
$$

### Pseudokod

```
Funkcja DziesietnyNaBinarny(n):
    1. binarna := ""
    2. Dopóki n > 0, wykonuj:
        3. reszta := n mod 2
        4. Dopisz reszta na początek binarna
        5. n := n div 2
    6. Zwróc binarna
```

## Konwersja z binarnego na dziesiętny

### Przykład

$$
11001_2=1*2^4+1*2^3+0*2^2+0*2^1+1*2^0=2^4+2^3+2^0=16+8+1=25_{10}
$$
