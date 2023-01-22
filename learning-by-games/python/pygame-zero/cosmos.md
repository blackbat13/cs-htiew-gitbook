# Kosmos

## Wstęp

Dzisiaj spróbujemy zasymulować bardziej naturalny ruch w kosmosie.
Dodamy też przeciwników, którzy będą za nami podążać i do nas strzelać!
Jak długo uda nam się przetrwać?

### Czego się nauczysz

- Poruszania postacią zgodnie z kierunkiem obrotu.
- Kierowania przeciwników w stronę gracza.
- Śledzenia kolizji wielu elementów gry.
- Podziału kodu na czytelne części.
- Śledzenia czasu gry.

### Grafiki do pobrania

{% file src="../../../.gitbook/assets/grafiki_kosmos.zip" %}
Grafiki do gry Kosmos
{% endfile %}

### Dźwięki do pobrania

{% file src="../../../.gitbook/assets/dzwieki_kosmos.zip" %}
Dźwięki do gry Kosmos
{% endfile %}

## Gra

![Kosmos](../../../.gitbook/assets/cosmos.gif)

## Szablon

Tym bardziej zaczniemy od bardziej rozbudowanego niż zwykle szablonu gry.
Przygotujemy sobie kilka funkcji, które później będziemy uzupełniać właściwą zawartością.
Dzięki temu nasz kod stanie się czytelniejszy, a nasza praca prostsza.

### Biblioteki

Oprócz podstawowych bibliotek *pgzrun* do obsługi gry oraz *random* do liczb losowych, przyda nam się także biblioteka *math* do obliczeń matematycznych, które będą nam potrzebny przy ruchach postaci.

```python
import pgzrun
import random
import math
```

### Konfiguracja

Utworzymy ekran o wymiarach $$1200\times 1200$$. Do tego w opcjach konfiguracyjnych zapamiętamy sobie także margines (**MARGIN**) o wartości $$20$$, którego będziemy używać przy elementach interfejsu.

```python
...

WIDTH = 1200
HEIGHT = 1200
MARGIN = 20
```

### Listy elementów

W naszej grze znajdzie się kilka rodzajów elementów, nie licząc samego gracza. Będą to:

- asteroidy (*asteroids*),
- przeciwnicy (*enemies*),
- lasery wystrzelone przez gracza (*playerLasers*),
- lasery wystrzelone przez przecinika (*enemyLasers*).

Ponieważ tych elementów może być wiele jednocześnie na ekranie, to każdy z typów zapamiętamy w osobnej liście. Na początku do naszych zmiennych przypiszemy pustą listę, czy puste nawiasy kwadratowe (`[]`).

```python
...

asteroids = []
playerLasers = []
enemyLasers = []
enemies = []
```

### Rysowanie

Jak zwykle będzie nam potrzebna funkcja rysująca zmiany na ekranie (*draw*). Wewnątrz niej wypełnimy ekran czarnym (*black*) kolorem za pomocą funkcji *screen.fill*.

```python
...

def draw():
    screen.fill("black")
```

Poza główną funkcją rysującą przyda nam się także pomocnicza funkcja rysująca wszystkie elmenty z podanej listy, ponieważ w naszej grze większość elementów będziemy przechowywać w listach. Stworzymy więc funkcję *drawList*, która przyjmie jeden parametr: listę elementów do narysowania. Parametr nazwiemy *list* i podamy go w okrągłych nawiasach po nazwie funkcji: *drawList(list)*.

```python
...

def drawList(list):
```

Naszą funkcję uzupełnimy później, teraz tworzymy tylko jej szablon, więc dopiszemy do niej instrukcję *pass*.

```python
...

def drawList(list):
    pass
```

### Aktualizacja

Ponieważ w naszej grze będzie wiele elementów, to będziemy musieli wiele rzeczy aktualizować. Aby zapobiec bałaganowi w kodzie, podzielimy sobie aktualizację na następujące funkcje:

