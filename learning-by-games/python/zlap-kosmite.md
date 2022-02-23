# Złap kosmitę

## Wstęp

Celem gry jest złapanie kosmity. Nie jest to jednak takie proste, jakby się mogło wydawać! Kosmita porusza się w losowych kierunkach. Za każde celne kliknięcie w kosmitę dostajemy punkt, a za każde pudło tracimy punkt! Co więcej, kosmita z każdym trafieniem przyspiesza! Ile punktów uda Ci się zdobyć?

### Czego się nauczysz

TODO

## Przygotowujemy projekt gry

TODO

### Grafiki do pobrania

TODO

### Struktura plików

TODO

### Importujemy biblioteki

Zastanówmy się, jakich "narzędzi" będziemy potrzebować. Podstawowym elementem będzie oczywiście nasza biblioteka do tworzenia gier. Docelowo nasz kosmita będzie się poruszał w **losowych** kierunkach, przyda nam się także biblioteka do liczb losowych. 

Dodajemy więc odpowiednie polecenia na samym początku pliku w edytorze:

```python
import pgzrun
import random
```

### Określamy wymiary okna gry

TODO

```python
WIDTH = 800
HEIGHT = 600
```

### Wybieramy kolor tła

TODO

{% hint style="info" %}
**RGB **

TODO
{% endhint %}

```python
kolor_tla = (0, 120, 0)
```

### **Wypełniamy ekran wybranym kolorem**

TODO

```python
    screen.fill(kolor_tla)
```

Pełna implementacja funkcji rysującej wygląda więc następująco:

```python
def draw():
    screen.fill(kolor_tla)
```

### Pozostałe elementy szablonu

Na koniec pozostało nam uzupełnić nasz program o pozostałe wymagane elementy szablonu, czyli funkcję aktualizującą i polecenie uruchamiające grę.

```python
def update():
    pass


pgzrun.go()
```

### Pełny program

```python
# Importujemy bibliotekę Pygame Zero do tworzenia gier
import pgzrun
# Imporujemy bibliotekę do liczb losowych
import random

# Określamy szerokość i wysokość okna gry
WIDTH = 800
HEIGHT = 600

# Podajemy kolor tła za pomocą trzech wartości, liczb od 0 do 255
# Liczby określają ile każdego z trzech podstawowych kolorów używamy
# Pierwsza liczba to ilość koloru czerwonego (Red)
# Druga liczba to ilość koloru zielonego (Green)
# Trzecia liczba to ilość koloru niebieskiego (Blue)
kolor_tla = (0, 120, 0)


def draw():
    # Wypełniamy ekran wybranym kolorem
    screen.fill(kolor_tla)


def update():
    pass


# Uruchamiamy grę
pgzrun.go()
```

### Testujemy działanie

TODO - filmik

## Rysowanie kosmity

TODO

### Tworzymy nowego aktora gry

TODO

```python
kosmita = Actor("kosmita.png")
```

### Ustalamy początkową pozycję kosmity

TODO

```python
kosmita.pos = (200, 200)
```

### Rysujemy kosmitę na ekranie

TODO

```python
    kosmita.draw()
```

Pełna implementacja funkcji rysującej wygląda więc następująco:

```python
def draw():
    screen.fill(kolor_tla)
    kosmita.draw()
```

### Pełny program

```python
import pgzrun
import random


WIDTH = 800
HEIGHT = 600

kolor_tla = (0, 120, 0)

# Tworzymy nową postać, nowego aktora naszej gry, na podstawie grafiki kosmita.png
kosmita = Actor("kosmita.png")

# Ustalamy początkową pozycję naszej postaci na ekranie
# Podajemy dwie współrzędne: x, y
# x oznacza odległość od lewej strony
# y oznacza odległość od góry ekranu
kosmita.pos = (200, 200)


def draw():
    screen.fill(kolor_tla)

    # Rysujemy kosmitę
    kosmita.draw()


def update():
    pass


pgzrun.go()
```

### Testujemy działanie

TODO - filmik

## Poruszanie kosmitą

