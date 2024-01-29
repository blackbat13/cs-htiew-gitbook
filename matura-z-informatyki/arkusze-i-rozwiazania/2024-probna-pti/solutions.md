# Rozwiązania

## Zadanie 2

### 2.3

```
Funkcja czy_k_rosnaca(A, n, k):
	1. Od i := 1 do n - k, wykonuj:
		2. Jeżeli A[i] >= A[i + k], to:
			3. Zwróć FAŁSZ
	4. Zwróć PRAWDA
```

Zaczynamy od pętli, która przechodzi przez kolejne indeksy w tablicy $$A$$ od $$1$$ do $$n - k$$ włącznie.
Chcemy zatrzymać się $$k$$ elementów przed końcem tablicy, ponieważ będziemy porównywać w pętli element obecny ($$A[i]$$) z elementem oddalonym od niego o $$k$$ ($$A[i + k]$$).
Dlatego musimy zadbać o to, aby nie wyjść poza zakres tablicy.

Wewnątrz pętli porównujemy ze sobą elementy w taki sposób, by sprawdzić, czy tablica **nie** jest $$k$$-rosnąca. Dlatego sprawdzamy czy obecny element ($$A[i]$$) jest większy lub równy od elementu oddalonego od niego o $$k$$ ($$A[i + k]$$). Jeżeli tak jest, to znaczy że tablica nie jest $$k$$-rosnąca, więc zwracamy wartość FAŁSZ jednocześnie kończąc działanie funkcji.

Jeżeli przejdziemy przez całą tablicę i nie znajdziemy dwóch elementów w *nieprawidłowej* relacji, to oznacza, że tablica jest $$k$$-rosnąca, więc zwracamy wartość PRAWDA.

### 2.4

{% tabs %}

{% tab title="C++" %}

{% code overflow="wrap" lineNumbers="true" %}
```cpp
#include <iostream>
#include <fstream>

using namespace std;

bool czy_k_rosnaca(int A[], int n, int k)
{
    for (int i = 0; i < n - k; i++)
    {
        if (A[i] >= A[i + k])
        {
            return false;
        }
    }

    return true;
}

int main()
{
    int A[100], n = 100;
    ifstream file("krosno.txt");
    for (int i = 0; i < n; i++)
    {
        file >> A[i];
    }
    file.close();

    for (int i = 1; i < n; i++)
    {
        if (czy_k_rosnaca(A, n, i))
        {
            cout << i << endl;
        }
    }

    return 0;
}
```
{% endcode %}

{% endtab %}

{% tab title="Python" %} 

{% code overflow="wrap" lineNumbers="true" %}
```python
def czy_k_rosnaca(A, n, k):
    for i in range(n - k):
        if A[i] >= A[i + k]:
            return False
        
    return True


n = 100

with open("krosno.txt") as file:
    A = [int(x) for x in file.read().split()]


for i in range(1, n):
    if czy_k_rosnaca(A, n, i):
        print(i)
```
{% endcode %}

{% endtab %}

{% endtabs %}

## Zadanie 3

### 3.3

```
Funkcja KopIter(A, n, m):
	1. Od i := n do 1 z krokiem -1, wykonuj:
		2. Od j := m do 1 z krokiem -1, wykonuj:
			3. k1 := 0
			4. k2 := 0
			5. Jeżeli i < n, to:
				6. k1 := A[i + 1][j]
			7. Jeżeli j < m, to:
				8. k2 := A[i][j + 1]
			9. Jeżeli k1 > k2, to:
				10. A[i][j] := A[i][j] + k1
			11. w przeciwnym przypadku:
				12. A[i][j] := A[i][j] + k2
	13. Zwróć A[1][1]
```

Idea rozwiązania polega na tym, aby zacząć w pewnym sensie od **końca**, tzn. od prawego dolnego rogu tablicy ($$A[n][m]$$). W tym celu przechodzimy pętlami od tyłu przez wiersze (od $$n$$ do $$1$$) i od tyłu przez kolumny (od $$m$$ do $$1$$).

W pętli do wartości obecnie obliczanego elementu ($$A[i][j]$$) dodajemy wartość **większego** z sąsiednich elementów (jeżeli istnieją). Przez sąsiednie elementy rozumiemy tutaj element leżący poniżej ($$A[i + 1][j]$$) oraz element leżący na prawo ($$A[i][j + 1]$$).

