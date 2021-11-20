# Asteroidy

## Wstęp

Kosmos, statki kosmiczne, asteroidy, lasery: tym się właśnie dziś zajmiemy!
Stworzymy naszą pierwszą grę kosmiczną!

### Czego się nauczysz

- Pracy z listami
- Dodawania nowych elementów do gry w trakcie jej działania
- Usuwania elementów gry w trakcie jej działania
- Odczytywania pozycji myszki
- Planowania wykonania akcji z opóźnieniem

### Grafiki do pobrania

{% file src="../../.gitbook/assets/grafiki_asteroidy.zip" %}
Grafiki do gry Asteroidy
{% endfile %}

## Gra

![Asteroidy](../../.gitbook/assets/asteroidsGame.gif)

Założenie gry jest proste: poruszamy statkiem u dołu ekranu, omijamy asteroidy, strzelamy do nich i zdobywamy punkty!
Powyższa animacja pokazuje, jak będzie wyglądać nasza gra.

### Biblioteki

Na początek dopisujemy odpowiednie biblioteki do naszej gry.
Tym razem, poza standardowymi, będziemy jeszcze potrzebowali biblioteki **pygame**, żeby móc odczytać pozycję myszy na ekranie, a także żeby móc ukryć wskaźnik myszy.

```python
import pgzrun
import pygame
import random
```

### Przygotowujemy ekran gry

Na początek ustalamy rozmiar okna i wyświetlamy tło naszej gry.
Rozmiar okna powinien być zgodny z rozmiarem grafiki tła.

```python
WIDTH = 600
HEIGHT = 900


def draw():
    screen.blit("tlo", (0, 0))
```

### Tworzymy statek

Czas dodać głównego aktora naszej gry: statek kosmiczny.
Umieścimy go na środku ekranu, na samym dole, z niewielkim marginesem dla przejrzystości.

```python
statek = Actor("statek")
statek.x = WIDTH / 2
statek.y = HEIGHT - 60
statek.px = 5
```

Gdy już mamy utworzonego aktora, możemy go wyświetlić na ekranie.

```python
def draw():
    screen.blit("tlo", (0, 0))
    statek.draw()
```

### Poruszamy statkiem

Statkiem będziemy poruszać w lewo/prawo.
Nasza postać będzie sterowana za pomocą myszki: statek będzie leciał w kierunku, w którym znajduje się wskaźnik myszy.
W części aktualizującej odczytujemy aktualną pozycję wskaźnika myszy i poruszamy statkiem we właściwym kierunku.

```python
def update():
    mysz_x, mysz_y = pygame.mouse.get_pos()
    if mysz_x < statek.x:
        statek.x -= statek.px
    if mysz_x > statek.x:
        statek.x += statek.px
```

### Przygotowujemy meteory

Czas przygotować meteory.
Chcemy, aby było w grze wyświetlało się kilka meteorów naraz. 
W tym celu potrzebna nam będzie **lista**.
Na początku tworzymy pustą listę.

```python
meteory = []
```

Teraz utworzymy funkcję, za pomocą której będziemy dodawać losowe meteory.
Na początku meteor będzie znajdował się nad ekranem, tak by efekt "spadania" wyglądał naturalniej.

```python
def dodaj_meteor():
    grafika = random.choice(["meteor1", "meteor2", "meteor3", "meteor4"])
    met = Actor(grafika)
    met.x = random.randint(20, WIDTH - 20)
    met.y = -10
    met.py = random.randint(2, 10)
    met.pa = random.randint(-5, 5)
    meteory.append(met)
```

### Dodajemy losowo meteory

W części aktualizującej będziemy losowo dodawać meteory w każdej klatce, z odpowiednio małym prawdopodobieństwem.

```python
    if random.randint(0, 250) <= 1:
        dodaj_meteor()
```

### Przemieszczamy meteory

Teraz czas na aktualizację pozycji meteorów.
W tym celu musimy przejść przez wszystkie elementy naszej listy i dla każdego wykonać odpowiednie operacje.
Robimy to w części aktualizującej.

```python
    for met in meteory:
        met.y += met.py
        if met.y > HEIGHT + 50:
            meteory.remove(met)
```

### Rysujemy meteory

Aby narysować meteory, musimy ponownie przejść przez całą listę i narysować każdy meteor osobno.

```python
    for met in meteory:
        met.draw()
```

### Pełna gra

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
statek.zycia = 3
statek.strzaly = 1
statek.punkty = 0

meteory = []

lasery = []

zycia = []


def draw():
    screen.blit("tlo", (0, 0))
    draw_meteory()
    draw_lasery()
    statek.draw()
    draw_punkty()
    draw_zycia()

    if statek.zycia == 0:
        screen.draw.text("Game Over", center=(WIDTH / 2, HEIGHT / 2), fontsize=90)


def draw_punkty():
    screen.draw.text(str(statek.punkty), center=(WIDTH / 2, 20), fontsize=50, color="yellow")


def draw_zycia():
    for st in zycia:
        st.draw()


def draw_meteory():
    for met in meteory:
        met.draw()


def draw_lasery():
    for las in lasery:
        las.draw()


def update():
    if statek.zycia == 0:
        return

    mysz_x, mysz_y = pygame.mouse.get_pos()
    if mysz_x < statek.x:
        statek.x -= statek.px
    if mysz_x > statek.x:
        statek.x += statek.px

    if random.randint(0, 250) <= 1:
        dodaj_meteor()

    update_meteory()
    update_lasery()
    update_trafienia()


def update_meteory():
    for met in meteory[:]:
        met.y += met.py
        met.angle += met.pa
        if met.y > HEIGHT + 50:
            meteory.remove(met)

        if met.colliderect(statek):
            statek.zycia -= 1
            zycia.pop()
            meteory.remove(met)


def update_lasery():
    for las in lasery[:]:
        las.y += las.py

        if las.y < -las.height:
            lasery.remove(las)


def update_trafienia():
    for las in lasery[:]:
        for met in meteory[:]:
            if las.colliderect(met):
                lasery.remove(las)
                meteory.remove(met)
                statek.punkty += 10
                break


def on_mouse_down():
    if statek.strzaly > 0:
        dodaj_laser()
        statek.strzaly -= 1
        clock.schedule(dodaj_strzal, 1)


def dodaj_laser():
    laser = Actor("laser")
    laser.x = statek.x
    laser.y = statek.y
    laser.py = -8
    lasery.append(laser)


def dodaj_meteor():
    grafika = random.choice(["meteor1", "meteor2", "meteor3", "meteor4"])
    met = Actor(grafika)
    met.x = random.randint(20, WIDTH - 20)
    met.y = -10
    met.py = random.randint(2, 10)
    met.pa = random.randint(-5, 5)
    meteory.append(met)


def dodaj_strzal():
    statek.strzaly += 1


def utworz_zycia():
    for i in range(statek.zycia):
        st = Actor("zycie")
        st.x = st.width / 2 + i * st.width
        st.y = st.height / 2
        zycia.append(st)


pygame.mouse.set_visible(False)
utworz_zycia()
pgzrun.go()

```