TODO

### Ustalamy prędkość kosmity

TODO

```python
kosmita.px = 1
kosmita.py = 0
```

### Aktualizujemy pozycję kosmity

TODO

```python
    kosmita.left += kosmita.px
    kosmita.top += kosmita.py
```

Pełna implementacja funkcji aktualizującej wygląda więc następująco:

```python
def update():
    kosmita.left += kosmita.px
    kosmita.top += kosmita.py
```

### Pełny program

```python
import pgzrun
import random


WIDTH = 800
HEIGHT = 600

kolor_tla = (0, 120, 0)

kosmita = Actor("kosmita.png")

kosmita.pos = (200, 200)

# Zapamiętujemy prędkość kosmity: poziomą (x) i pionową (y)
kosmita.px = 1
kosmita.py = 0


def draw():
    screen.fill(kolor_tla)
    kosmita.draw()


def update():
    # Przesuwamy kosmitę, zmieniając jego pozycje zgodnie z prędkością
    kosmita.left += kosmita.px
    kosmita.top += kosmita.py


pgzrun.go()
```

### Testujemy działanie

TODO - filmik

## Przechodzenie przez krawędzie ekranu

TODO

### Wyjście z prawej strony

TODO

```python
    if kosmita.left > WIDTH:
```

TODO

```python
    if kosmita.left > WIDTH:
        kosmita.left = 0
```

Pełna implementacja funkcji aktualizującej wygląda więc następująco:

```python
def update():
    kosmita.left += kosmita.px
    kosmita.top += kosmita.py

    if kosmita.left > WIDTH:
        kosmita.left = 0
```

### Wyjście z lewej strony

TODO

```python
    if kosmita.left < 0:
        kosmita.left = WIDTH
```

Pełna implementacja funkcji aktualizującej wygląda więc następująco:

```python
def update():
    kosmita.left += kosmita.px
    kosmita.top += kosmita.py

    if kosmita.left > WIDTH:
        kosmita.left = 0
        
    if kosmita.left < 0:
        kosmita.left = WIDTH
```

### Wyjście z dołu

TODO

```python
    if kosmita.top > HEIGHT:
        kosmita.top = 0
```

Pełna implementacja funkcji aktualizującej wygląda więc następująco:

```python
def update():
    kosmita.left += kosmita.px
    kosmita.top += kosmita.py

    if kosmita.left > WIDTH:
        kosmita.left = 0
        
    if kosmita.left < 0:
        kosmita.left = WIDTH
        
    if kosmita.top > HEIGHT:
        kosmita.top = 0
```

### Wyjście z góry

TODO

```python
    if kosmita.top < 0:
        kosmita.top = HEIGHT
```

Pełna implementacja funkcji aktualizującej wygląda więc następująco:

```python
def update():
    kosmita.left += kosmita.px
    kosmita.top += kosmita.py

    if kosmita.left > WIDTH:
        kosmita.left = 0
        
    if kosmita.left < 0:
        kosmita.left = WIDTH
        
    if kosmita.top > HEIGHT:
        kosmita.top = 0

    if kosmita.top < 0:
        kosmita.top = HEIGHT
```

### Pełny program

```python
import pgzrun
import random


WIDTH = 800
HEIGHT = 600

kolor_tla = (0, 120, 0)

kosmita = Actor("kosmita.png")

kosmita.pos = (200, 200)

kosmita.px = 1
kosmita.py = 0


def draw():
    screen.fill(kolor_tla)
    kosmita.draw()


def update():
    kosmita.left += kosmita.px
    kosmita.top += kosmita.py

    # Jeżeli odległość kosmity od lewego brzegu jest większa od szerokości ekranu
    # Czyli, jeżeli kosmita wyszedł poza ekran
    if kosmita.left > WIDTH:
        # Przesuwamy kosmitę na początek
        kosmita.left = 0

    # Jeżeli kosmita wyszedł z lewej strony ekranu, przesuwamy go w prawo
    if kosmita.left < 0:
        kosmita.left = WIDTH

    # Jeżeli kosmita wyszedł z dołu ekranu, przesuwamy go na górę
    if kosmita.top > HEIGHT:
        kosmita.top = 0

    # Jeżeli kosmita wyszedł z góry ekranu, przesuwamy go na dół
    if kosmita.top < 0:
        kosmita.top = HEIGHT


pgzrun.go()
```