- aktualizacja gracza (*updatePlayer*),
- aktualizacja laserów gracza (*updatePlayerLasers*),
- aktualizacja asteroid (*updateAsteroids*),
- aktualizacja przeciwników (*updateEnemies*),
- aktualizacja laserów przeciwników (*updateEnemyLasers*),
- aktualizacja kolizji (*updateCollisions*).

Wszystkie te funkcje wywołamy po kolei w funkcji *update*:

```python
...

def update():
    updatePlayer()
    updatePlayerLasers()
    updateAsteroids()
    updateEnemies()
    updateEnemyLasers()
    updateCollisions()
```

Teraz pozostało nam stworzyć szablony tych funkcji, wszystkie z jedną instrukcją: *pass*.

```python
...

def updatePlayer():
    pass


def updatePlayerLasers():
    pass


def updateAsteroids():
    pass


def updateEnemies():
    pass


def updateEnemyLasers():
    pass


def updateCollisions():
    pass
```

### Funkcje pomocnicze

Przyda nam się jeszcze pięć funkcji pomocniczych:

- dodanie nowego lasera gracza (*addPlayerLaser*),
- dodanie nowej asteroidy (*addAsteroid*),
- dodanie nowego przeciwnika (*addEnemy*),
- dodanie nowego lasera przeciwnika (*addEnemyLaser(enemy)*),
- zwiększenie licznika czas (*addTime*).

Podobnie jak wcześniej, funkcje stworzymy jako szablony i wypełnimy jedynie instrukcją *pass*.

```python
...

def addPlayerLaser():
    pass


def addAsteroid():
    pass


def addEnemy():
    pass


def addEnemyLaser(enemy):
    pass


def addTime():
    pass
```

### Uruchomienie gry

Pozostało nam na samym dole naszego kodu dopisać instrukcję uruchamiającą grę.

```python
...

pgzrun.go()
```

### Pełny kod

```python
import pgzrun
import random
import math

WIDTH = 1200
HEIGHT = 1200
MARGIN = 20

asteroids = []
playerLasers = []
enemyLasers = []
enemies = []


def draw():
    screen.fill("black")


def drawList(list):
    pass


def update():
    updatePlayer()
    updateAsteroids()
    updatePlayerLasers()
    updateEnemies()
    updateEnemyLasers()
    updateCollisions()


def updatePlayer():
    pass


def updateAsteroids():
    pass


def updatePlayerLasers():
    pass


def updateEnemies():
    pass


def updateEnemyLasers():
    pass


def updateCollisions():
    pass


def addPlayerLaser():
    pass


def addAsteroid():
    pass


def addEnemy():
    pass


def addEnemyLaser(enemy):
    pass


def addTime():
    pass


pgzrun.go()
```

## Gracz

### Dodajemy gracza

```python
player = Actor("player")
player.x = WIDTH / 2
player.y = HEIGHT - 60
player.v = 2
player.va = 2
player.ac = 0.2
player.maxv = 8
player.angle = 0
player.lifes = 3
player.time = 0
```

### Rysujemy gracza

Na końcu części rysującej dopisujemy instrukcję rysującą naszego gracza na ekranie: *player.draw()*.

```python
def draw():
    ...
    player.draw()
```

### Poruszamy graczem

Przemieszczamy gracza zgodnie z jego kierunkiem ruchu.

```python
def updatePlayer():
    player.x += math.sin(math.radians(player.angle - 180)) * player.v
    player.y += math.cos(math.radians(player.angle - 180)) * player.v
```

Jeżeli wciśnięty jest klawisz **A** (*if keyboard.A*), to obracamy gracza przeciwnie do ruchu wskazówek zegara zgodnie z jego prędkością obrotu (*player.va*). W tym celu dodajemy prędkość obrotu do kąta gracza (*player.angle*).

```python
def updatePlayer():
    ...
    if keyboard.A:
        player.angle += player.va
```

