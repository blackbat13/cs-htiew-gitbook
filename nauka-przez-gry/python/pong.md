# Pong

## Wstęp

Klasyczną grę Pong stworzoną przez firmę Atari zna chyba każdy. Dwie paletki po przeciwległych brzegach ekranu, piłka odbijająca się od paletek - ta prosta w swoich założeniach gra była jednak czymś przełomowym w swoich czasach.

Dzisiaj spróbujemy tę grę odtworzyć w trochę bardziej współczesnym środowisku i z odświeżoną grafiką. Do dzieła!

### Czego się nauczysz

* Obsługi dwóch graczy jednocześnie
* Symulacji prostej fizyki odbijania się piłki
* Obsługi zakończenia gry i wyświetlenia wyniku

### Grafiki do pobrania

Zanim zaczniemy, pobierz poniższe grafiki, rozpakuj i umieść w katalogu **images **w projekcie gry.

{% file src="../../.gitbook/assets/grafiki_pong.zip" %}
Grafiki do gry Pong
{% endfile %}

## Wersja klasyczna

Zaczniemy od stworzenia klasycznej wersji gry Pong. Na początek przyjrzyjmy się temu, co jest naszym celem.

![Pong - wersja klasyczna](../../.gitbook/assets/pongGame.gif)

Spróbujmy przeanalizować powyższą animację. Zacznijmy od wyróżniania elementów graficznych:

* Szare tło
* Żółta linia po środku dzieląca planszę na dwie części
* Punkty wyświetlane na górze ekranu
* Dwie paletki - jedna przy lewym brzegu, druga przy prawym
* Piłka

### Szablon

Jak zwykle zaczynamy od standardowego szablonu. Jako wymiary gry przyjmiemy 800x600 (szerokość 800 i wysokość 600).

Ustalmy także tytuł naszej gry: "Pong".

```python
import pgzrun


WIDTH = 800
HEIGHT = 600

TITLE = "PONG"


def draw():
    pass
    
    
def update():
    pass
    
    
pgzrun.go()
```

### Określamy tło gry

Zacznijmy od rzeczy prostej - tła gry. Jak już ustaliliśmy na tło składa się szary kolor i żółta linia na środku ekranu. Zacznijmy od szarego koloru. Dla ułatwienia zapamiętamy go w zmiennej `kolor_tla`, którą dodamy zaraz pod tytułem gry. Chcemy mieć lekki odcień szarości.

```python
kolor_tla = (64, 64, 64)
```

Jak już mamy kolor, to wypełnijmy nim całe tło. Dodajemy instrukcję `screen.fill` w części rysującej.

```python
def draw():
    screen.fill(kolor_tla)
```

Mamy kolor tła, teraz dodajmy żółtą linię. W tym celu użyjemy polecenia screen.draw.line do narysowania linii. Żeby narysować linię musimy podać jej początek i koniec, a także kolor. Gdybyśmy chcieli narysować żółtą linię przez cały ekran, wyglądałoby to tak:

```python
screen.draw.line((WIDTH / 2, 0), (WIDTH / 2, HEIGHT), color = "yellow")
```

Teraz dostosujmy naszą linię, dodając niewielkie marginesy: 40 pikseli z góry i z dołu.

```python
screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
```

Oczywiście, żeby narysować linię na ekraniu, musimy dopisać powyższe polecenie w części rysującej, zaraz pod wypełnieniem ekranu kolorem tła.

```python
def draw():
    screen.fill(kolor_tla)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
```

Nasz pełny kod przedstawia się teraz następująco:

```python
import pgzrun


WIDTH = 800
HEIGHT = 600

TITLE = "PONG"

kolor_tla = (64, 64, 64)


def draw():
    screen.fill(kolor_tla)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
    
    
def update():
    pass
    
    
pgzrun.go()
```

### Pełna gra

