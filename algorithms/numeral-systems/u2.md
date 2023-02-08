# System U2

## Wstęp

System U2, czyli system uzupełnień do dwóch, pozwala na reprezentację nie tylko dodatnich wartości, ale także ujemnych. W tym systemie szczególne znaczenie ma pierwszy, najbardziej znaczący bit liczby, który jest bezpośrednio powiązany z jej znakiem.

## Konwersja z dziesiętnego

Istnieją dwie podstawowe metody konwersji liczby dziesiętnej na system U2.

### Przykład

Liczba do konwersji: $$-102$$ 

Docelowa liczba bitów: $$8$$ 

### Metoda I

#### 1. Konwertujemy wartość bezwzględną

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

#### 2. Dodajemy brakujące bity

$$
01100110
$$

#### 3. Zamieniamy bity na przeciwne

$$
10011001
$$

#### 4. Dodajemy liczbę 1 do wyniku

$$
10011010
$$

#### 5. Konwersja skończona

$$
-102_{10}=10011010_{U2}
$$

### Metoda II

#### 1. Rozwiązujemy równanie

$$
-102=x-128
$$

$$
x=26
$$

#### 2. Konwertujemy wynik na system binarny

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

#### 3. Dopisujemy zera i jedynkę z przodu

$$
10011010
$$

#### 4. Konwersja skończona

$$
10011010_{U2}
$$

## Konwersja do dziesiętnego

Konwersja z systemu U2 na system dziesiętny przebiega bardzo podobnie, jak przy konwersji z systemu binarnego. Zasadniczą różnicę stanowi to, w jaki sposób traktujemy pierwszy bit. Ponieważ pierwszy bit powiązany jest ze znakiem liczby, to nie tylko przemnażamy go przez odpowiednią potęgę dwójki, ale także przez $$-1$$.

### Przykład 1

$$
10011010_{U2}=2^1+2^3+2^4-2^7=2+8+16-128=26-128=-102_{10}
$$

### Przykład 2

$$
00011010_{U2}=2^1+2^3+2^4=2+8+16=26_{10}
$$