### Testujemy działanie

TODO - filmik

## Klikanie na kosmitę

TODO

### Odczytujemy pozycję kliknięcia

TODO

```python
def on_mouse_down(pos):
```

### Sprawdzamy, czy trafiliśmy w kosmitę

TODO

```python
    if kosmita.collidepoint(pos):
```

Pełna implementacja funkcji przechwytującej kliknięcia wygląda więc następująco:

```python
def on_mouse_down(pos):
    if kosmita.collidepoint(pos):
```

### Ustawiamy kosmitę w losowym miejscu

TODO

```python
        kosmita.left = random.randint(0, WIDTH)
        kosmita.top = random.randint(0, HEIGHT - 90)
```

Pełna implementacja funkcji przechwytującej kliknięcia wygląda więc następująco:

```python
def on_mouse_down(pos):
    if kosmita.collidepoint(pos):
        kosmita.left = random.randint(0, WIDTH)
        kosmita.top = random.randint(0, HEIGHT-90)
```

### Nadajemy kosmicie losową prędkość

TODO

```python
        kosmita.px = random.randint(-2, 2)
        kosmita.py = random.randint(-2, 2)
```

Pełna implementacja funkcji przechwytującej kliknięcia wygląda więc następująco:

```python
def on_mouse_down(pos):
    if kosmita.collidepoint(pos):
        kosmita.left = random.randint(0, WIDTH)
        kosmita.top = random.randint(0, HEIGHT-90)

        kosmita.px = random.randint(-2, 2)
        kosmita.py = random.randint(-2, 2)
```

### Pełny program

```python
import pgzrun
import random


WIDTH = 800
HEIGHT = 600

kolor_tla = (0, 120, 0)

kosmita = Actor("kosmita.png")

kosmita.pos = (200, 200)

kosmita.px = 1
kosmita.py = 0


def draw():
    screen.fill(kolor_tla)
    kosmita.draw()


def update():
    kosmita.left += kosmita.px
    kosmita.top += kosmita.py

    if kosmita.left > WIDTH:
        kosmita.left = 0

    if kosmita.left < 0:
        kosmita.left = WIDTH

    if kosmita.top > HEIGHT:
        kosmita.top = 0

    if kosmita.top < 0:
        kosmita.top = HEIGHT


# Tutaj piszemy, co ma się wydarzyć, gdy gracz kliknie myszką
# Zmienna pos zawiera pozycję myszki na ekranie
def on_mouse_down(pos):
    # Jeżeli kliknęliśmy w kosmitę, to
    if kosmita.collidepoint(pos):
        # Ustawiamy kosmitę w losowym miejscu
        kosmita.left = random.randint(0, WIDTH)
        kosmita.top = random.randint(0, HEIGHT-90)

        # Ustawiamy losową prędkość kosmity
        kosmita.px = random.randint(-2, 2)
        kosmita.py = random.randint(-2, 2)


pgzrun.go()
```

### Testujemy działanie

TODO - filmik

## Wyświetlanie punktów

TODO

### Pełny program

```python
import pgzrun
import random


WIDTH = 800
HEIGHT = 600

kolor_tla = (0, 120, 0)

kosmita = Actor("kosmita.png")

kosmita.pos = (200, 200)

kosmita.px = 1
kosmita.py = 0

# W zmiennej punkty będziemy zliczać punkty zdobyte przez gracza
kosmita.punkty = 0

def draw():
    screen.fill(kolor_tla)
    kosmita.draw()
    
    # Wypisujemy liczbę punktów
    screen.draw.text("Punkty: " + str(kosmita.punkty), (50, 30), color="orange")


def update():
    kosmita.left += kosmita.px
    kosmita.top += kosmita.py

    if kosmita.left > WIDTH:
        kosmita.left = 0

    if kosmita.left < 0:
        kosmita.left = WIDTH

    if kosmita.top > HEIGHT:
        kosmita.top = 0

    if kosmita.top < 0:
        kosmita.top = HEIGHT


def on_mouse_down(pos):
    if kosmita.collidepoint(pos):
        kosmita.left = random.randint(0, WIDTH)
        kosmita.top = random.randint(0, HEIGHT-90)

        kosmita.px = random.randint(-2, 2)
        kosmita.py = random.randint(-2, 2)


pgzrun.go()
```