```python
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

# Tytuł gry
TITLE = 'Pong'

# Główny kolor elementów gry
kolor = 'yellow'
kolor_tla = (64, 64, 64)

# Tworzymy aktora lewej paletki
lewa = Actor("lewa.png")
lewa.x = 20
lewa.y = HEIGHT / 2
lewa.wynik = 0
lewa.wygrana = False

# Tworzymy aktora prawej paletki
prawa = Actor("prawa.png")
prawa.x = WIDTH - 20
prawa.y = HEIGHT / 2
prawa.wynik = 0
prawa.wygrana = False

# Tworzymy aktora piłki
# Piłka ma określoną prędkość poruszania się
# A także informację o tym, czy gra została zakończona
pilka = Actor("pilka.png")
pilka.x = WIDTH / 2
pilka.y = HEIGHT / 2
pilka.px = 5
pilka.py = 5
pilka.koniec_gry = False


def draw():
    screen.fill(kolor_tla)

    if pilka.koniec_gry:
        wypisz_wynik()
    else:
        lewa.draw()
        prawa.draw()
        pilka.draw()
        wypisz_punkty()

        # Eysujemy linię dzielącą pole gry
        screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color=kolor)

# Wypisujemy wynik końca gry
def wypisz_wynik():
  if lewa.wygrana:
      screen.draw.text("LEWY WYGRYWA!!!",
                        color=kolor,
                        center=(WIDTH / 2, HEIGHT / 2),
                        fontsize=96)
  else:
      screen.draw.text("PRAWY WYGRYWA!!!",
                        color=kolor,
                        center=(WIDTH / 2, HEIGHT / 2),
                        fontsize=96)

# Wypisujemy na ekranie punkty graczy
def wypisz_punkty():
    # Wypisujemy wynik lewego gracza
    screen.draw.text("Lewy: " + str(lewa.wynik),
                     color=kolor,
                     center=(WIDTH / 4 - 20, 20),
                     fontsize=48)

    # Wypisujemy wynik prawego gracza
    screen.draw.text('Prawy: ' + str(prawa.wynik),
                     color=kolor,
                     center=(WIDTH / 2 + WIDTH / 4 - 20, 20),
                     fontsize=48)


# Aktualizujemy stan gry - ruchy graczy i piłki
def update():
    # Jeżeli gra nie została jeszcze zakończona
    if not pilka.koniec_gry:
        # Odczytujemy ruchy graczy
        ruch_graczy()

        # Poruszamy piłkę
        ruch_pilki()


# Odczytujemy ruchy graczy
def ruch_graczy():
    # Prawy gracz porusza się za pomocą strzałek góra i dół
    if keyboard.up and prawa.top > 40:
        prawa.y -= 5

    if keyboard.down and prawa.bottom < HEIGHT - 40:
        prawa.y += 5

    # Lewy gracz porusza się za pomocą klawiszy w i s
    if keyboard.w and lewa.top > 40:
        lewa.y -= 5

    if keyboard.s and lewa.bottom < HEIGHT - 40:
        lewa.y += 5


# Resetujemy pozycję piłki
def resetuj_pilke():
    pilka.left = WIDTH // 2
    pilka.top = HEIGHT // 2
    pilka.px = random.choice([-5, 5])
    pilka.py = random.choice([-5, 5])


# Obliczamy ruch piłki i ją przemieszczamy
def ruch_pilki():
    # Przemieszczamy piłkę zgodnie z jej prędkością
    pilka.left += pilka.px
    pilka.top += pilka.py

    # Odbijamy piłkę od górnej ściany
    if pilka.top <= 40:
        pilka.py *= -1

    # Odbijamy piłkę od dolnej ściany
    if pilka.bottom >= HEIGHT - 40:
        pilka.py *= -1

    # Odbijamy piłkę od lewej paletki
    if lewa.colliderect(pilka):
        pilka.px *= -1

    # Odpijamy piłkę od prawej paletki
    if prawa.colliderect(pilka):
        pilka.px *= -1

    # Jeżeli piłka wypadła z lewej strony, to prawy gracz dostaje punkt
    if pilka.left <= 0:
        resetuj_pilke()
        prawa.wynik += 1

        # Jeżeli prawa paletka uzyskała 11 punktów to wygrywa i gra się kończy
        if prawa.wynik == 11:
            prawa.wygrana = True
            pilka.koniec_gry = True

    # Jeżeli piłka wypadła z prawej strony, to lewy graczdostaje punkt
    if pilka.right >= WIDTH:
        resetuj_pilke()
        lewa.wynik += 1

        # Jeżeli lewa paletka uzyskała 11 punktów to wygrywa i gra się kończy
        if lewa.wynik == 11:
            lewa.wygrana = True
            pilka.koniec_gry = True

pgzrun.go()
```