Jest to jeden z klasycznych algorytmów **dynamicznych**, który pozwala odpowiedzieć na pytanie: **jaka jest największa możliwa do uzyskania suma wartości na odwiedzonych polach, jeżeli chcemy dostać się z lewego górnego rogu do prawego dolnego rogu, a możemy poruszać się jedynie w prawo i w dół?**.

## Zadanie 4

### 4.1

{% tabs %}

{% tab title="C++" %}

{% code overflow="wrap" lineNumbers="true" %}
```cpp
```
{% endcode %}

{% endtab %}

{% tab title="Python" %} 

{% code overflow="wrap" lineNumbers="true" %}
```python
with open("konta.txt") as file:
    accounts = set(file.read().split())

print("Zadanie 1:", len(accounts))
```
{% endcode %}

{% endtab %}

{% endtabs %}

### 4.2

{% tabs %}

{% tab title="C++" %}

{% code overflow="wrap" lineNumbers="true" %}
```cpp
```
{% endcode %}

{% endtab %}

{% tab title="Python" %} 

{% code overflow="wrap" lineNumbers="true" %}
```python
with open("konta.txt") as file:
    data = [line.split() for line in file.read().split("\n")]

left = {el[0] for el in data}
right = {el[1] for el in data}
result = left.difference(right)
print("Zadanie 2:", ", ".join(result))
```
{% endcode %}

{% endtab %}

{% endtabs %}

### 4.3

{% tabs %}

{% tab title="C++" %}

{% code overflow="wrap" lineNumbers="true" %}
```cpp
```
{% endcode %}

{% endtab %}

{% tab title="Python" %} 

{% code overflow="wrap" lineNumbers="true" %}
```python
with open("konta.txt") as file:
    data = [line.split() for line in file.read().split("\n")]

relations = dict()
for el in data:
    if el[0] in relations:
        relations[el[0]].add(el[1])
    else:
        relations[el[0]] = {el[1]}

result = 0
for el in relations:
    for acc in relations[el]:
        if el in relations[acc]:
            result += 1

print("Zadanie 3:", result // 2)
```
{% endcode %}

{% endtab %}

{% endtabs %}

### 4.4

{% tabs %}

{% tab title="C++" %}

{% code overflow="wrap" lineNumbers="true" %}
```cpp
```
{% endcode %}

{% endtab %}

{% tab title="Python" %} 

{% code overflow="wrap" lineNumbers="true" %}
```python
with open("konta.txt") as file:
    data = [line.split() for line in file.read().split("\n")]

relations = dict()
for el in data:
    if el[0] in relations:
        relations[el[0]].add(el[1])
    else:
        relations[el[0]] = {el[1]}

max_obs = 0
max_acc = ""

for el in relations:
    if len(relations[el]) > max_obs:
        max_obs = len(relations[el])
        max_acc = el

print("Zadanie 4:", max_acc)
```
{% endcode %}

{% endtab %}

{% endtabs %}

### 4.5

{% tabs %}

{% tab title="C++" %}

{% code overflow="wrap" lineNumbers="true" %}
```cpp
```
{% endcode %}

{% endtab %}

{% tab title="Python" %} 

{% code overflow="wrap" lineNumbers="true" %}
```python
with open("konta.txt") as file:
    data = [line.split() for line in file.read().split("\n")]

left = {el[0] for el in data}
right = {el[1] for el in data}
false_accounts = left.difference(right)

observ_counts = dict()
for el in data:
    if el[0] in false_accounts:
        continue

    if el[1] in observ_counts:
        observ_counts[el[1]] += 1
    else:
        observ_counts[el[1]] = 1

max_obs = max(observ_counts.values())
max_acc = ""
for el in observ_counts:
    if observ_counts[el] == max_obs:
        max_acc = el

print("Zadanie 5:", max_acc)
```
{% endcode %}

{% endtab %}

{% endtabs %}

## Zadanie 5

{% file src="../../../.gitbook/assets/pti_2024_zad5.xlsm" %}
Rozwiązanie
{% endfile %}

### 5.4

Funkcja sprawdzająca, czy podana liczba jest liczbą pierwszą:

{% code overflow="wrap" lineNumbers="true" %}
```vb
Function CZY_PIERWSZA(n As Integer) As Boolean
    If n < 2 Then
        CZY_PIERWSZA = False
    Else
        wynik = True
        i = 2
        While i * i <= n
            If n Mod i = 0 Then
                wynik = False
            End If
            
            i = i + 1
        Wend
        
        CZY_PIERWSZA = wynik
    End If
End Function
```
{% endcode %}