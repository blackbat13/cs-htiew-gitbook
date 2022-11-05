# Flappy Bird

## Wstęp

Dzisiaj odtworzymy jedną z kultowych gier mobilnych: Flappy Bird.

### Czego się nauczysz

* Jak dodać grawitację i skok do gry
* Jak stworzyć i obsłużyć proste menu
* Jak stworzyć "nieskończoną" grę bazującą na prostych założeniach

### Grafiki do pobrania

Zanim zaczniemy, pobierz poniższe grafiki, rozpakuj i umieść w katalogu **images** w projekcie gry.

{% file src="../../.gitbook/assets/grafiki_flappy.zip" %}
Grafiki do gry Flappy Bird
{% endfile %}

Grafiki pochodzą ze strony projektu pgzero: [https://github.com/lordmauve/pgzero/tree/master/examples/flappybird/images](https://github.com/lordmauve/pgzero/tree/master/examples/flappybird/images)

Grafiki przycisków pochodzą ze strony: [https://kenney.nl/](https://kenney.nl)

### Efekty dźwiękowe do pobrania

Zanim zaczniemy, pobierz poniższe efekty dźwiękowe i umieść je w katalogu **sounds** w projekcie gry.

{% file src="../../.gitbook/assets/dzwieki_flappy.zip" %}
Efekty dźwiękowe do gry Flappy Bird
{% endfile %}

Efekty dźwiękowe pochodzą ze strony: [https://www.sounds-resource.com/mobile/flappybird/sound/5309/](https://www.sounds-resource.com/mobile/flappybird/sound/5309/)

## Nasz cel

![Flappy Bird - animacja](../../.gitbook/assets/flappyGame.gif)

## Tworzymy okno gry

Jak zwykle zaczynamy od podstaw. Wymiary naszego okna są zależne od wymiarów grafiki tła i wynoszą $$400\times700$$. Ustawiamy więc odpowiednie wymiary i wypełniamy tło grafiką _tlo.png_ za pomocą polecenia `screen.blit()`.

```python
import pgzrun
import random


TITLE = "PyGameZero Flappy Bird"
WIDTH = 400
HEIGHT = 700


def draw():
    screen.blit("tlo.png", (0, 0))


def update():
    pass


pgzrun.go()
```

## Ptak

Zacznijmy od naszej głównej postaci: ptaka.

### Dodajemy aktora

Na samym początku dodajemy nowego aktora z grafiki _ptak1.png_. Umieścimy go z lewej strony ekranu, na środku, pod współrzędnymi $$(75, 200)$$.

```python
ptak = Actor("ptak1.png")
ptak.x = 75
ptak.y = 200
```

### Rysujemy

Wyświetlmy naszą nową postać na ekranie. W części rysującej dopisujemy odpowiednie polecenie.

```python
def draw():
    screen.blit("tlo.png", (0, 0))
    ptak.draw()
```

### Grawitacja

Jak na razie nasza postać jest bardzo statyczna i tkwi w jednym miejscu. Urozmaićmy więc trochę jej życie i dodajmy siłę grawitacji. Grawitacja w naszej grze będzie działać podobnie do tej, którą znamy z codziennego życia: będzie ściągać postać w dół. Zanim jednak będziemy mogli dodać oddziaływanie grawitacji na postać, musimy ustalić siłę grawitacji. Dodajmy więc zmienną `grawitacja` na początku naszego kodu, zaraz pod wymiarami okna, i przypiszmy jej wartość $$0.3$$.

```python
grawitacja = 0.3
```

Teraz czas zaaplikować grawitację do postaci ptaka. Grawitacja powinna wpływać na prędkość pionową postaci, musimy więc tę prędkość dopisać do naszego aktora.

```python
ptak.py = 0
```

Teraz, w każdej klatce animacji, prędkość postaci będzie zwiększana o siłę grawitacji. Z kolei pozycja aktora będzie się zmieniać zgodnie z jego prędkością. Dopisujemy więc obliczenia w części aktualizującej.

```python
def update():
    ptak.py += grawitacja
    ptak.y += ptak.py
```

### Latanie

Mamy już grawitację, czas więc dodać możliwość próby przezwyciężenia tej wielkiej siły: zdolność latania. Nasza postać będzie podnosić się lekko do góry za każdym razem, gdy wciśniemy jakiś (dowolny) przycisk na klawiaturze. Potrzebna nam więc funkcja `on_key_down`. W celu zasymulowania unoszenia się postaci do góry wystarczy, że nadamy jej odpowiednią prędkość wzlotową.

```python
def on_key_down():
    ptak.py = -7
```

### Pełny kod

Dotychczasowy pełny kod naszej gry przedstawiony jest poniżej.

```python
import pgzrun
import random


TITLE = "PyGameZero Flappy Bird"
WIDTH = 400
HEIGHT = 700

grawitacja = 0.3

ptak = Actor("ptak1.png")
ptak.x = 75
ptak.y = 200
ptak.py = 0


def draw():
    screen.blit("tlo.png", (0, 0))
    ptak.draw()


def update():
    ptak.py += grawitacja
    ptak.y += ptak.py


def on_key_down():
    ptak.py = -7


pgzrun.go()
```

## Rury

Czas dodać naszego przeciwnika w grze: rury. Jak zwykle zaczynamy od dodania nowych aktorów. Tym razem będzie ich dwóch: górna rura (`rura_gora`) i dolna rura (`rura_dol`). Utworzymy ich tak jak zazwyczaj z niewielką różnicą: ustalimy im odpowiednie _**kotwice**_. Kotwica pozwala nam wybrać punkt grafiki, według którego będziemy ją umieszczać na ekranie. Można to sobie wyobrazić jako miejsce, w którym "trzymamy" grafikę, gdy ją przemieszczamy. Domyślnie grafikę poruszamy względem jej środka, ale możemy też wybrać inne miejsce zaczepienia. Ze względu na charakter rur w naszej grze jest to duże ułatwienie.

Dla górnej rury ustawimy kotwicę w jej lewym **dolnym** rogu. Dla dolnej rury natomiast ustawimy kotwicę w jej lewym **górnym** rogu.

```python
rura_gora = Actor("gora", anchor=("left", "bottom"))
rura_dol = Actor("dol", anchor=("left", "top"))
```

### Rysujemy rury

Gdy już mamy aktorów, czas ich wyświetlić na ekranie. Dodajemy dwie instrukcje w części rysującej naszej gry. Narysujemy je przed narysowaniem postaci ptaka, żeby go nie zasłaniały.

```python
def draw():
    screen.blit("tlo.png", (0, 0))
    rura_gora.draw()
    rura_dol.draw()
    ptak.draw()
```

### Ustawiamy pozycję rur

Główną trudnością w naszej grze będzie niewielka przestrzeń pomiędzy rurami, przez którą musimy przelecieć. 
Żeby gra nie była zbyt przewidywalna, ta przestrzeń powinna pojawiać się na losowej wysokości. 
Stworzymy więc funkcję `ustaw_rury` za pomocą której będziemy losować nową pozycję rur.

```python
def ustaw_rury():
    przerwa = random.randint(200, 500)
    rura_gora.pos = (WIDTH, przerwa - 70)
    rura_dol.pos = (WIDTH, przerwa + 70)
```

Teraz czas wywołać naszą funkcję. Zrobimy to zaraz przed uruchomieniem gry, czyli tuż przed instrukcją `pgzrun.go()`.

```python
ustaw_rury()
pgzrun.go()
```

### Przemieszczamy rury

W każdej klatce animacji nasze rury powinny przemieszczać się w lewą stronę. 
W tym celu w części aktualizującej będziemy je przesuwać o $$3$$ piksele w lewo.

```python
def update():
    ptak.py += grawitacja
    ptak.y += ptak.py

    rura_gora.left -= 3
    rura_dol.left -= 3
```

Gdy rury znikną z lewej strony ekranu, należy ustawić je ponownie.

```python
    if rura_gora.x < -100:
        ustaw_rury()
```

### Pełny kod

Dotychczasowy pełny kod naszej gry przedstawiony jest poniżej.

```python
import pgzrun
import random


TITLE = "PyGameZero Flappy Bird"
WIDTH = 400
HEIGHT = 700

grawitacja = 0.3

ptak = Actor("ptak1.png")
ptak.x = 75
ptak.y = 200
ptak.py = 0

rura_gora = Actor("gora", anchor=("left", "bottom"))
rura_dol = Actor("dol", anchor=("left", "top"))

def draw():
    screen.blit("tlo.png", (0, 0))
    rura_gora.draw()
    rura_dol.draw()
    ptak.draw()


def update():
    ptak.py += grawitacja
    ptak.y += ptak.py

    rura_gora.left -= 3
    rura_dol.left -= 3

    if rura_gora.x < -100:
        ustaw_rury()


def on_key_down():
    ptak.py = -7


def ustaw_rury():
    przerwa = random.randint(200, 500)
    rura_gora.pos = (WIDTH, przerwa - 70)
    rura_dol.pos = (WIDTH, przerwa + 70)


ustaw_rury()
pgzrun.go()
```

## Koniec gry

Kiedy nasza gra się kończy? Gdy trafimy w rurę, lub wylecimy poza ekran.

### Reset gry

Zacznijmy od zastanowienia się, co chcemy zrobić, gdy gra się skończy, tzn. gdy gracz przegra.
Możemy oczywiście wyświetlić komunikat o przegranej i wyłączyć grę.
Nasza gra ma jednak z założenia wysoki poziom trudności, więc uruchamianie jej raz za razem po każdej przegranej bardzo szybko stałoby się uciążliwe.
Zamiast tego po przegranej **zresetujemy grę**, tzn. zaczniemy ją od nowa.
W tym celu stworzymy nową funkcję *resetuj*.

Co powinniśmy zrobić, aby zresetować grę?
Jakie jej ustawienia musimy przywrócić do początkowych wartości?
Potrzebujemy przywrócić naszego gracza, ptaka, na początkową pozycję i nadać mu właściwą prędkość.
Przytałoby się także ponownie ustawić rury, abyśmy przypadkiem nie wylądowali w środku jeden z nich.

```python
def resetuj():
    ptak.x = 75
    ptak.y = 200
    ptak.py = 0
    ustaw_rury()
```

Gotową funkcję dopisujemy w wolnym miejscu, np. pod funkcją *update*.

### Ucieczka poza ekran

Gdy wylecimy ptakiem poza ekran, gra ma się zakończyć, tzn. zacząć od nowa.
Co to znaczy, że nasz aktor przemieścił się poza ekran?
To znaczy, że jego współrzędne znajdują się poza ekranem.

Ponieważ nasza postać porusza się jedynie góra-dół, ograniczymy się do sprawdzenia, czy nie wylecieliśmy z góry albo z dołu ekranu.
Jeżeli wylecieliśmy z góry ekranu, to znaczy, że nasza współrzędna $$y$$ jest mniejsza od $$0$$.

```python
if ptak.y < 0:
```

Jeżeli natomiast wylecieliśmy z dołu ekranu, to znaczy, że nasza współrzędna $$y$$ jest większa od wysokości (**HEIGHT**) ekranu.

```python
if ptak.y < 0 or ptak.y > HEIGHT:
```

Co chcemy zrobić, gdy ptak wyleci poza ekran?
Chcemy zrestartować grę, wywołujemy więc przygotowaną wcześniej funkcję *resetuj*.

```python
if ptak.y < 0 or ptak.y > HEIGHT:
    resetuj()
```

Gotową instrukcję dopisujemy na koniec części aktualizującej, czyli funkcji *update*.

```python
def update():
    ptak.py += grawitacja
    ptak.y += ptak.py

    rura_gora.left -= 3
    rura_dol.left -= 3

    if rura_gora.x < -100:
        ustaw_rury()

    if ptak.y < 0 or ptak.y > WIDTH:
        resetuj()
```

### Kolizja z rurą

W jaki sposób wykryć, że ptak uderzył w rurę?
Musimy sprawdzić, czy aktor reprezentujący ptaka i aktor reprezentujący rurę są ze sobą w **kolizji**.
Co to oznacza, że dwaj aktorzy są ze sobą w kolizji?
To znaczy, że prostokąty, które reprezentują ich grafiki, **nachodzą na siebie**.
Można to sprawdzić na wiele sposobów, ale biblioteka PyGameZero ma do tego wbudowaną funkcję: **colliderect**.

W celu sprawdzenie, czy ptak jest w kolizji z górną rurą, zapiszemy:

```python
if ptak.colliderect(rura_gora):
```

Oczywiście nie interesuje nas tylko uderzenie w górną rurę, ale także i w dolną.
W gruncie rzeczy ptak może zahaczyć o górną rurę **lub** dolną.
Dodajmy więc to do naszego warunku.

```python
if ptak.colliderect(rura_gora) or ptak.colliderect(rura_dol):
```

Co chcemy zrobić, gdy ptak uderzy w którąś z rur?
Podobnie jak w przypadku, gdy ptak wyleci poza ekran, chcemy zresetować grę.

```python
if ptak.colliderect(rura_gora) or ptak.colliderect(rura_dol):
    resetuj()
```

Gotową instrukcję dopisujemy na koniec części aktualizującej, czyli funkcji *update*.

```python
def update():
    ptak.py += grawitacja
    ptak.y += ptak.py

    rura_gora.left -= 3
    rura_dol.left -= 3

    if rura_gora.x < -100:
        ustaw_rury()

    if ptak.y < 0 or ptak.y > WIDTH:
        resetuj()

    if ptak.colliderect(rura_gora) or ptak.colliderect(rura_dol):
        resetuj() 
```

### Pełny kod

Dotychczasowy pełny kod naszej gry przedstawiony jest poniżej.

```python
import pgzrun
import random


TITLE = "PyGameZero Flappy Bird"
WIDTH = 400
HEIGHT = 700

grawitacja = 0.3

ptak = Actor("ptak1.png")
ptak.x = 75
ptak.y = 200
ptak.py = 0

rura_gora = Actor("gora", anchor=("left", "bottom"))
rura_dol = Actor("dol", anchor=("left", "top"))

def draw():
    screen.blit("tlo.png", (0, 0))
    rura_gora.draw()
    rura_dol.draw()
    ptak.draw()


def update():
    ptak.py += grawitacja
    ptak.y += ptak.py

    rura_gora.left -= 3
    rura_dol.left -= 3

    if rura_gora.x < -100:
        ustaw_rury()

    if ptak.y < 0 or ptak.y > WIDTH:
        resetuj()

    if ptak.colliderect(rura_gora) or ptak.colliderect(rura_dol):
        resetuj() 


def resetuj():
    ptak.x = 75
    ptak.y = 200
    ptak.py = 0
    ustaw_rury()

def on_key_down():
    ptak.py = -7


def ustaw_rury():
    przerwa = random.randint(200, 500)
    rura_gora.pos = (WIDTH, przerwa - 70)
    rura_dol.pos = (WIDTH, przerwa + 70)


ustaw_rury()
pgzrun.go()
```

## Pełna gra

Pełna implementacja dostępna jest poniżej.

{% embed url="https://github.com/blackbat13/flappybirdpygamezero" %}
Flappy Bird PyGameZero
{% endembed %}