### Testujemy działanie

TODO

## Wersja z bonusami

TODO

### Pełny program

```python
import random
import pgzrun
import pygame

WIDTH = 800
HEIGHT = 600

# Tytuł gry
TITLE = 'Pong'

# Główny kolor elementów gry
kolor = 'yellow'
kolor_tla = (64, 64, 64)

# Tworzymy aktorów - lewą paletkę, prawą paletkę i piłkę
# Paletki mają początkową pozycję i wynik
lewa = Actor("lewa.png")
lewa.left = 10
lewa.top = HEIGHT / 2
lewa.wynik = 0

prawa = Actor("prawa.png")
prawa.right = WIDTH - 10
prawa.top = HEIGHT / 2
prawa.wynik = 0

# Piłka ma jeszcze określoną prędkość poruszania się
# A także informację o tym, czy gra została zakończona
pilka = Actor("pilka.png")
pilka.left = WIDTH / 2
pilka.top = HEIGHT / 2
pilka.px = 5
pilka.py = 5
pilka.koniec_gry = False
pilka.czas = 0

bonus = Actor("bonus.png")
bonus.aktywny = False


def draw():
    screen.fill(kolor_tla)

    if lewa.wynik == 11:
        screen.draw.text(
            "LEWY WYGRYWA!!!",
            color=kolor,
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=96
        )
        pilka.koniec_gry = True
    elif prawa.wynik == 11:
        screen.draw.text(
            "PRAWY WYGRYWA!!!",
            color=kolor,
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=96
        )
        pilka.koniec_gry = True
    else:
        lewa.draw()
        prawa.draw()
        pilka.draw()

    # Wypisujemy wynik lewego gracza
    screen.draw.text(
        "Lewy: " + str(lewa.wynik),
        color=kolor,
        center=(WIDTH / 4 - 20, 20),
        fontsize=48
    )

    # Wypisujemy wynik prawego gracza
    screen.draw.text(
        'Prawy: ' + str(prawa.wynik),
        color=kolor,
        center=(WIDTH / 2 + WIDTH / 4 - 20, 20),
        fontsize=48
    )

    # Rysujemy linię dzielącą pole gry
    screen.draw.line(
        (WIDTH / 2, 40),
        (WIDTH / 2, HEIGHT - 40),
        color=kolor)

    # Wypisujemy czas gry na ekranie
    screen.draw.text(
        str(pilka.czas),
        color=kolor,
        center=(WIDTH / 2, HEIGHT - 20),
        fontsize=30
    )

    if bonus.aktywny:
        bonus.draw()


# Aktualizujemy stan gry - ruchy graczy i piłki
def update():
    # Jeżeli gra nie została jeszcze zakończona
    if not pilka.koniec_gry:
        # Odczytujemy ruchy graczy
        ruch_graczy()

        # Poruszamy piłkę
        ruch_pilki()


# Odczytujemy ruchy graczy
def ruch_graczy():
    # Prawy gracz porusza się za pomocą strzałek góra i dół
    if keyboard.up:
        if prawa.top - 5 > 40:
            prawa.top -= 5
    elif keyboard.down:
        if prawa.bottom + 5 < HEIGHT - 40:
            prawa.top += 5

    # Lewy gracz porusza się za pomocą klawiszy w i s
    if keyboard.w:
        if lewa.top - 5 > 40:
            lewa.top -= 5
    elif keyboard.s:
        if lewa.bottom + 5 < HEIGHT - 40:
            lewa.top += 5


# Resetujemy pozycję piłki
def resetuj_pilke():
    pilka.left = WIDTH // 2
    pilka.top = HEIGHT // 2
    pilka.px = random.choice([-5, 5])
    pilka.py = random.choice([-5, 5])


# Obliczamy ruch piłki i ją przemieszczamy
def ruch_pilki():
    # Przemieszczamy piłkę zgodnie z jej prędkością
    pilka.left += pilka.px
    pilka.top += pilka.py

    # Odbijamy od ścian - góra i dół
    if pilka.top <= 40:
        pilka.py *= -1

    if pilka.bottom >= HEIGHT - 40:
        pilka.py *= -1

    # Odbijamy od paletek
    if lewa.colliderect(pilka):
        # Aby zapobiec "gliczowaniu" się piłki w paletce, sprawdzamy, czy piłka przekroczyła granicę paletki
        # Jeżeli tak, to ją resetujemy i przyznajemy punkt
        if pilka.x < lewa.x + 12:
            resetuj_pilke()
            prawa.wynik += 1
            return

        # Jeżeli piłka dotyka brzegu paletki, to odbijamy ją ze zwiększoną prędkością
        if abs(pilka.y - (lewa.y - 52)) < 30 or abs(pilka.y - (lewa.y + 52)) < 30:
            pilka.px *= -1.2
        else:
            pilka.px *= -1

    if prawa.colliderect(pilka):
        if pilka.x > prawa.x - 12:
            resetuj_pilke()
            lewa.wynik += 1
            return
        if abs(pilka.y - (prawa.y - 52)) < 30 or abs(pilka.y - (prawa.y + 52)) < 30:
            pilka.px *= -1.2
        else:
            pilka.px *= -1

    # Jeżeli piłka wypadła poza ekran, to jeden z graczy dostaje punkt
    if pilka.left <= 0:
        resetuj_pilke()
        prawa.wynik += 1

    if pilka.right >= WIDTH:
        resetuj_pilke()
        lewa.wynik += 1

    # Jeżeli piłka wpadła na bonus i bonus jest aktywny
    if pilka.colliderect(bonus) and bonus.aktywny:
        # Jeżeli piłka jest po lewej stronie planszy, to lewy gracz dostaje punkt
        if pilka.x < WIDTH / 2:
            lewa.wynik += 1
        else:
            # W przeciwnym wypadku, piłka jest po prawej stronie ekranu i prawy gracz dostaje punkt
            prawa.wynik += 1

        # Dezaktywujemy bonus
        bonus.aktywny = False
        skaluj(pilka, 50, 50)
        clock.schedule(przywroc_pilke, 5.0)


# Aktualizujemy czas przypisany do piłki
def aktualizuj_czas():
    pilka.czas += 1


# Aktualizujemy bonus
def aktualizuj_bonus():
    bonus.x = random.randint(40, WIDTH - 40)
    bonus.y = random.randint(30, HEIGHT - 30)
    bonus.aktywny = True
    clock.schedule(aktualizuj_bonus, random.uniform(3.0, 10.0))


# Skalujemy aktora do nowych wymiarów
def skaluj(aktor, szerokosc, wysokosc):
    aktor._surf = pygame.transform.scale(aktor._surf, (szerokosc, wysokosc))
    aktor._update_pos()


# Przywracamy normalny rozmiar piłki
def przywroc_pilke():
    skaluj(pilka, 22, 22)


# Uruchamiamy aktualizację czasu co jedną sekundę
clock.schedule_interval(aktualizuj_czas, 1.0)
# Pierwszy bonus pojawi się po 5 sekundach
clock.schedule(aktualizuj_bonus, 5.0)
pgzrun.go()

```