Podobnie postępujemy przy obrocie zgodnie ze wskazówkami zegara, gdy naciśnięty jest klawisz **D**. Tym razem odejmujemy prędkość obrotu od kąta gracza.

```python
def updatePlayer():
    ...
    if keyboard.A:
        player.angle += player.va

    if keyboard.D:
        player.angle -= player.va
```

Gdy naciśnięty będzie klawisz **W**, to gracz powinien przyspieszać, nie przekraczając jednak swojej maksymalnej prędkości. Aby zwiększyć prędkość gracza (*player.v*) dodamy do niej jego przyspieszenie (*player.ac*).

```python
def updatePlayer():
    ...
    if keyboard.W:
        player.v += player.ac
```

Następnie powinniśmy sprawdzić, czy prędkość nie przekroczyła prędkości maksymalnej (*player.maxv*). Jeżeli tak się stanie, to powinniśmy przywrócić prędkość maksymalną, tzn. do prędkości przypisać prędkość maksymalną.

```python
def updatePlayer():
    ...
    if keyboard.W:
        player.v += player.ac
        if player.v > player.maxv:
            player.v = player.maxv
```

Podobnie postąpimy w przypadku zwalniania, gdy wciśnięty jest klawisz **S**. Najpierw zmniejszymy prędkość gracza odejmując od niej przyspieszenie.

```python
def updatePlayer():
    ...
    if keyboard.S:
        player.v -= player.ac
```

Następnie sprawdzimy, czy prędkość spadła poniżej zera. Jeżeli tak, to przywrócimy prędkości wartość zero.

```python
def updatePlayer():
    ...
    if keyboard.S:
        player.v -= player.ac
        if player.v < 0:
            player.v = 0
```

### Przechodzimy przez krawędzie ekranu

```python
def updatePlayer():
    ...
    if player.x > WIDTH + MARGIN:
        player.x = -MARGIN
```

```python
def updatePlayer():
    ...
    if player.x > WIDTH + MARGIN:
        player.x = -MARGIN

    if player.x < -MARGIN:
        player.x = WIDTH + MARGIN
```

```python
def updatePlayer():
    ...
    if player.x > WIDTH + MARGIN:
        player.x = -MARGIN

    if player.x < -MARGIN:
        player.x = WIDTH + MARGIN

    if player.y < -MARGIN:
        player.y = HEIGHT + MARGIN
```

```python
def updatePlayer():
    ...
    if player.x > WIDTH + MARGIN:
        player.x = -MARGIN

    if player.x < -MARGIN:
        player.x = WIDTH + MARGIN

    if player.y < -MARGIN:
        player.y = HEIGHT + MARGIN

    if player.y > HEIGHT + MARGIN:
        player.y = -MARGIN
```

### Pełny kod

```python
import pgzrun
import random
import math

WIDTH = 1200
HEIGHT = 1200
MARGIN = 20

asteroids = []
playerLasers = []
enemyLasers = []
enemies = []

player = Actor("player")
player.x = WIDTH / 2
player.y = HEIGHT - 60
player.v = 2
player.va = 2
player.ac = 0.2
player.maxv = 8
player.angle = 0
player.lifes = 3
player.time = 0

def draw():
    screen.fill("black")
    player.draw()


def drawList(list):
    pass


def update():
    updatePlayer()
    updateAsteroids()
    updatePlayerLasers()
    updateEnemies()
    updateEnemyLasers()
    updateCollisions()


def updatePlayer():
    player.x += math.sin(math.radians(player.angle - 180)) * player.v
    player.y += math.cos(math.radians(player.angle - 180)) * player.v

    if keyboard.A:
        player.angle += player.va

    if keyboard.D:
        player.angle -= player.va

    if keyboard.W:
        player.v += player.ac
        if player.v > player.maxv:
            player.v = player.maxv

    if keyboard.S:
        player.v -= player.ac
        if player.v < 0:
            player.v = 0

    if player.x > WIDTH + MARGIN:
        player.x = -MARGIN

    if player.x < -MARGIN:
        player.x = WIDTH + MARGIN

    if player.y < -MARGIN:
        player.y = HEIGHT + MARGIN

    if player.y > HEIGHT + MARGIN:
        player.y = -MARGIN


def updateAsteroids():
    pass


def updatePlayerLasers():
    pass


def updateEnemies():
    pass


def updateEnemyLasers():
    pass


def updateCollisions():
    pass


def addPlayerLaser():
    pass


def addAsteroid():
    pass


def addEnemy():
    pass


def addEnemyLaser(enemy):
    pass


def addTime():
    pass


pgzrun.go()
```

