# Problem n królowych

## Opis problemu

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna, liczba królowych do rozstawienia

#### Wynik

- **PRAWDA** jeżeli istnieje poprawne rozwiązanie
- **FAŁSZ** w przeciwnym przypadku

## Rozwiązanie

Idea naszego rozwiązania jest prosta. Będziemy przechodzić wiersz po wierszu i próbować wszystkie możliwe ustawienia królowych w wierszu. Po ustawieniu królowej w danym wierszu przechodzimy do kolejnego wiersza, gdzie ponownie sprawdzamy wszystkie możliwe ustawienia.

Oczywiście w ten sposób sprawdzalibyśmy wiele błędnych ustawień. Dlatego przed ustawieniem nowej królowej będziemy sprawdzać, czy jest to poprawne ustawienie, tzn. czy to pole nie jest już atakowane przez żadną inną królową.

W celu sprawdzenia, czy dane pole nie jest atakowane przez inną królową, musimy przejść przez wszystkie poprzednie wiersze i sprawdzić, czy królowa ustawiona w danym wierszu nie atakuje obecnego pola w pionie lub na ukos.

### Pseudokod

```
funkcja SprawdźPozycję(wiersz, kolumna, pozycje):
    1. Dla i := 1 do wiersz - 1, wykonuj:
        2. Jeżeli pozycje[i] = kolumna lub kolumna - pozycje[i] = wiersz - i, to:
            3. Zwróć FAŁSZ
    4. Zwróć PRAWDA
```

```
funkcja ZnajdźRozwiązanie(n, wiersz, pozycje):
    1. Jeżeli wiersz > n, to:
        2. Zwróć PRAWDA
    3. Dla kolumna := 1 do n, wykonuj:
        4. Jeżeli SprawdźPozycję(wiersz, kolumna, pozycje), to:
            5. pozycje[wiersz] := kolumna
            6. Jeżeli ZnajdźRozwiązanie(n, wiersz + 1, pozycje), to:
                7. Zwróć PRAWDA
    8. Zwróć FAŁSZ
```

### Schemat blokowy

```mermaid
flowchart TD
    START(["SprawdźPozycję(wiersz, kolumna, pozycje)"]) --> K0[i := 1]
    K0 --> K1{i < wiersz}
    K1 -- PRAWDA --> K2{"pozycje[i] = kolumna\nlub\nkolumna - pozycje[i] = wiersz - i"}
    K2 -- PRAWDA --> K3[/Zwróć FAŁSZ/]
    K2 -- FAŁSZ --> K1i[i := i + 1]
    K1i --> K1
    K1 -- FAŁSZ --> K4[/Zwróć PRAWDA/]
    K3 --> STOP([STOP])
    K4 --> STOP
```

```mermaid
flowchart TD
    START(["ZnajdźRozwiązanie(n, wiersz, pozycje)"]) --> K1{wiersz > n}
    K1 -- PRAWDA --> K2[/Zwróć PRAWDA/]
    K2 --> STOP([STOP])
    K1 -- FAŁSZ --> K3p[kolumna := 1]
    K3p --> K3{kolumna <= n}
    K3 -- PRAWDA --> K4{"SprawdźPozycję(wiersz, kolumna, pozycje)"}
    K4 -- PRAWDA --> K5["pozycje[wiersz] := kolumna"]
    K5 --> K6{"ZnajdźRozwiązanie(n, wiersz + 1, pozycje)"}
    K6 -- PRAWDA --> K7[/Zwróć PRAWDA/]
    K7 --> STOP
    K6 -- FAŁSZ --> K3i[kolumna := kolumna + 1]
    K4 -- FAŁSZ --> K3i
    K3i --> K3
    K3 -- FAŁSZ --> K8[/Zwróć FAŁSZ/]
    K8 --> STOP
```

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/backtracking/n-queens.md" %}
[n-queens.md](../../programming/c++/algorithms/backtracking/n-queens.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/backtracking/n-queens.md" %}
[n-queens.md](../../programming/python/algorithms/backtracking/n-queens.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programming/kotlin/algorithms/backtracking/n-queens.md" %}
[n-queens.md](../../programming/kotlin/algorithms/backtracking/n-queens.md)
{% endcontent-ref %}