### Testujemy działanie

TODO

## Przeciwko komputerowi

TODO

### Pełny program

```python
import random
import pgzrun

WIDTH = 800
HEIGHT = 600

# Tytuł gry
TITLE = 'Pong'

# Główny kolor elementów gry
kolor = 'yellow'
kolor_tla = (64, 64, 64)

# Tworzymy aktorów - lewą paletkę, prawą paletkę i piłkę
# Paletki mają początkową pozycję i wynik
lewa = Actor("lewa.png")
lewa.left = 10
lewa.top = HEIGHT / 2
lewa.wynik = 0

prawa = Actor("prawa.png")
prawa.right = WIDTH - 10
prawa.top = HEIGHT / 2
prawa.wynik = 0

# Piłka ma jeszcze określoną prędkość poruszania się
# A także informację o tym, czy gra została zakończona
pilka = Actor("pilka.png")
pilka.left = WIDTH / 2
pilka.top = HEIGHT / 2
pilka.px = 5
pilka.py = 5
pilka.koniec_gry = False


def draw():
    screen.fill(kolor_tla)

    if lewa.wynik == 11:
        screen.draw.text(
            "LEWY WYGRYWA!!!",
            color=kolor,
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=96
        )
        pilka.koniec_gry = True
    elif prawa.wynik == 11:
        screen.draw.text(
            "PRAWY WYGRYWA!!!",
            color=kolor,
            center=(WIDTH / 2, HEIGHT / 2),
            fontsize=96
        )
        pilka.koniec_gry = True
    else:
        lewa.draw()
        prawa.draw()
        pilka.draw()

    # Wypisujemy wynik lewego gracza
    screen.draw.text(
        "Lewy: " + str(lewa.wynik),
        color=kolor,
        center=(WIDTH / 4 - 20, 20),
        fontsize=48
    )

    # Wypisujemy wynik prawego gracza
    screen.draw.text(
        'Prawy: ' + str(prawa.wynik),
        color=kolor,
        center=(WIDTH / 2 + WIDTH / 4 - 20, 20),
        fontsize=48
    )

    # Eysujemy linię dzielącą pole gry
    screen.draw.line(
        (WIDTH / 2, 40),
        (WIDTH / 2, HEIGHT - 40),
        color=kolor)


# Aktualizujemy stan gry - ruchy graczy i piłki
def update():
    # Jeżeli gra nie została jeszcze zakończona
    if not pilka.koniec_gry:
        # Odczytujemy ruchy graczy
        ruch_graczy()

        # Poruszamy piłkę
        ruch_pilki()


# Odczytujemy ruchy graczy
def ruch_graczy():
    # Prawy gracz porusza się za pomocą strzałek góra i dół
    if keyboard.up:
        if prawa.top - 5 > 40:
            prawa.top -= 5
    elif keyboard.down:
        if prawa.bottom + 5 < HEIGHT - 40:
            prawa.top += 5

    # Lewy gracz porusza się automatycznie
    if lewa.y > pilka.y:
        if lewa.top - 5 > 40:
            lewa.top -= 5
    elif lewa.y < pilka.y:
        if lewa.bottom + 5 < HEIGHT - 40:
            lewa.top += 5


# Resetujemy pozycję piłki
def resetuj_pilke():
    pilka.left = WIDTH // 2
    pilka.top = HEIGHT // 2
    pilka.px = random.choice([-5, 5])
    pilka.py = random.choice([-5, 5])


# Obliczamy ruch piłki i ją przemieszczamy
def ruch_pilki():
    # Przemieszczamy piłkę zgodnie z jej prędkością
    pilka.left += pilka.px
    pilka.top += pilka.py

    # Odbijamy od ścian - góra i dół
    if pilka.top <= 40:
        pilka.py *= -1

    if pilka.bottom >= HEIGHT - 40:
        pilka.py *= -1

    # Odbijamy od paletek
    if lewa.colliderect(pilka):
        pilka.px *= -1

    if prawa.colliderect(pilka):
        pilka.px *= -1

    # Jeżeli piłka wypadła poza ekran, to jeden z graczy dostaje punkt
    if pilka.left <= 0:
        resetuj_pilke()
        prawa.wynik += 1

    if pilka.right >= WIDTH:
        resetuj_pilke()
        lewa.wynik += 1


pgzrun.go()
```

### Testujemy działanie

TODO

## Zadania dodatkowe

TODO

