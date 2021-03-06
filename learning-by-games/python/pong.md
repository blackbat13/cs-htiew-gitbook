# Pong

## Wstęp

Klasyczną grę Pong stworzoną przez firmę Atari zna chyba każdy. Dwie paletki po przeciwległych brzegach ekranu, piłka odbijająca się od paletek - ta prosta w swoich założeniach gra była jednak czymś przełomowym w swoich czasach.

Dzisiaj spróbujemy tę grę odtworzyć w trochę bardziej współczesnym środowisku i z odświeżoną grafiką. Do dzieła!

### Czego się nauczysz

* Obsługi dwóch graczy jednocześnie
* Symulacji prostej fizyki odbijania się piłki
* Obsługi zakończenia gry i wyświetlenia wyniku

### Grafiki do pobrania

Zanim zaczniemy, pobierz poniższe grafiki, rozpakuj i umieść w katalogu **images** w projekcie gry.

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

## Podstawowy szablon

Jak zwykle zaczynamy od standardowego szablonu. Jako wymiary gry przyjmiemy $$800\times600$$ (szerokość $$800$$ i wysokość $$600$$).

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

## Tło gry

Na początek rzecz prosta - tło gry. Jak już ustaliliśmy na tło składa się szary kolor i żółta linia na środku ekranu. Zacznijmy od szarego koloru. 

### Szare tło

Dla ułatwienia kolor tła zapamiętamy w zmiennej `kolor_tla`, którą dodamy zaraz pod tytułem gry. Chcemy mieć lekki odcień szarości.
W tym celu ustalamy kolor za pomocą trzech wartości: **(R, G, B)**.
W celu uzyskania odcieniu szarości wystarczy podać trzy takie same liczby, np. $$64$$.

```python
kolor_tla = (64, 64, 64)
```

Jak już mamy kolor, to wypełnijmy nim całe tło. Dodajemy instrukcję `screen.fill` w części rysującej.

```python
def draw():
    screen.fill(kolor_tla)
```

### Żółta linia

Mamy kolor tła, teraz dodajmy żółtą linię. W tym celu użyjemy polecenia screen.draw.line do narysowania linii. 
Żeby narysować linię musimy podać jej początek i koniec, a także kolor. 
Gdybyśmy chcieli narysować żółtą linię przez cały ekran, wyglądałoby to tak:

```python
screen.draw.line((WIDTH / 2, 0), (WIDTH / 2, HEIGHT), color = "yellow")
```

Teraz dostosujmy naszą linię, dodając niewielkie marginesy: $$40$$ pikseli z góry i z dołu.

```python
screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
```

Oczywiście, żeby narysować linię na ekraniu, musimy dopisać powyższe polecenie w części rysującej, zaraz pod wypełnieniem ekranu kolorem tła.

```python
def draw():
    screen.fill(kolor_tla)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
```

### Pełny kod

Dotychczasowy pełny kod naszej gry przedstawiony jest poniżej.

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

## Aktorzy

W naszej grze występują trzy postacie (aktorzy):
* lewa paletka,
* prawa paletka,
* piłka.

Dodamy je po kolei do naszej gry i wyświetlimy na ekranie.

## Lewa paletka

Naszych aktorów dodamy zaraz pod kolorem tła, czyli na górze programu.

### Tworzymy aktora

Najpierw musimy utworzyć aktora i zapisać go w nowej zmiennej, którą nazwiemy _lewa_.
Naszego aktora tworzymy na podstawie grafiki *lewa.png*.

```python
lewa = Actor("lewa.png")
```

### Ustalamy pozycję lewej paletki

Nasza lewa paletka będzie znajdować się z lewej strony ekranu.
Nie chcemy jednak, by dotykała krawędzi, damy jej więc pewien niewielki margines, np. $$20$$ pikseli.
Dzięki temu nasza gra będzie wyglądała estetyczniej.
Ustalamy więc współrzędną $$x$$ lewej paletki.

```python
lewa.x = 20
```

Trzeba jeszcze pomyśleć o drugiej współrzędnej: $$y$$.
Początkowo umieśćmy paletkę na środku, czyli w połowie wysokości ekranu gry.

```python
lewa.y = HEIGHT / 2
```

### Rysujemy paletkę

Skoro już umieściliśmy naszą lewą paletkę w jej początkowej pozycji, możemy ją narysować na ekranie.
Do części rysującej, zaraz pod poleceniem rysującym żółtą linię, dopisujemy polecenie rysujące lewą paletkę: _lewa.draw()_.

