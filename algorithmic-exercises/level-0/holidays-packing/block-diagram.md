# Block diagram

```mermaid
flowchart TD
    START([START]) --> K1[/Wczytaj a, b, c/]
    K1 --> K2{a <= 20\noraz\nb <= 20\noraz\nc <= 20}
    K2 -- PRAWDA --> K3[/Wypisz 'TAK'/]
    K2 -- FAŁSZ --> K5[/Wypisz 'NIE'/]
    K3 --> STOP([STOP])
    K5 --> STOP
```