### Testujemy działanie

TODO - filmik

## Zliczanie punktów

TODO

### Zdobywamy punkty

TODO

### Tracimy punkty

TODO

### Pełny program

```python
import pgzrun
import random


WIDTH = 800
HEIGHT = 600

kolor_tla = (0, 120, 0)

kosmita = Actor("kosmita.png")

kosmita.pos = (200, 200)

kosmita.px = 1
kosmita.py = 0

kosmita.punkty = 0

def draw():
    screen.fill(kolor_tla)
    kosmita.draw()
    screen.draw.text("Punkty: " + str(kosmita.punkty), (50, 30), color="orange")


def update():
    kosmita.left += kosmita.px
    kosmita.top += kosmita.py

    if kosmita.left > WIDTH:
        kosmita.left = 0

    if kosmita.left < 0:
        kosmita.left = WIDTH

    if kosmita.top > HEIGHT:
        kosmita.top = 0

    if kosmita.top < 0:
        kosmita.top = HEIGHT


def on_mouse_down(pos):
    if kosmita.collidepoint(pos):
        kosmita.left = random.randint(0, WIDTH)
        kosmita.top = random.randint(0, HEIGHT-90)

        kosmita.px = random.randint(-2, 2)
        kosmita.py = random.randint(-2, 2)

        # Zwiększamy liczbę punktów
        kosmita.punkty += 1
    else:
        # Jeżeli nie trafiliśmy w kosmitę, odejmujemy punkty
        kosmita.punkty -= 1

pgzrun.go()
```

### Testujemy działanie

TODO - filmik

## Poziom trudności

TODO

### Pełny program

```python
import pgzrun
import random


WIDTH = 800
HEIGHT = 600

kolor_tla = (0, 120, 0)

kosmita = Actor("kosmita.png")

kosmita.pos = (200, 200)

kosmita.px = 1
kosmita.py = 0

kosmita.punkty = 0

# Tutaj zapamiętujemy, jak szybko porusza się kosmita
kosmita.poziom = 1

def draw():
    screen.fill(kolor_tla)
    kosmita.draw()
    screen.draw.text("Punkty: " + str(kosmita.punkty), (50, 30), color="orange")


def update():
    # Przesuwamy kosmitę, zmieniając jego pozycje zgodnie z prędkością i trudnością gry
    kosmita.left += kosmita.px * kosmita.poziom
    kosmita.top += kosmita.py * kosmita.poziom

    if kosmita.left > WIDTH:
        kosmita.left = 0

    if kosmita.left < 0:
        kosmita.left = WIDTH

    if kosmita.top > HEIGHT:
        kosmita.top = 0

    if kosmita.top < 0:
        kosmita.top = HEIGHT


def on_mouse_down(pos):
    if kosmita.collidepoint(pos):
        kosmita.left = random.randint(0, WIDTH)
        kosmita.top = random.randint(0, HEIGHT-90)

        kosmita.px = random.randint(-2, 2)
        kosmita.py = random.randint(-2, 2)

        kosmita.punkty += 1
        
        # Zwiększamy szybkość kosmity, jeżeli nie jest już zbyt szybki
        if kosmita.poziom < 10:
            kosmita.poziom += 1
    else:
        kosmita.punkty -= 1
        
        # Zmniejszamy szybkość kosmity, jeżeli nie jest już zbyt wolny
        if kosmita.poziom >= 1:
            kosmita.poziom -= 1

pgzrun.go()
```

