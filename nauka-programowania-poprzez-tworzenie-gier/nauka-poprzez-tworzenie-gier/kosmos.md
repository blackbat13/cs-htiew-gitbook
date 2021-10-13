# Kosmos

## Wstęp

TODO

### Czego się nauczysz

TODO

### Grafiki do pobrania

{% file src="../../.gitbook/assets/grafiki_kosmos.zip" %}
Grafiki do gry Kosmos
{% endfile %}

### Dźwięki do pobrania

{% file src="../../.gitbook/assets/dzwieki_kosmos.zip" %}
Dźwięki do gry Kosmos
{% endfile %}

## Gra

TODO

### Pełny program

```python
import pgzrun
import random
import math

WIDTH = 1200
HEIGHT = 1200

statek = Actor("statek")
statek.x = WIDTH / 2
statek.y = HEIGHT - 60
statek.v = 2
statek.va = 2
statek.ac = 0.2
statek.maxv = 8
statek.angle = 0
statek.zycia = 3
statek.czas = 0

margines = 20

meteory = []

pociski = []

zycia = [Actor("zycie", pos=(20, 20)), Actor("zycie", pos=(60, 20)), Actor("zycie", pos=(100, 20))]


lowca = Actor("statek2")
lowca.x = -500
lowca.y = 0
lowca.v = 0.5
lowca.ac = 0.001



def draw():
    screen.fill((0, 0, 0))

    for met in meteory:
        met.draw()

    for poc in pociski:
        poc.draw()

    statek.draw()

    for i in range(statek.zycia):
        zycia[i].draw()

    if statek.zycia < 1:
        screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2), fontsize=100, color="red")

    screen.draw.text(str(statek.czas), center=(WIDTH/2, 40), fontsize=80, color="yellow")

    lowca.draw()


def update():
    if statek.zycia < 1:
        return

    statek.x += math.sin(math.radians(statek.angle - 180)) * statek.v
    statek.y += math.cos(math.radians(statek.angle - 180)) * statek.v
    if random.randint(0, 300) <= 1:
        dodaj_meteor()

    for met in meteory:
        met.x += math.sin(math.radians(met.angle - 180)) * met.v
        met.y += math.cos(math.radians(met.angle - 180)) * met.v
        if met.x > WIDTH + margines:
            met.x = -margines

        if met.x < -margines:
            met.x = WIDTH + margines

        if met.y < -margines:
            met.y = HEIGHT + margines

        if met.y > HEIGHT + margines:
            met.y = -margines

    for poc in pociski:
        poc.x += math.sin(math.radians(poc.angle - 180)) * poc.v
        poc.y += math.cos(math.radians(poc.angle - 180)) * poc.v

        if poc.x > WIDTH + margines or poc.x < -margines:
            pociski.remove(poc)

        if poc.y > HEIGHT + margines or poc.y < -margines:
            pociski.remove(poc)

    for poc in pociski:
        for met in meteory:
            if met.colliderect(poc):
                meteory.remove(met)
                pociski.remove(poc)

    for met in meteory:
        if statek.collidepoint(met.pos):
            statek.zycia -= 1
            if statek.zycia == 0:
                sounds.game_over.play()
            meteory.remove(met)
            break

    if keyboard.A:
        statek.angle += statek.va

    if keyboard.D:
        statek.angle -= statek.va

    if keyboard.W:
        statek.v += statek.ac
        if statek.v > statek.maxv:
            statek.v = statek.maxv

    if keyboard.S:
        statek.v -= statek.ac
        if statek.v < 0:
            statek.v = 0

    if statek.x > WIDTH + margines:
        statek.x = -margines

    if statek.x < -margines:
        statek.x = WIDTH + margines

    if statek.y < -margines:
        statek.y = HEIGHT + margines

    if statek.y > HEIGHT + margines:
        statek.y = -margines

    lowca.angle = lowca.angle_to(statek.pos) - 90
    lowca.x += math.sin(math.radians(lowca.angle - 180)) * lowca.v
    lowca.y += math.cos(math.radians(lowca.angle - 180)) * lowca.v
    lowca.v += lowca.ac

    if lowca.collidepoint(statek.pos):
        statek.zycia = 0
        sounds.game_over.play()


def on_key_down(key):
    if key == keys.SPACE:
        poc = Actor("laser2")
        poc.angle = statek.angle
        poc.x = statek.x
        poc.y = statek.y
        poc.v = 10
        pociski.append(poc)
        sounds.laser1.play()


def dodaj_meteor():
    grafika = random.choice(["meteor1", "meteor2", "meteor3", "meteor4"])
    met = Actor(grafika)

    strona = random.randint(1, 2)
    if strona == 1:
        met.x = random.choice([-margines, WIDTH + margines])
        met.y = random.randint(margines, HEIGHT - margines)
    else:
        met.x = random.randint(margines, WIDTH - margines)
        met.y = random.choice([-margines, HEIGHT + margines])
    met.v = random.randint(2, 10)
    met.angle = random.randint(0, 360)
    meteory.append(met)


def zwieksz_czas():
    if statek.zycia > 0:
        statek.czas += 1


clock.schedule_interval(zwieksz_czas, 1)
pgzrun.go()
```

### Testujemy działanie

TODO
