# Głodna świnia

## Wstęp

Stworzymy prostą grę, w której naszym graczem będzie świnia. Świnie, jak wiadomo, lubią jeść. Naszym celem będzie więc nakarmienie świni, a dokładniej: doprowadzenie jej do jedzenia. Na ekranie będą się pojawiać w losowych miejscach warzywa, a my będziemy tak sterować świnią, żeby zjadła jak najwięcej. Po każdym posiłku świnia będzie przyspieszać, więc gra będzie stawała się coraz trudniejsza. Koniec gry nastąpi, gdy świnia ucieknie poza ekran.

### Materiały do pobrania

#### Grafiki

Umieszczamy w katalogu **images**.

{% file src="../../.gitbook/assets/hungry_pig_images.zip" %}
Grafiki do gry Głodna Świnia
{% endfile %}

#### Dźwięki

Umieszczamy w katalogu **sounds**.

{% file src="../../.gitbook/assets/hungry_pig_sounds.zip" %}
Dźwięki do gry Głodna Świnia
{% endfile %}

#### Czcionki

Umieszczamy w katalogu **fonts**.

{% file src="../../.gitbook/assets/hungry_pig_fonts.zip" %}
Czcionki do gry Głodna Świnia
{% endfile %}

### Źródła

- [https://kenney.nl/](https://kenney.nl/)
- [https://comigo.itch.io/farm-puzzle-animals](https://comigo.itch.io/farm-puzzle-animals)
- [https://www.zapsplat.com/music/pig-squeal-close-up/](https://www.zapsplat.com/music/pig-squeal-close-up/)

## Nasz cel

![Głodna świnia - animacja](../../.gitbook/assets/hungry_pig.gif)

## Tworzymy okno gry

Zaczynamy od utworzenia okna gry i podstawowej konfiguracji projektu. Wymiary okna ustawimy na $$800\times800$$, ponieważ tak mamy przygotowaną grafikę tła (__bg.png__). Tło wyświetlimy na ekranie w części rysującej za pomocą polecenia `screen.blit()`, podając nazwę grafiki oraz współrzędne lewego górnego rogu, gdzie tło ma zostać narysowane. Możemy także ustawić tytuł naszej gry, np. "Hungry Pig", czyli z angielskiego "głodna świnia".

```python
import pgzrun
import random

TITLE = "PyGameZero Hungry Pig"
WIDTH = 800
HEIGHT = 800


def draw():
    screen.blit("bg.png", (0, 0))

def update():
    pass


pgzrun.go()
```

## Świnia

Zacznijmy od naszej głównej postaci: świni. 

### Dodajemy aktora

Jak przyjrzymy się grafikom, to zobaczymy, że mamy kilka grafik reprezentujących świnię w zależności od kierunku, w którym jest obrócona. Wykorzystamy to przy poruszaniu się świni. Na początku jednak skorzystamy z grafiki __pig_down.png__. Na górze naszego programy, zaraz pod ustawieniami wymiarów okna, tworzymy naszego nowego aktora, którego nazwiemy **pig**, za pomocą polecenia `Actor()`. Naszą postać umieścimy na początku na środku ekranu, czyli pod współrzędnymi $$(400, 400)$$.

```python
pig = Actor("pig_down")
pig.x = 400
pig.y = 400
```

### Rysujemy świnię na ekranie

W części rysującej dopisujemy instrukcję, która wyświetli naszego nowego aktora na ekranie: `pig.draw()`.

```python
def draw():
    screen.blit("bg", (0, 0))
    pig.draw()
```

### Sterowanie świnią

Naszą świnią będziemy sterować za pomocą klawiatury. Strzałkami będziemy wybierać kierunek, w którym świnia ma podążać. Nasza świnia będzie jednak poruszać się przez cały czas, podążając w ostatnio wybranym kierunku zgodnie ze swoją prędkością. Do tego będą nam potrzebne nowe zmienne, które dopiszemy do naszego aktora: 
- prędkość pozioma: **vx**,
- prędkość pionowa: **vy**,
- ogólna prędkość: **v**.

Ogólna prędkość posłuży nam do wyznaczania, jak szybko świnia ma się poruszać w wybranym kierunku. Tę wartość będziemy także zwiększać po każdym zjedzonym warzywie.

Dopisujemy więc nowe parametry do naszej świni. Aby na początku świnia stała w miejscu, prędkość poziomą i pionową ustawimy na $$0$$. Natomiast prędkość ogólną ustawimy na $$3$$, co wydaje się być dobrym poziomem startowym dla naszej gry. Oczywiście zachęcam do eksperymentowania!

```python
pig = Actor("pig_down")
pig.x = 400
pig.y = 400
pig.vx = 0
pig.vy = 0
pig.v = 3
```

Teraz czas zastosować prędkość do pozycji świni, tak aby mogła poruszać się po ekranie. W części aktualizującej usuwamy `pass` i dopisujemy dwie linijki aktualizujące pozycję świni na ekranie, poprzez dodanie prędkości do współrzędnych położenia naszego aktora.

```python
def update():
    pig.x += pig.vx
    pig.y += pig.vy
```

Oczywiście w tym momencie świnia nie będzie się jeszcze poruszać, ponieważ ustawiliśmy jej prędkości na $$0$$. Warto dla testów tymczasowo zmienić prędkości **vx** i **vy**, a następnie uruchomić grę by sprawdzić, czy wszystko działa poprawnie.

Teraz czas wreszcie dodać obsługę sterowania. W tym celu będziemy potrzebowali nowej funkcji, która pozwoli nam reagować na zdarzenia wciśnięcia klawisza na klawiaturze: `on_key_down(key)`. Dopiszemy ją na dole naszego programu, pod funkcją `update`, ale przed poleceniem `pgzrun.go()`. Wewnątrz funkcji będziemy reagować na kliknięcia przycisków na klawiaturze. W zależności od klikniętego przycisku, będziemy wykonywać inne operacje. Jeżeli kliknięta zostanie np. strzałka w lewo, to ustawimy prędkość poziomą **vx** świni na **-v**, wyzerujemy prędkość pionową i zmienimy grafikę na __pig_left.png__.

```python
def on_key_down(key):
    if key == keys.LEFT:
        pig.vx = -pig.v
        pig.vy = 0
        pig.image = "pig_left"
```

Podobnie postępujemy z pozostałymi kierunkami, odpowiednio zmieniając prędkości świni i jej grafikę.

```python
def on_key_down(key):
    if key == keys.LEFT:
        pig.vx = -pig.v
        pig.vy = 0
        pig.image = "pig_left"

    if key == keys.RIGHT:
        pig.vx = pig.v
        pig.vy = 0
        pig.image = "pig_right"

    if key == keys.UP:
        pig.vx = 0
        pig.vy = -pig.v
        pig.image = "pig_up"

    if key == keys.DOWN:
        pig.vx = 0
        pig.vy = pig.v
        pig.image = "pig_down"
```

### Pełen kod

```python
import pgzrun
import random

TITLE = "Hungry Pig"
WIDTH = 800
HEIGHT = 800

pig = Actor("pig_down")
pig.x = 400
pig.y = 400
pig.vx = 0
pig.vy = 0
pig.v = 3


def draw():
    screen.blit("bg", (0, 0))
    pig.draw()


def update():
    pig.x += pig.vx
    pig.y += pig.vy


def on_key_down(key):
    if key == keys.LEFT:
        pig.vx = -pig.v
        pig.vy = 0
        pig.image = "pig_left"

    if key == keys.RIGHT:
        pig.vx = pig.v
        pig.vy = 0
        pig.image = "pig_right"

    if key == keys.UP:
        pig.vx = 0
        pig.vy = -pig.v
        pig.image = "pig_up"

    if key == keys.DOWN:
        pig.vx = 0
        pig.vy = pig.v
        pig.image = "pig_down"


pgzrun.go()
```

## Buraki

Nasza świnia będzie żywić się burakami. Na ekranie zawsze będzie dokładnie jeden burak. Gdy świnia zje buraka, ten pojawi się ponownie w nowym, losowym miejscu na ekranie.

### Dodajemy aktora

Naszego aktora zapiszemy w zmiennej `beet`. Utworzymy go na podstawie grafiki __beetroot.png__ i początkowo umieścimy w dowolnym miejscu na ekranie, np. pod współrzędnymi $$(200, 200)$$.

```python
beet = Actor("beetroot")
beet.x = 200
beet.y = 200
```

### Rysujemy buraka na ekranie

W części rysującej dopisujemy instrukcję, która wyświetli naszego nowego aktora na ekranie: `beet.draw()`.

```python
def draw():
    screen.blit("bg", (0, 0))
    pig.draw()
    beet.draw()
```

### Zjadanie buraków

Podczas poruszania się po ekranie, gdy świnia wejdzie w kolizję z burakiem, to go zje. Po zjedzeniu buraka świnia powinna przyspieszyć, wydać odpowiedni odgłos, a sam burak powinien przemieścić się w losowe miejsce na ekranie.

W celu stwierdzenia, że świnia jest w kolizji z burakiem, skorzystamy z instrukcji **colliderect**:

```python
if pig.colliderect(beet):
```

Wszystko będziemy zapisywać w części aktualizującej **update**, zaraz pod zmianą pozycji świni.

Po wykryciu kolizji zacznijmy od przemieszczenia buraka w losowe miejsce. Osobno wylosujemy nowe wartości dla współrzędnych $$x$$ oraz $$y$$. Aby jednak burak nie pojawił się na brzegu ekranu, warto zadbać o odpowiedni margines, np $$50$$ pikseli. W celu wylosowania wartości skorzystamy z biblioteki **random** oraz funkcji **randint**, do której, jako argumenty, przekazujemy przedział, z jakiego chcemy wylosować wartość.

```python
beet.x = random.randint(50, WIDTH - 50)
beet.y = random.randint(50, HEIGHT - 50)
```

Następnie zwiększamy prędkość świni. W tym celu modyfikujemy parametr **v**, dodając do niego jakąś niewielką liczbę, np. $$0.8$$. Warto poeksperymentować z różnymi wartościami by dobrać odpowiedni dla siebie poziom trudności.

```python
pig.v += 0.8
```

Na koniec warto jeszcze dodać efekty dźwiękowe.

```python
sounds.pig.play()
```

Cały kod stwierdzający kolizję z burakiem prezentuje się następująco:

```python
if pig.colliderect(beet):
    beet.x = random.randint(50, WIDTH - 50)
    beet.y = random.randint(50, HEIGHT - 50)
    pig.v += 0.8
    pig.points += 1
    sounds.pig.play()
```

Umieszczamy naszą instrukcję w części aktualizującej.

```python
def update():
    pig.x += pig.vx
    pig.y += pig.vy

    if pig.colliderect(beet):
        beet.x = random.randint(50, WIDTH - 50)
        beet.y = random.randint(50, HEIGHT - 50)
        pig.v += 0.8
        pig.points += 1
        sounds.pig.play()
```

### Pełen kod

```python
import pgzrun
import random

TITLE = "Hungry Pig"
WIDTH = 800
HEIGHT = 800

pig = Actor("pig_down")
pig.x = 400
pig.y = 400
pig.vx = 0
pig.vy = 0
pig.v = 3

beet = Actor("beetroot")
beet.x = 200
beet.y = 200


def draw():
    screen.blit("bg", (0, 0))
    pig.draw()
    beet.draw()


def update():
    pig.x += pig.vx
    pig.y += pig.vy

    if pig.colliderect(beet):
        beet.x = random.randint(50, WIDTH - 50)
        beet.y = random.randint(50, HEIGHT - 50)
        pig.v += 0.8
        sounds.pig.play()


def on_key_down(key):
    if key == keys.LEFT:
        pig.vx = -pig.v
        pig.vy = 0
        pig.image = "pig_left"

    if key == keys.RIGHT:
        pig.vx = pig.v
        pig.vy = 0
        pig.image = "pig_right"

    if key == keys.UP:
        pig.vx = 0
        pig.vy = -pig.v
        pig.image = "pig_up"

    if key == keys.DOWN:
        pig.vx = 0
        pig.vy = pig.v
        pig.image = "pig_down"


pgzrun.go()
```

## Punkty

Cóż to za gra bez punktów! Dodanie jednak punktów do naszej gry to żaden problem. Punkty będziemy dostawać za każdego zjedzonego buraka. Na początku dopisujemy punkty w postaci nowej zmiennej **points** do naszej świni. Początkowo punkty ustawiamy na $$0$$.

```python
pig.points = 0
```

### Wyświetlamy punkty

Zanim przejdziemy do zliczania punktów, wyświetlmy je na ekranie gry. W tym celu, w części rysującej **draw**, dopisujemy polecenie `screen.draw.text`. Jako parametry podamy tekst do wyświetlenia, czyli nasze punkty zamienione na tekst, a także pozycję tekstu na ekranie (**center**), rozmiar czcionki (**fontsize**), kolor tekstu (**color**) oraz nazwę czcionki (**fontname**).

```python
screen.draw.text(f"{pig.points}", center=(WIDTH / 2, 50), fontsize=60, color="#fdee00", fontname="kenney_bold")
```

Polecenie dopisujemy na koniec części rysujacej.

```python
def draw():
    screen.blit("bg", (0, 0))
    pig.draw()
    beet.draw()
    screen.draw.text(f"{pig.points}", center=(WIDTH / 2, 50), fontsize=60, color="#fdee00", fontname="kenney_bold")
```

### Zliczamy punkty

Jak już ustaliliśmy, punkty będziemy dostawać za każdego zjedzonego buraka. W takim razie, do części, w której wykrywamy kolizję z burakiem, dopisujemy zwiększanie punktów: `pig.points += 1`. Warto to dopisać zaraz pod zwiększeniem prędkości świni, tak aby zachować czytelność kodu, ale kolejność nie ma dużego znaczenia.

```python
if pig.colliderect(beet):
    beet.x = random.randint(50, WIDTH - 50)
    beet.y = random.randint(50, HEIGHT - 50)
    pig.v += 0.8
    pig.points += 1
    sounds.pig.play()
```

### Pełen kod

```python
import pgzrun
import random

TITLE = "Hungry Pig"
WIDTH = 800
HEIGHT = 800

pig = Actor("pig_down")
pig.x = 400
pig.y = 400
pig.vx = 0
pig.vy = 0
pig.v = 3
pig.points = 0

beet = Actor("beetroot")
beet.x = 200
beet.y = 200


def draw():
    screen.blit("bg", (0, 0))
    pig.draw()
    beet.draw()
    screen.draw.text(f"{pig.points}", center=(WIDTH / 2, 50), fontsize=60, color="#fdee00", fontname="kenney_bold")
    

def update():
    pig.x += pig.vx
    pig.y += pig.vy

    if pig.colliderect(beet):
        beet.x = random.randint(50, WIDTH - 50)
        beet.y = random.randint(50, HEIGHT - 50)
        pig.v += 0.8
        pig.points += 1
        sounds.pig.play()


def on_key_down(key):
    if key == keys.LEFT:
        pig.vx = -pig.v
        pig.vy = 0
        pig.image = "pig_left"

    if key == keys.RIGHT:
        pig.vx = pig.v
        pig.vy = 0
        pig.image = "pig_right"

    if key == keys.UP:
        pig.vx = 0
        pig.vy = -pig.v
        pig.image = "pig_up"

    if key == keys.DOWN:
        pig.vx = 0
        pig.vy = pig.v
        pig.image = "pig_down"


pgzrun.go()
```

## Koniec gry

Cóż to za gra, która się nie kończy? Nasza gra będzie kończyć się, gdy świnia wyjdzie poza ekran. W celu zapamiętania, że gra się już zakończyła, dopiszemy do świni nową zmienną **dead** którą na początku ustawimy na wartość **False**.

```python
pig = Actor("pig_down")
pig.x = 400
pig.y = 400
pig.vx = 0
pig.vy = 0
pig.v = 3
pig.points = 0
pig.dead = False
```

### Wyświetlamy komunikat

Zacznijmy od wyświetlenia na ekranie komunikatu o zakończeniu gry. W części rysującej, gdy gra jest zakończona, tzn. gdy zmienna `pig.dead` ma wartość **True**, wyświetlimy na ekranie komunikat **GAME OVER**.

```python
if pig.dead:
    screen.draw.text(f"GAME OVER", center=(WIDTH / 2, HEIGHT / 2), fontsize=70, color="#e30022", fontname="kenney_bold")
```

Całość dopisujemy na koniec części rysującej.

```python
def draw():
    screen.blit("bg", (0, 0))
    pig.draw()
    beet.draw()
    screen.draw.text(f"{pig.points}", center=(WIDTH / 2, 50), fontsize=60, color="#fdee00", fontname="kenney_bold")
    if pig.dead:
        screen.draw.text(f"GAME OVER", center=(WIDTH / 2, HEIGHT / 2), fontsize=70, color="#e30022", fontname="kenney_bold")
```

Warto przetestować, czy komunikat wyświetla się poprawnie, tymczasowo zmieniając wartość zmiennej `pig.dead` na **True**.

### Sprawdzamy wyjście poza ekran

Nasza gra się kończy, gdy świnia wyjdzie poza ekran gry. Aby sprawdzić, czy tak się stało, wystarczy sprawdzić wartości współrzędnych naszej świni. Jeżeli są mniejsze od zera, albo większe od odpowiednio szerokości i wysokości, to znaczy, że świnia wyszła poza ekran. Dopisujemy więc odpowiedni warunek na koniec części aktualizującej.

```python
if pig.x < 0 or pig.x > WIDTH or pig.y < 0 or pig.y > HEIGHT:
```

Gdy świnia wyjdzie poza ekran to gra się kończy, ustawiamy więc zmienną `pig.dead` na wartość **True**.

```python
if pig.x < 0 or pig.x > WIDTH or pig.y < 0 or pig.y > HEIGHT:
    pig.dead = True
```

Dla lepszego efektu możemy także przemieścić świnię zaraz nad napis **GAME OVER** i zmienić jej grafikę na __pig_dead.png__.

```python
if pig.x < 0 or pig.x > WIDTH or pig.y < 0 or pig.y > HEIGHT:
    pig.dead = True
    pig.x = WIDTH / 2
    pig.y = HEIGHT / 3
    pig.image = "pig_dead"
```

Tak teraz powinna wyglądać nasza część aktualizująca:

```python
def update():
    pig.x += pig.vx
    pig.y += pig.vy

    if pig.colliderect(beet):
        beet.x = random.randint(50, WIDTH - 50)
        beet.y = random.randint(50, HEIGHT - 50)
        pig.v += 0.8
        pig.points += 1
        sounds.pig.play()

    if pig.x < 0 or pig.x > WIDTH or pig.y < 0 or pig.y > HEIGHT:
        pig.dead = True
        pig.x = WIDTH / 2
        pig.y = HEIGHT / 3
        pig.image = "pig_dead"
```

### Zamrożenie rozgrywki

Gdy teraz przetestujemy naszą grę, to zauważymy, że rozgrywka dalej się toczy po zakończeniu gry, tzn. dalej można poruszać świnią i zjadać buraki. Oczywiście nie chcemy, by tak się działo. W tym celu należy dopisać prostą instrukcję warunkową na początek części aktualizującej, a także na początek części odpowiedzialnej za odczytywanie klikniętych przycisków z klawiatury.

```python
if pig.dead:
    return
```

Dzięki temu, jeżeli gra jest już zakończona, to żadne dalsze instrukcje w danej części nie będą już wykonywane.

### Pełen kod

```python
import pgzrun
import random

TITLE = "Hungry Pig"
WIDTH = 800
HEIGHT = 800

pig = Actor("pig_down")
pig.x = 400
pig.y = 400
pig.vx = 0
pig.vy = 0
pig.v = 3
pig.points = 0
pig.dead = False

beet = Actor("beetroot")
beet.x = 200
beet.y = 200


def draw():
    screen.blit("bg", (0, 0))
    pig.draw()
    beet.draw()
    screen.draw.text(f"{pig.points}", center=(WIDTH / 2, 50), fontsize=60, color="#fdee00", fontname="kenney_bold")
    if pig.dead:
        screen.draw.text(f"GAME OVER", center=(WIDTH / 2, HEIGHT / 2), fontsize=70, color="#e30022", fontname="kenney_bold")
    

def update():
    if pig.dead:
        return

    pig.x += pig.vx
    pig.y += pig.vy

    if pig.colliderect(beet):
        beet.x = random.randint(50, WIDTH - 50)
        beet.y = random.randint(50, HEIGHT - 50)
        pig.v += 0.8
        pig.points += 1
        sounds.pig.play()

    if pig.x < 0 or pig.x > WIDTH or pig.y < 0 or pig.y > HEIGHT:
        pig.dead = True
        pig.x = WIDTH / 2
        pig.y = HEIGHT / 3
        pig.image = "pig_dead"


def on_key_down(key):
    if pig.dead:
        return

    if key == keys.LEFT:
        pig.vx = -pig.v
        pig.vy = 0
        pig.image = "pig_left"

    if key == keys.RIGHT:
        pig.vx = pig.v
        pig.vy = 0
        pig.image = "pig_right"

    if key == keys.UP:
        pig.vx = 0
        pig.vy = -pig.v
        pig.image = "pig_up"

    if key == keys.DOWN:
        pig.vx = 0
        pig.vy = pig.v
        pig.image = "pig_down"


pgzrun.go()
```