## Strzelamy

### Dodajemy laser

```python
def on_key_down(key):
    if key == keys.SPACE:
        las = Actor("laser1")
        las.angle = player.angle
        las.x = player.x
        las.y = player.y
        las.v = 10
        playerLasers.append(las)
        sounds.laser1.play()
```

### Rysujemy lasery

Zacznijmy od uzupełnienia naszej funkcji *drawList* rysującej wszystkie elementy listy na ekranie.

```python
def drawList(list):
    for element in list:
        element.draw()
```

Teraz pozostało nam w części rysującej *draw* wywołać naszą funkcję z parametrem *playerLasers*, by narysować wszystkie lasery gracza na ekranie. Ponieważ nie chcemy, by lasery przykrywały grafikę gracza, to narysujemy je przed graczem, czyli przed instrukcją *player.draw()*.

```python
def draw():
    screen.fill("black")

    drawList(playerLasers)

    player.draw()
```

### Poruszamy laserami

```python
def updatePlayerLasers():
    for las in playerLasers[:]:
        las.x += math.sin(math.radians(las.angle - 180)) * las.v
        las.y += math.cos(math.radians(las.angle - 180)) * las.v

        if las.x > WIDTH + MARGIN or las.x < -MARGIN:
            playerLasers.remove(las)
        elif las.y > HEIGHT + MARGIN or las.y < -MARGIN:
            playerLasers.remove(las)
```

## Przeciwnicy

### Dodajemy przeciwników

```python
def updateEnemies():
    if random.randint(0, 500) <= 1:
        addEnemy()


def addEnemy():
    enemy = Actor("enemy")
    side = random.randint(1, 2)
    if side == 1:
        enemy.x = random.choice([-MARGIN, WIDTH + MARGIN])
        enemy.y = random.randint(MARGIN, HEIGHT - MARGIN)
    else:
        enemy.x = random.randint(MARGIN, WIDTH - MARGIN)
        enemy.y = random.choice([-MARGIN, HEIGHT + MARGIN])

    enemy.v = random.randint(2, 5)
    enemies.append(enemy)
```

### Rysujemy przeciwników

```python
def draw():
    screen.fill((0, 0, 0))

    drawList(playerLasers)
    drawList(enemies)

    player.draw()
```

### Poruszamy przeciwnikami

```python
def updateEnemies():
    if random.randint(0, 500) <= 1:
        addEnemy()

    for enemy in enemies:
        enemy.angle = enemy.angle_to(player.pos) - 90
        enemy.x += math.sin(math.radians(enemy.angle - 180)) * enemy.v
        enemy.y += math.cos(math.radians(enemy.angle - 180)) * enemy.v
```

### Strzelamy laserami

```python
def updateEnemies():
    if random.randint(0, 500) <= 1:
        addEnemy()

    for enemy in enemies:
        enemy.angle = enemy.angle_to(player.pos) - 90
        enemy.x += math.sin(math.radians(enemy.angle - 180)) * enemy.v
        enemy.y += math.cos(math.radians(enemy.angle - 180)) * enemy.v

        if random.randint(0, 500) <= 1:
            las = Actor("laser2")
            las.angle = enemy.angle
            las.x = enemy.x
            las.y = enemy.y
            las.v = random.randint(5, 10)
            enemyLasers.append(las)
            sounds.laser2.play()
```