```python
def draw():
    screen.fill(kolor_tla)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
    lewa.draw()
```

### Pełny kod

Dotychczasowy pełny kod naszej gry przedstawiony jest poniżej.

```python
import pgzrun


WIDTH = 800
HEIGHT = 600

TITLE = "PONG"

kolor_tla = (64, 64, 64)

lewa = Actor("lewa.png")
lewa.x = 20
lewa.y = HEIGHT / 2


def draw():
    screen.fill(kolor_tla)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
    lewa.draw()

    
def update():
    pass
    
    
pgzrun.go()
```

## Prawa paletka

Prawą paletkę tworzymy bardzo podobnie do lewej.
Najważniejszą różnicą będzie oczywiście jej grafika i początkowe położenie.

### Tworzymy aktora

Najpierw musimy utworzyć aktora i zapisać go w nowej zmiennej, którą nazwiemy _prawa_.
Naszego aktora tworzymy na podstawie grafiki *prawa.png*.

```python
prawa = Actor("prawa.png")
```

### Ustalamy pozycję prawej paletki

Nasza prawa paletka będzie znajdować się z prawej strony ekranu.
Nie chcemy jednak, by dotykała krawędzi, damy jej więc pewien niewielki margines, taki jak dla lewej paletyki, czyli $$20$$ pikseli.
Dzięki temu nasza gra będzie wyglądała estetyczniej.
Ustalamy więc współrzędną $$x$$ prawej paletki.
Ponieważ umieszczamy ją z prawej strony ekranu, to aby obliczyć jej pozycję, od szerokości ekranu (**WIDTH**) odejmujemy ustalony wcześniej margines.

```python
prawa.x = WIDTH - 20
```

Trzeba jeszcze pomyśleć o drugiej współrzędnej: $$y$$.
Początkowo umieśćmy paletkę na środku, czyli w połowie wysokości ekranu gry, tak samo jak lewą paletkę.

```python
prawa.y = HEIGHT / 2
```

### Rysujemy paletkę

Skoro już umieściliśmy naszą prawą paletkę w jej początkowej pozycji, możemy ją narysować na ekranie.
Do części rysującej, zaraz pod poleceniem rysującym lewą paletkę, dopisujemy polecenie rysujące prawą paletkę: _prawa.draw()_.

```python
def draw():
    screen.fill(kolor_tla)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
    lewa.draw()
    prawa.draw()
```

### Pełny kod

Dotychczasowy pełny kod naszej gry przedstawiony jest poniżej.

```python
import pgzrun


WIDTH = 800
HEIGHT = 600

TITLE = "PONG"

kolor_tla = (64, 64, 64)

lewa = Actor("lewa.png")
lewa.x = 20
lewa.y = HEIGHT / 2

prawa = Actor("prawa.png")
prawa.x = WIDTH - 20
prawa.y = HEIGHT / 2


def draw():
    screen.fill(kolor_tla)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
    lewa.draw()
    prawa.draw()
    
    
def update():
    pass
    
    
pgzrun.go()
```

## Piłka

Piłkę dodamy podobnie jak paletki, ale umieścimy ją na środku ekranu.

### Tworzymy aktora

Najpierw musimy utworzyć aktora i zapisać go w nowej zmiennej, którą nazwiemy _pilka_.
Naszego aktora tworzymy na podstawie grafiki *pilka.png*.

```python
pilka = Actor("pilka.png")
```

### Ustalamy pozycję piłki

Nasza piłka będzie początkow znajdować się na środku ekranu.
Dlatego do współrzędnej $$x$$ przypisujemy połowę szerokości (**WIDTH**) ekranu, a do współrzędnej $$y$$ przypisujemy połowę wysokości (**HEIGHT**) ekranu.

```python
pilka.x = WIDTH / 2
pilka.y = HEIGHT / 2
```

### Rysujemy piłkę

Skoro już umieściliśmy naszą piłkę w jej początkowej pozycji, możemy ją narysować na ekranie.
Do części rysującej, zaraz pod poleceniem rysującym prawą paletkę, dopisujemy polecenie rysujące piłkę: _pilka.draw()_.

```python
def draw():
    screen.fill(kolor_tla)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
    lewa.draw()
    prawa.draw()
    pilka.draw()
```

### Pełny kod

Dotychczasowy pełny kod naszej gry przedstawiony jest poniżej.

