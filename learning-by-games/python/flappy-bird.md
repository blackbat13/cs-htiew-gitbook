# Flappy Bird

## Wstęp

Dzisiaj odtworzymy jedną z kultowych gier mobilnych: Flappy Bird.

### Czego się nauczysz

* Jak dodać grawitację i skok do gry.
* Jak stworzyć i obsłużyć proste menu.
* Jak stworzyć "nieskończoną" grę bazującą na prostych założeniach.

### Grafiki do pobrania

Umieszczamy w katalogu **images**.

{% file src="../../.gitbook/assets/flappy_images.zip" %}
Grafiki do gry Flappy Bird
{% endfile %}

### Efekty dźwiękowe do pobrania

Umieszczamy w katalogu **sounds**.

{% file src="../../.gitbook/assets/flappy_sounds.zip" %}
Efekty dźwiękowe do gry Flappy Bird
{% endfile %}

### Źródła

- Grafiki przycisków pochodzą ze strony: [https://kenney.nl/](https://kenney.nl).
- Pozostałe grafiki pochodzą ze strony projektu pgzero: [https://github.com/lordmauve/pgzero/tree/master/examples/flappybird/images](https://github.com/lordmauve/pgzero/tree/master/examples/flappybird/images).
- Efekty dźwiękowe pochodzą ze strony: [https://www.sounds-resource.com/mobile/flappybird/sound/5309/](https://www.sounds-resource.com/mobile/flappybird/sound/5309/).

## Nasz cel

![Flappy Bird - animacja](../../.gitbook/assets/flappyGame.gif)

## Wstępna konfiguracja

Zaczynamy standardowo: tworzymy nowy projekt, instalujemy bibliotekę, pobieramy materiały i umieszczamy je w odpowiednich miejscach.
Nasz projekt możemy nazwać np. "FlappyBird". Gdy już utworzymy projekt, tworzymy w nim dwa nowe katalogi: *images* oraz *sounds*. Następnie pobieramy wyżej wymienione materiały, rozpakowujemy je, a zawartość przerzucamy do odpowiednich katalogów. Pozostało nam jeszcze zainstalować bibliotekę: w okienku terminala wypisujemy standardowo polecenie `pip install pgzero`.

## Tworzymy okno gry

Jak zwykle zaczynamy od podstaw. Wymiary naszego okna są zależne od wymiarów grafiki tła i wynoszą $$400\times700$$. Ustawiamy więc odpowiednie wymiary i wypełniamy tło grafiką *bg.png* za pomocą polecenia `screen.blit()`. Możemy także skonfigurować tytuł naszej gry.

```python
import pgzrun
import random


WIDTH = 400
HEIGHT = 700

TITLE = "PyGameZero Flappy Bird"


def draw():
    screen.blit("bg.png", (0, 0))


def update():
    pass


pgzrun.go()
```

## Ptak

Zacznijmy od naszej głównej postaci: ptaka.

### Dodajemy aktora

Na samym początku dodajemy nowego aktora z grafiki *bird1.png*. Umieścimy go z lewej strony ekranu, na środku, pod współrzędnymi $$(75, 200)$$.

```python
bird = Actor("bird1.png")
bird.x = 75
bird.y = 200
```

### Rysujemy

Wyświetlmy naszą nową postać na ekranie. W części rysującej dopisujemy odpowiednie polecenie.

```python
def draw():
    screen.blit("bg.png", (0, 0))
    bird.draw()
```

### Grawitacja

Jak na razie nasza postać jest bardzo statyczna i tkwi w jednym miejscu. Urozmaićmy więc trochę jej życie i dodajmy siłę grawitacji. Grawitacja w naszej grze będzie działać podobnie do tej, którą znamy z codziennego życia: będzie ściągać postać w dół. Zanim jednak będziemy mogli dodać oddziaływanie grawitacji na postać, musimy ustalić siłę grawitacji. Dodajmy więc zmienną `gravity` na początku naszego kodu, zaraz pod wymiarami okna, i przypiszmy jej wartość $$0.3$$.

```python
gravity = 0.3
```

Teraz czas zaaplikować grawitację do postaci ptaka. Grawitacja powinna wpływać na prędkość pionową postaci, musimy więc tę prędkość dopisać do naszego aktora.

```python
bird.vy = 0
```

Teraz, w każdej klatce animacji, prędkość postaci będzie zwiększana o siłę grawitacji. Z kolei pozycja aktora będzie się zmieniać zgodnie z jego prędkością. Dopisujemy więc obliczenia w części aktualizującej.

```python
def update():
    bird.vy += gravity
    bird.y += bird.vy
```

### Latanie

Mamy już grawitację, czas więc dodać możliwość próby przezwyciężenia tej wielkiej siły: zdolność latania. Nasza postać będzie podnosić się lekko do góry za każdym razem, gdy wciśniemy jakiś (dowolny) przycisk na klawiaturze. Potrzebna nam więc funkcja `on_key_down`. W celu zasymulowania unoszenia się postaci do góry wystarczy, że nadamy jej odpowiednią prędkość wzlotową.

```python
def on_key_down():
    bird.vy = -7
```

### Pełny kod

Dotychczasowy pełny kod naszej gry przedstawiony jest poniżej.

```python
import pgzrun
import random


WIDTH = 400
HEIGHT = 700

TITLE = "PyGameZero Flappy Bird"

gravity = 0.3

bird = Actor("bird1.png")
bird.x = 75
bird.y = 200
bird.vy = 0


def draw():
    screen.blit("bg.png", (0, 0))
    bird.draw()


def update():
    bird.vy += gravity
    bird.y += bird.vy


def on_key_down():
    bird.vy = -7


pgzrun.go()
```

## Rury

Czas dodać naszego przeciwnika w grze: rury. Jak zwykle zaczynamy od dodania nowych aktorów. Tym razem będzie ich dwóch: górna rura (`pipe_top`) i dolna rura (`pipe_bottom`). Utworzymy ich tak jak zazwyczaj z niewielką różnicą: ustalimy im odpowiednie _**kotwice**_. Kotwica pozwala nam wybrać punkt grafiki, według którego będziemy ją umieszczać na ekranie. Można to sobie wyobrazić jako miejsce, w którym "trzymamy" grafikę, gdy ją przemieszczamy. Domyślnie grafikę poruszamy względem jej środka, ale możemy też wybrać inne miejsce zaczepienia. Ze względu na charakter rur w naszej grze jest to duże ułatwienie.

Dla górnej rury ustawimy kotwicę w jej lewym **dolnym** rogu. Dla dolnej rury natomiast ustawimy kotwicę w jej lewym **górnym** rogu.

```python
pipe_top = Actor("top", anchor=("left", "bottom"))
pipe_bottom = Actor("bottom", anchor=("left", "top"))
```

### Rysujemy rury

Gdy już mamy aktorów, czas ich wyświetlić na ekranie. Dodajemy dwie instrukcje w części rysującej naszej gry. Narysujemy je przed narysowaniem postaci ptaka, żeby go nie zasłaniały.

```python
def draw():
    screen.blit("bg.png", (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    ptak.draw()
```

### Ustawiamy pozycję rur

Główną trudnością w naszej grze będzie niewielka przestrzeń pomiędzy rurami, przez którą musimy przelecieć. 
Żeby gra nie była zbyt przewidywalna, ta przestrzeń powinna pojawiać się na losowej wysokości. 
Stworzymy więc funkcję `set_pipes` za pomocą której będziemy losować nową pozycję rur.

```python
def set_pipes():
    gap = random.randint(200, 500)
    pipe_top.pos = (WIDTH, gap - 70)
    pipe_bottom.pos = (WIDTH, gap + 70)
```

Teraz czas wywołać naszą funkcję. Zrobimy to zaraz przed uruchomieniem gry, czyli tuż przed instrukcją `pgzrun.go()`.

```python
set_pipes()
pgzrun.go()
```

### Przemieszczamy rury

W każdej klatce animacji nasze rury powinny przemieszczać się w lewą stronę. 
W tym celu w części aktualizującej będziemy je przesuwać o $$3$$ piksele w lewo.

```python
def update():
    ...

    pipe_top.left -= 3
    pipe_bottom.left -= 3
```

Gdy rury znikną z lewej strony ekranu, należy ustawić je ponownie.

```python
    if pipe_top.x < -100:
        set_pipes()
```

### Pełny kod

Dotychczasowy pełny kod naszej gry przedstawiony jest poniżej.

```python
import pgzrun
import random


WIDTH = 400
HEIGHT = 700

TITLE = "PyGameZero Flappy Bird"

gravity = 0.3

bird = Actor("bird1.png")
bird.x = 75
bird.y = 200
bird.vy = 0

pipe_top = Actor("top", anchor=("left", "bottom"))
pipe_bottom = Actor("bottom", anchor=("left", "top"))

def draw():
    screen.blit("bg.png", (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()


def update():
    bird.vy += gravity
    bird.y += bird.vy

    pipe_top.left -= 3
    pipe_bottom.left -= 3

    if pipe_top.x < -100:
        set_pipes()


def on_key_down():
    bird.vy = -7


def set_pipes():
    gap = random.randint(200, 500)
    pipe_top.pos = (WIDTH, gap - 70)
    pipe_bottom.pos = (WIDTH, gap + 70)


set_pipes()
pgzrun.go()
```

## Koniec gry

Kiedy nasza gra się kończy? Gdy trafimy w rurę, lub wylecimy poza ekran.

### Reset gry

Zacznijmy od zastanowienia się, co chcemy zrobić, gdy gra się skończy, tzn. gdy gracz przegra.
Możemy oczywiście wyświetlić komunikat o przegranej i wyłączyć grę.
Nasza gra ma jednak z założenia wysoki poziom trudności, więc uruchamianie jej raz za razem po każdej przegranej bardzo szybko stałoby się uciążliwe.
Zamiast tego po przegranej **zresetujemy grę**, tzn. zaczniemy ją od nowa.
W tym celu stworzymy nową funkcję *reset*.

Co powinniśmy zrobić, aby zresetować grę?
Jakie jej ustawienia musimy przywrócić do początkowych wartości?
Potrzebujemy przywrócić naszego gracza, ptaka, na początkową pozycję i nadać mu właściwą prędkość.
Przytałoby się także ponownie ustawić rury, abyśmy przypadkiem nie wylądowali w środku jeden z nich.

```python
def reset():
    bird.x = 75
    bird.y = 200
    bird.vy = 0
    set_pipes()
```

Gotową funkcję dopisujemy w wolnym miejscu, np. pod funkcją *update*.

### Ucieczka poza ekran

Gdy wylecimy ptakiem poza ekran, gra ma się zakończyć, tzn. zacząć od nowa.
Co to znaczy, że nasz aktor przemieścił się poza ekran?
To znaczy, że jego współrzędne znajdują się poza ekranem.

Ponieważ nasza postać porusza się jedynie góra-dół, ograniczymy się do sprawdzenia, czy nie wylecieliśmy z góry albo z dołu ekranu.
Jeżeli wylecieliśmy z góry ekranu, to znaczy, że nasza współrzędna $$y$$ jest mniejsza od $$0$$.

```python
if bird.y < 0:
```

Jeżeli natomiast wylecieliśmy z dołu ekranu, to znaczy, że nasza współrzędna $$y$$ jest większa od wysokości (**HEIGHT**) ekranu.

```python
if bird.y < 0 or bird.y > HEIGHT:
```

Co chcemy zrobić, gdy ptak wyleci poza ekran?
Chcemy zrestartować grę, wywołujemy więc przygotowaną wcześniej funkcję *resetuj*.

```python
if bird.y < 0 or bird.y > HEIGHT:
    reset()
```

Gotową instrukcję dopisujemy na koniec części aktualizującej, czyli funkcji *update*.

```python
def update():
    ...

    if bird.y < 0 or bird.y > WIDTH:
        reset()
```

### Kolizja z rurą

W jaki sposób wykryć, że ptak uderzył w rurę?
Musimy sprawdzić, czy aktor reprezentujący ptaka i aktor reprezentujący rurę są ze sobą w **kolizji**.
Co to oznacza, że dwaj aktorzy są ze sobą w kolizji?
To znaczy, że prostokąty, które reprezentują ich grafiki, **nachodzą na siebie**.
Można to sprawdzić na wiele sposobów, ale biblioteka PyGameZero ma do tego wbudowaną funkcję: **colliderect**.

W celu sprawdzenie, czy ptak jest w kolizji z górną rurą, zapiszemy:

```python
if bird.colliderect(pipe_top):
```

Oczywiście nie interesuje nas tylko uderzenie w górną rurę, ale także i w dolną.
W gruncie rzeczy ptak może zahaczyć o górną rurę **lub** dolną.
Dodajmy więc to do naszego warunku.

```python
if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
```

Co chcemy zrobić, gdy ptak uderzy w którąś z rur?
Podobnie jak w przypadku, gdy ptak wyleci poza ekran, chcemy zresetować grę.

```python
if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
    reset()
```

Gotową instrukcję dopisujemy na koniec części aktualizującej, czyli funkcji *update*.

```python
def update():
    ...

    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        reset()
```

### Pełny kod

Dotychczasowy pełny kod naszej gry przedstawiony jest poniżej.

```python
import pgzrun
import random


WIDTH = 400
HEIGHT = 700

TITLE = "PyGameZero Flappy Bird"

gravity = 0.3

bird = Actor("bird1.png")
bird.x = 75
bird.y = 200
bird.vy = 0

pipe_top = Actor("top", anchor=("left", "bottom"))
pipe_bottom = Actor("bottom", anchor=("left", "top"))


def draw():
    screen.blit("bg.png", (0, 0))
    pipe_top.draw()
    pipe_bottom.draw()
    bird.draw()


def update():
    bird.vy += gravity
    bird.y += bird.vy

    pipe_top.left -= 3
    pipe_bottom.left -= 3

    if pipe_top.x < -100:
        set_pipes()

    if bird.y < 0 or bird.y > WIDTH:
        reset()

    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        reset()


def on_key_down():
    bird.vy = -7


def set_pipes():
    gap = random.randint(200, 500)
    pipe_top.pos = (WIDTH, gap - 70)
    pipe_bottom.pos = (WIDTH, gap + 70)


def reset():
    bird.x = 75
    bird.y = 200
    bird.vy = 0
    set_pipes()


set_pipes()
pgzrun.go()
```

## Pełna gra

Pełna implementacja dostępna jest poniżej.

{% embed url="https://github.com/blackbat13/flappybirdpygamezero" %}
Flappy Bird PyGameZero
{% endembed %}