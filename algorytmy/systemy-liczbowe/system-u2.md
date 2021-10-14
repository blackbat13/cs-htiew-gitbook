# System U2

## Konwersja z dziesiętnego - przykład

Liczba do konwersji: $$-102$$ 

Docelowa liczba bitów: $$8$$ 

### Metoda I

#### Konwertujemy wartość bezwzględną

| div | mod |
| :-: | :-: |
| 102 |  0  |
|  51 |  1  |
|  25 |  1  |
|  12 |  0  |
|  6  |  0  |
|  3  |  1  |
|  1  |  1  |
|  0  |     |

$$
102_{10}=1100110_2
$$

#### Dodajemy brakujące bity

$$
01100110
$$

#### Zamieniamy bity na przeciwne

$$
10011001
$$

#### Dodajemy liczbę 1 do wyniku

$$
10011010
$$

#### Konwersja skończona

$$
-102_{10}=10011010_{U2}
$$

### Metoda II

#### Rozwiązujemy równanie

$$
-102=x-128
$$

$$
x=26
$$

#### Konwertujemy wynik na system binarny

| div | mod |
| :-: | :-: |
|  26 |  0  |
|  13 |  1  |
|  6  |  0  |
|  3  |  1  |
|  1  |  1  |
|  0  |     |

$$
26_{10}=11010_2
$$

#### Dopisujemy zera i jedynkę z przodu

$$
10011010
$$

#### Konwersja skończona

$$
10011010_{U2}
$$

## Konwersja do dziesiętnego - przykład

$$
10011010_{U2}=2^1+2^3+2^4-2^7=2+8+16-128=26-128=-102_{10}
$$