### Testujemy działanie

TODO - filmik

## Pełna gra z komentarzami

```python
# Importujemy bibliotekę Pygame Zero do tworzenia gier
import pgzrun
# Imporujemy bibliotekę do liczb losowych
import random

# Określamy szerokość i wysokość okna gry
WIDTH = 800
HEIGHT = 600

# Podajemy kolor tła za pomocą trzech wartości, liczb od 0 do 255
# Liczby określają ile każdego z trzech podstawowych kolorów używamy
# Pierwsza liczba to ilość koloru czerwonego (Red)
# Druga liczba to ilość koloru zielonego (Green)
# Trzecia liczba to ilość koloru niebieskiego (Blue)
kolor_tla = (0, 120, 0)

# Tworzymy nową postać, nowego aktora naszej gry, na podstawie grafiki kosmita.png
kosmita = Actor("kosmita.png")

# Ustalamy początkową pozycję naszej postaci na ekranie
# Podajemy dwie współrzędne: x, y
# x oznacza odległość od lewej strony
# y oznacza odległość od góry ekranu
kosmita.pos = (200, 200)

# Zapamiętujemy prędkość kosmity: poziomą (x) i pionową (y)
kosmita.px = 1
kosmita.py = 0

# W zmiennej punkty będziemy zliczać punkty zdobyte przez gracza
kosmita.punkty = 0

# Tutaj zapamiętujemy, jak szybko porusza się kosmita
kosmita.poziom = 1


def draw():
    # Wypełniamy ekran wybranym kolorem
    screen.fill(kolor_tla)

    # Rysujemy kosmitę
    kosmita.draw()

    # Wypisujemy liczbę punktów
    screen.draw.text("Punkty: " + str(kosmita.punkty), (50, 30), color="orange")


def update():
    # Przesuwamy kosmitę, zmieniając jego pozycje zgodnie z prędkością i trudnością gry
    kosmita.left += kosmita.px * kosmita.poziom
    kosmita.top += kosmita.py * kosmita.poziom

    # Jeżeli odległość kosmity od lewego brzegu jest większa od szerokości ekranu
    # Czyli, jeżeli kosmita wyszedł poza ekran
    if kosmita.left > WIDTH:
        # Przesuwamy kosmitę na początek
        kosmita.left = 0

    # Jeżeli kosmita wyszedł z lewej strony ekranu, przesuwamy go w prawo
    if kosmita.left < 0:
        kosmita.left = WIDTH

    # Jeżeli kosmita wyszedł z dołu ekranu, przesuwamy go na górę
    if kosmita.top > HEIGHT:
        kosmita.top = 0

    # Jeżeli kosmita wyszedł z góry ekranu, przesuwamy go na dół
    if kosmita.top < 0:
        kosmita.top = HEIGHT


# Tutaj piszemy, co ma się wydarzyć, gdy gracz kliknie myszką
# Zmienna pos zawiera pozycję myszki na ekranie
def on_mouse_down(pos):
    # Jeżeli kliknęliśmy w kosmitę, to
    if kosmita.collidepoint(pos):
        # Ustawiamy kosmitę w losowym miejscu
        kosmita.left = random.randint(0, WIDTH)
        kosmita.top = random.randint(0, HEIGHT-90)

        # Ustawiamy losową prędkość kosmity
        kosmita.px = random.randint(-2, 2)
        kosmita.py = random.randint(-2, 2)
        
        # Zwiększamy liczbę punktów
        kosmita.punkty += 1

        # Zwiększamy szybkość kosmity, jeżeli nie jest już zbyt szybki
        if kosmita.poziom < 10:
            kosmita.poziom += 1
    else:
        # Jeżeli nie trafiliśmy w kosmitę, odejmujemy punkty
        kosmita.punkty -= 1
        
        # Zmniejszamy szybkość kosmity, jeżeli nie jest już zbyt wolny
        if kosmita.poziom >= 1:
            kosmita.poziom -= 1

# Uruchamiamy grę
pgzrun.go()
```

## Zadania dodatkowe

TODO