### Rysujemy lasery

```python
def draw():
    screen.fill((0, 0, 0))

    drawList(playerLasers)
    drawList(enemyLasers)
    drawList(enemies)

    player.draw()
```

### Poruszamy laserami

```python
def updateEnemyLasers():
    for las in enemyLasers[:]:
        las.x += math.sin(math.radians(las.angle - 180)) * las.v
        las.y += math.cos(math.radians(las.angle - 180)) * las.v

        if las.x > WIDTH + MARGIN or las.x < -MARGIN:
            enemyLasers.remove(las)
        elif las.y > HEIGHT + MARGIN or las.y < -MARGIN:
            enemyLasers.remove(las)
```

### Sprawdzamy kolizje

```python
def updateCollisions():
    for las in playerLasers[:]:
        for enemy in enemies[:]:
            if enemy.colliderect(las):
                enemies.remove(enemy)
                playerLasers.remove(las)

    for las in enemyLasers[:]:
        if player.collidepoint(las.pos):
            player.lifes -= 1
            if player.lifes == 0:
                sounds.game_over.play()
            enemyLasers.remove(las)

    for enemy in enemies[:]:
        if player.collidepoint(enemy.pos):
            player.lifes -= 1
            if player.lifes == 0:
                sounds.game_over.play()
            enemies.remove(enemy)
```

## Asteroidy

### Dodajemy asteroidy

```python
def updateAsteroids():
    if random.randint(0, 1000) <= 1:
        addAsteroid()


def addAsteroid():
    image = random.choice(["meteor1", "meteor2", "meteor3", "meteor4"])
    ast = Actor(image)

    side = random.randint(1, 2)
    if side == 1:
        ast.x = random.choice([-MARGIN, WIDTH + MARGIN])
        ast.y = random.randint(MARGIN, HEIGHT - MARGIN)
    else:
        ast.x = random.randint(MARGIN, WIDTH - MARGIN)
        ast.y = random.choice([-MARGIN, HEIGHT + MARGIN])
    ast.v = random.randint(2, 10)
    ast.angle = random.randint(0, 360)
    asteroids.append(ast)
```

### Rysujemy asteroidy

```python
def draw():
    screen.fill((0, 0, 0))

    drawList(asteroids)
    drawList(playerLasers)
    drawList(enemyLasers)
    drawList(enemies)

    player.draw()
```

### Poruszamy asteroidami

```python
def updateAsteroids():
    if random.randint(0, 1000) <= 1:
        addAsteroid()

    for ast in asteroids:
        ast.x += math.sin(math.radians(ast.angle - 180)) * ast.v
        ast.y += math.cos(math.radians(ast.angle - 180)) * ast.v

        if ast.x > WIDTH + MARGIN:
            ast.x = -MARGIN

        if ast.x < -MARGIN:
            ast.x = WIDTH + MARGIN

        if ast.y < -MARGIN:
            ast.y = HEIGHT + MARGIN

        if ast.y > HEIGHT + MARGIN:
            ast.y = -MARGIN
```

### Sprawdzamy kolizje

```python
def updateCollisions():
    ...

    for las in playerLasers[:]:
        for met in asteroids[:]:
            if met.colliderect(las):
                asteroids.remove(met)
                playerLasers.remove(las)

    for las in enemyLasers[:]:
        for met in asteroids[:]:
            if met.colliderect(las):
                asteroids.remove(met)
                enemyLasers.remove(las)

    for ast in asteroids[:]:
        if player.collidepoint(ast.pos):
            player.lifes -= 1
            if player.lifes == 0:
                sounds.game_over.play()
            asteroids.remove(ast)
```

## Czas

### Wyświetlamy czas

```python
def draw():
    ...
    screen.draw.text(str(player.time), center=(WIDTH / 2, 40), fontsize=80, color="yellow")
```

