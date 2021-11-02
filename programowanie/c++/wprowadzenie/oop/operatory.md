# Przeciążanie operatorów

## Wstęp

Na nowo zdefiniowanych własnych typach przeprowadzamy różne operacje.
Często są to także standardowe operacje arytmetyczne, jak np. dodanie do siebie współrzędnych dwóch punktów.
W takich sytuacjach wygodniej jest korzystać z predefiniowanych operatorów, takich jak operator dodawania $$+$$ zamiast z metod typu ``add``.

Wyobraźmy sobie, że mamy dwie zmienne (obiekty) reprezentujące punkty: ``p1`` oraz ``p2``. 
Chcemy dodać współrzędne jednego punktu do drugiego i wynik zapisać w zmiennej ``p1``.
Zazwyczaj zapisalibyśmy coś w stylu ``p1.Add(p2)``.
Używając jednak **przeciążenia operatorów** możemy zapisać ``p1 = p1 + p2``.

## Przykład: dodawanie punktów

### Point2D

```cpp
Point2D operator+(const Point2D &other) {
  return Point2D(this->x + other.x, this->y + other.y);
}
```

### main

```cpp
Point2D p1 = Point2D(3, 4);
Point2D p2 = Point2D(1, 9);

auto p3 = p1 + p2;

p3.print();
```
