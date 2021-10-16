# Asteroidy

## Wstęp

TODO

### Czego się nauczysz

TODO

### Grafiki do pobrania

{% file src="../../.gitbook/assets/grafiki_asteroidy.zip" %}
Grafiki do gry Asteroidy
{% endfile %}

## Gra

TODO

### Przygotowujemy ekran gry

TODO

```python
WIDTH = 600
HEIGHT = 900
```

TODO

```python
def draw():
    screen.blit("tlo", (0, 0))
```

### Tworzymy statek

TODO

```python
statek = Actor("statek")
statek.x = WIDTH / 2
statek.y = HEIGHT - 60
statek.px = 5
```

TODO

```python
def draw():
    screen.blit("tlo", (0, 0))
    statek.draw()
```

### Poruszamy statkiem

TODO

```python
def update():
    mysz_x, mysz_y = pygame.mouse.get_pos()
    if mysz_x < statek.x:
        statek.x -= statek.px
    if mysz_x > statek.x:
        statek.x += statek.px
```

### Przygotowujemy meteory

TODO

```python
meteory = []
```

TODO

```python
def dodaj_meteor():
    grafika = random.choice(["meteor1", "meteor2", "meteor3", "meteor4"])
    met = Actor(grafika)
    met.x = random.randint(20, WIDTH - 20)
    met.y = -10
    met.py = random.randint(2, 10)
    meteory.append(met)
```

### Dodajemy losowo meteory

TODO

```python
    if random.randint(0, 250) <= 1:
        dodaj_meteor()
```

### Przemieszczamy meteory

TODO

```python
    for met in meteory:
        met.y += met.py
```

TODO

```python
        if met.y > HEIGHT + 50:
            meteory.remove(met)
```

TODO

```python
    for met in meteory:
        met.y += met.py
        if met.y > HEIGHT + 50:
            meteory.remove(met)
```

### Pełny program

```python
import pgzrun
import random
import pygame

WIDTH = 600
HEIGHT = 900

statek = Actor("statek")
statek.x = WIDTH / 2
statek.y = HEIGHT - 60
statek.px = 5

meteory = []


def draw():
    screen.blit("tlo", (0, 0))
    statek.draw()

    for met in meteory:
        met.draw()


def update():
    mysz_x, mysz_y = pygame.mouse.get_pos()
    if mysz_x < statek.x:
        statek.x -= statek.px
    if mysz_x > statek.x:
        statek.x += statek.px

    if random.randint(0, 250) <= 1:
        dodaj_meteor()

    for met in meteory:
        met.y += met.py
        if met.y > HEIGHT + 50:
            meteory.remove(met)


def dodaj_meteor():
    grafika = random.choice(["meteor1", "meteor2", "meteor3", "meteor4"])
    met = Actor(grafika)
    met.x = random.randint(20, WIDTH - 20)
    met.y = -10
    met.py = random.randint(2, 10)
    meteory.append(met)


pgzrun.go()
```

### Testujemy działanie

TODO

## Zadania dodatkowe

TODO