```python
import pgzrun


WIDTH = 800
HEIGHT = 600

TITLE = "PONG"

kolor_tla = (64, 64, 64)

lewa = Actor("lewa.png")
lewa.x = 20
lewa.y = HEIGHT / 2

prawa = Actor("prawa.png")
prawa.x = WIDTH - 20
prawa.y = HEIGHT / 2

pilka = Actor("pilka.png")
pilka.x = WIDTH / 2
pilka.y = HEIGHT / 2


def draw():
    screen.fill(kolor_tla)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
    lewa.draw()
    prawa.draw()
    pilka.draw()
    
    
def update():
    pass
    
    
pgzrun.go()
```

## Ruch graczy

Paletki chcemy poruszać jedynie w dwóch kierunkach: w górę i w dół.
Obie paletki będziemy sterować za pomocą klawiatury.
Lewą paletkę obsłużymy klawiszami **W** i **S**, a prawą paletkę obsłużymy **strzałkami w górę i w dół**.

### Funkcja odczytująca ruchy

W celu zachowania czytelności naszego kodu, napiszemy sobie nową **funkcję**, tzn. wydzielony fragment kodu, który będzie realizował konkretne zadanie.
To zadanie będzie polegało na odczytaniu wciśniętych klawiszy z klawiatury i wykonaniu odpowiedniego ruchu paletek.
Nazwiemy naszą funkcję *ruch_graczy*.
Wewnątrz funkcji będziemy sprawdzać, czy dany klawisz na klawiaturze jest wciśnięty, a jeżeli tak, to wykonamy stosowny ruch paletki, tzn. zmienimy jej współrzędne.

```python
def ruch_graczy():
    if keyboard.w:
        lewa.y -= lewa.py

    if keybaord.s:
        lewa.y += lewa.py

    if keyboard.up:
        prawa.y -= prawa.py

    if keyboard.down:
        prawa.y += prawa.py
```

### Wywołujemy funkcję w części aktualizującej

Aby zobaczyć rezultaty naszego działania, potrzebujemy jeszcze **użyć** naszej funkcji.
Ruch graczy to **aktualizacja** pozycji graczy na ekranie, dlatego naszą nową funkcję *ruch_graczy* **wywołujemy** w części aktualizującej (**update**), zastępując jej dotychczasową zawartość (*pass*).

```python
def update():
    ruch_graczy()
```

### Ograniczenie ruchu graczy

Nie chcemy, by paletki mogły wychodzić poza ekran, dlatego dodajemy dodatkowe warunki do naszych instrukcji.
Przed wykonaniem danego ruchu sprawdzimy, czy paletka znajduje się wystarczająco daleko od brzegu ekranu, aby ten ruch móc wykonać.

```python
def ruch_graczy():
    if keyboard.w and lewa.top > 40:
        lewa.y -= lewa.py

    if keybaord.s and lewa.bottom < HEIGHT - 40:
        lewa.y += lewa.py

    if keyboard.up and prawa.top > 40:
        prawa.y -= prawa.py

    if keyboard.down and prawa.bottom < HEIGHT - 40:
        prawa.y += prawa.py
```

### Pełny kod

Dotychczasowy pełny kod naszej gry przedstawiony jest poniżej.

```python
import pgzrun


WIDTH = 800
HEIGHT = 600

TITLE = "PONG"

kolor_tla = (64, 64, 64)

lewa = Actor("lewa.png")
lewa.x = 20
lewa.y = HEIGHT / 2
lewa.py = 5

prawa = Actor("prawa.png")
prawa.x = WIDTH - 20
prawa.y = HEIGHT / 2
prawa.py = 5

pilka = Actor("pilka.png")
pilka.x = WIDTH / 2
pilka.y = HEIGHT / 2


def draw():
    screen.fill(kolor_tla)
    screen.draw.line((WIDTH / 2, 40), (WIDTH / 2, HEIGHT - 40), color = "yellow")
    lewa.draw()
    prawa.draw()
    pilka.draw()
    
    
def update():
    ruch_graczy()


def ruch_graczy():
    if keyboard.w and lewa.top > 40:
        lewa.y -= lewa.py

    if keybaord.s and lewa.bottom < HEIGHT - 40:
        lewa.y += lewa.py

    if keyboard.up and prawa.top > 40:
        prawa.y -= prawa.py

    if keyboard.down and prawa.bottom < HEIGHT - 40:
        prawa.y += prawa.py
    
    
pgzrun.go()
```

## Pełna gra - wersja podstawowa

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

        # Rysujemy linię dzielącą pole gry
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

## Wersja z bonusami

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

## Przeciwko komputerowi

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