### Aktualizujemy czas

```python
def addTime():
    if player.lifes > 0:
        player.time += 1


clock.schedule_interval(addTime, 1)
```

## Życia

### Dodajemy życia

```python
lifes = [Actor("life", pos=(20, 20)), Actor("life", pos=(60, 20)), Actor("life", pos=(100, 20))]
```

### Rysujemy życia

```python
def draw():
    ...
    for i in range(player.lifes):
        lifes[i].draw()
```

## Koniec gry

### Zatrzymujemy grę

```python
def update():
    if player.lifes < 1:
        return
    ...
```

### Wyświetlamy napis GAME OVER

```python
def draw():
    ...
    if player.lifes < 1:
        screen.draw.text("GAME OVER", center=(WIDTH / 2, HEIGHT / 2), fontsize=100, color="red")
```

## Pełna gra

```python
import pgzrun
import random
import math

WIDTH = 1200
HEIGHT = 1200
MARGIN = 20

player = Actor("player")
player.x = WIDTH / 2
player.y = HEIGHT - 60
player.v = 2
player.va = 2
player.ac = 0.2
player.maxv = 8
player.angle = 0
player.lifes = 3
player.time = 0

asteroids = []
playerLasers = []
enemyLasers = []
enemies = []

lifes = [Actor("life", pos=(20, 20)), Actor("life", pos=(60, 20)), Actor("life", pos=(100, 20))]


def draw():
    screen.fill((0, 0, 0))

    drawList(asteroids)
    drawList(playerLasers)
    drawList(enemyLasers)
    drawList(enemies)

    player.draw()

    for i in range(player.lifes):
        lifes[i].draw()

    if player.lifes < 1:
        screen.draw.text("GAME OVER", center=(WIDTH / 2, HEIGHT / 2), fontsize=100, color="red")

    screen.draw.text(str(player.time), center=(WIDTH / 2, 40), fontsize=80, color="yellow")

def drawList(list):
    for element in list:
        element.draw()

def update():
    if player.lifes < 1:
        return

    updatePlayer()
    updateAsteroids()
    updatePlayerLasers()
    updateEnemies()
    updateEnemyLasers()
    updateCollisions()


def updatePlayer():
    player.x += math.sin(math.radians(player.angle - 180)) * player.v
    player.y += math.cos(math.radians(player.angle - 180)) * player.v

    if keyboard.A:
        player.angle += player.va

    if keyboard.D:
        player.angle -= player.va

    if keyboard.W:
        player.v += player.ac
        if player.v > player.maxv:
            player.v = player.maxv

    if keyboard.S:
        player.v -= player.ac
        if player.v < 0:
            player.v = 0

    if player.x > WIDTH + MARGIN:
        player.x = -MARGIN

    if player.x < -MARGIN:
        player.x = WIDTH + MARGIN

    if player.y < -MARGIN:
        player.y = HEIGHT + MARGIN

    if player.y > HEIGHT + MARGIN:
        player.y = -MARGIN


def updateAsteroids():
    if random.randint(0, 1000) <= 1:
        addAsteroid()

    for ast in asteroids:
        ast.x += math.sin(math.radians(ast.angle - 180)) * ast.v
        ast.y += math.cos(math.radians(ast.angle - 180)) * ast.v

        if ast.x > WIDTH + MARGIN:
            ast.x = -MARGIN

        if ast.x < -MARGIN:
            ast.x = WIDTH + MARGIN

        if ast.y < -MARGIN:
            ast.y = HEIGHT + MARGIN

        if ast.y > HEIGHT + MARGIN:
            ast.y = -MARGIN


def updatePlayerLasers():
    for las in playerLasers[:]:
        las.x += math.sin(math.radians(las.angle - 180)) * las.v
        las.y += math.cos(math.radians(las.angle - 180)) * las.v

        if las.x > WIDTH + MARGIN or las.x < -MARGIN:
            playerLasers.remove(las)
        elif las.y > HEIGHT + MARGIN or las.y < -MARGIN:
            playerLasers.remove(las)


def updateEnemies():
    if random.randint(0, 500) <= 1:
        addEnemy()

    for enemy in enemies:
        enemy.angle = enemy.angle_to(player.pos) - 90
        enemy.x += math.sin(math.radians(enemy.angle - 180)) * enemy.v
        enemy.y += math.cos(math.radians(enemy.angle - 180)) * enemy.v

        if random.randint(0, 500) <= 1:
            las = Actor("laser2")
            las.angle = enemy.angle
            las.x = enemy.x
            las.y = enemy.y
            las.v = random.randint(5, 10)
            enemyLasers.append(las)
            sounds.laser2.play()


def updateEnemyLasers():
    for las in enemyLasers[:]:
        las.x += math.sin(math.radians(las.angle - 180)) * las.v
        las.y += math.cos(math.radians(las.angle - 180)) * las.v

        if las.x > WIDTH + MARGIN or las.x < -MARGIN:
            enemyLasers.remove(las)
        elif las.y > HEIGHT + MARGIN or las.y < -MARGIN:
            enemyLasers.remove(las)


def updateCollisions():
    for las in playerLasers[:]:
        for met in asteroids[:]:
            if met.colliderect(las):
                asteroids.remove(met)
                playerLasers.remove(las)

    for las in enemyLasers[:]:
        for met in asteroids[:]:
            if met.colliderect(las):
                asteroids.remove(met)
                enemyLasers.remove(las)

    for las in playerLasers[:]:
        for enemy in enemies[:]:
            if enemy.colliderect(las):
                enemies.remove(enemy)
                playerLasers.remove(las)

    for las in enemyLasers[:]:
        if player.collidepoint(las.pos):
            player.lifes -= 1
            if player.lifes == 0:
                sounds.game_over.play()
            enemyLasers.remove(las)

    for enemy in enemies[:]:
        if player.collidepoint(enemy.pos):
            player.lifes -= 1
            if player.lifes == 0:
                sounds.game_over.play()
            enemies.remove(enemy)

    for ast in asteroids[:]:
        if player.collidepoint(ast.pos):
            player.lifes -= 1
            if player.lifes == 0:
                sounds.game_over.play()
            asteroids.remove(ast)


def on_key_down(key):
    if key == keys.SPACE:
        las = Actor("laser1")
        las.angle = player.angle
        las.x = player.x
        las.y = player.y
        las.v = 10
        playerLasers.append(las)
        sounds.laser1.play()


def addAsteroid():
    image = random.choice(["meteor1", "meteor2", "meteor3", "meteor4"])
    ast = Actor(image)

    side = random.randint(1, 2)
    if side == 1:
        ast.x = random.choice([-MARGIN, WIDTH + MARGIN])
        ast.y = random.randint(MARGIN, HEIGHT - MARGIN)
    else:
        ast.x = random.randint(MARGIN, WIDTH - MARGIN)
        ast.y = random.choice([-MARGIN, HEIGHT + MARGIN])
    ast.v = random.randint(2, 10)
    ast.angle = random.randint(0, 360)
    asteroids.append(ast)


def addEnemy():
    enemy = Actor("enemy")
    side = random.randint(1, 2)
    if side == 1:
        enemy.x = random.choice([-MARGIN, WIDTH + MARGIN])
        enemy.y = random.randint(MARGIN, HEIGHT - MARGIN)
    else:
        enemy.x = random.randint(MARGIN, WIDTH - MARGIN)
        enemy.y = random.choice([-MARGIN, HEIGHT + MARGIN])

    enemy.v = random.randint(2, 5)
    enemies.append(enemy)


def addTime():
    if player.lifes > 0:
        player.time += 1


clock.schedule_interval(addTime, 1)
pgzrun.go()
```