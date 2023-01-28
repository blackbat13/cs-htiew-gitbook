# Asteroidy

## Wstęp

Kosmos, statki kosmiczne, asteroidy, lasery: tym się właśnie dziś zajmiemy!
Stworzymy naszą pierwszą grę kosmiczną!

### Czego się nauczysz

- Pracy z listami.
- Dodawania nowych elementów do gry w trakcie jej działania.
- Usuwania elementów gry w trakcie jej działania.
- Odczytywania pozycji myszki.
- Planowania wykonania akcji z opóźnieniem.

### Grafiki do pobrania

{% file src="../../../.gitbook/assets/images_asteroids.zip" %}
Grafiki do gry Asteroidy
{% endfile %}

### Dźwięki do pobrania

{% file src="../../../.gitbook/assets/sounds_asteroids.zip" %}
Dźwięki do gry Asteroidy
{% endfile %}

### Muzyka do pobrania

{% file src="../../../.gitbook/assets/music_asteroids.zip" %}
Muzyka do gry Asteroidy
{% endfile %}

## Gra

![Asteroidy](../../../.gitbook/assets/asteroidsGame.gif)

Założenie gry jest proste: poruszamy statkiem u dołu ekranu, omijamy asteroidy, strzelamy do nich i zdobywamy punkty!
Powyższa animacja pokazuje, jak będzie wyglądać nasza gra.

# Wstępna konfiguracja

Zaczynamy standardowo: tworzymy nowy projekt, instalujemy bibliotekę, pobieramy materiały i umieszczamy je w odpowiednich miejscach.
Nasz projekt możemy nazwać np. "Asteroids" albo "Asteroidy". Gdy już utworzymy projekt, tworzymy w nim nowe katalogi *images*, *sounds* oraz *music*. Następnie pobieramy wyżej wymienione materiały, rozpakowujemy je, a zawartość przerzucamy do odpowiednich katalogów. Pozostało nam jeszcze zainstalować bibliotekę: w okienku terminala wypisujemy standardowo polecenie `pip install pgzero`.

## Podstawowy szablon

### Biblioteki

Na początek dopisujemy odpowiednie biblioteki do naszej gry.
Tym razem, poza standardowymi, będziemy jeszcze potrzebowali biblioteki **pygame**, żeby móc odczytać pozycję myszy na ekranie, a także żeby móc ukryć wskaźnik myszy.

```python
import pgzrun
import pygame
import random
```

### Przygotowujemy ekran gry

Na początek ustalamy rozmiar okna i wyświetlamy tło naszej gry z grafiki *bg.png* za pomocą funkcji `screen.blit` w części rysującej *draw*.
Rozmiar okna powinien być zgodny z rozmiarem grafiki tła, tzn. $$600\times900$$.

```python
WIDTH = 600
HEIGHT = 900


def draw():
    screen.blit("bg", (0, 0))
```

### Aktualizacja

Potrzebna jest nam jeszcze funkcja *update*, którą standardowo umieszczamy pod funkcją *draw* i wpisujemy w niej jedną instrukcję: **pass**.

```python
def update():
    pass
```

### Uruchomienie gry

Na końcu naszego kodu dopisujemy instrukcję `pgzrun.go()` uruchamiającą naszą grę.

### Pełny kod

```python
import pgzrun
import pygame
import random


WIDTH = 600
HEIGHT = 900


def draw():
    screen.blit("bg", (0, 0))


def update():
    pass


pgzrun.go()
```

## Statek

Głównym aktorem naszej gry, w którego wcieli się gracz, będzie statek kosmiczny. Będziemy go wyświetlać na dole ekranu i poruszać na boki za pomocą myszy.
### Tworzymy statek

Naszego aktora tworzymy na górze, zaraz przed funkcją *draw*. Utworzymy go na podstawie grafiki *ship.png* i zapiszemy w zmiennej *ship*.

```python
ship = Actor("ship")
```

Statek umieścimy na środku ekranu ($$WIDTH / 2$$), na samym dole z zachowaniem marginesu $$60$$ pikseli ($$HEIGHT - 60$$).

```python
ship = Actor("ship")
ship.x = WIDTH / 2
ship.y = HEIGHT - 60
```

### Rysujemy statek

Gdy już mamy utworzonego aktora, możemy go wyświetlić na ekranie. Dopisujemy instrukcję rysującą statek (`ship.draw()`) na końcu funkcji *draw*.

```python
def draw():
    ...
    ship.draw()
```

### Poruszamy statkiem

Statkiem będziemy poruszać w lewo/prawo.
Nasza postać będzie sterowana za pomocą myszki: statek będzie leciał w kierunku, w którym znajduje się wskaźnik myszy. W tym celu musimy nadać naszemu statkowi jakąś prędkość poziomą. Dopiszemy więc do naszego statku zmienną **vx** z początkową wartością np. $$5$$, zaraz pod ustaleniem pozycji statku na ekranie.

```python
ship.vx = 5
```

W części aktualizującej usuwamy instrukcję *pass*. Na początku odczytamy aktualną pozycję wskaźnika myszy za pomocą funkcji `pygame.mouse.get_pos()` z biblioteki *pygame*. Ponieważ funkcja ta zwraca nam współrzędne wskaźnika myszy ($$x$$ oraz $$y$$), to jej wynik zapiszemy w dwóch zmiennych: **mouse_x** oraz **mouse_y**.

```python
def update():
    mouse_x, mouse_y = pygame.mouse.get_pos()
```

Teraz pozostało nam sprawdzić, z której strony znajduje się wskaźnik myszy względem statku: z lewej czy z prawej. Jeżeli współrzędna $$x$$ myszy jest mniejsza od współrzędnej $$x$$ statku, to znaczy, że mysz znajduje się z lewej strony statku. Dopisujemy więc instrukcję warunkową ze wspomnianym warunkiem na koniec funkcji *update*.

```python
def update():
    ...
    if mouse_x < ship.x:
```

Jeżeli tak jest, to powinniśmy statek przesunąć w lewo zgodnie z jego prędkością. W tym celu odejmujemy prędkość statku (**vx**) od jego współrzędnej $$x$$.

```python
def update():
    ...
    if mouse_x < ship.x:
        ship.x -= ship.vx
```

Podobnie postępujemy przy ruchu w prawą stronę. Zaczynamy od warunku: sprawdzamy, czy współrzędna $$x$$ myszy jest większa od współrzędnej $$x$$ statku.

```python
def update():
    ...
    if mouse_x > ship.x:
```

Poruszamy statkiem w prawo, tzn. dodajemy jego prędkość do pozycji $$x$$.

```python
def update():
    ...
    if mouse_x > ship.x:
        ship.x += ship.vx
```

Pełna funkcja *update* będzie więc wyglądała tak jak poniżej.

```python
def update():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x < ship.x:
        ship.x -= ship.px
    if mouse_x > ship.x:
        ship.x += ship.vx
```

### Pełny kod

```python
import pgzrun
import pygame
import random


WIDTH = 600
HEIGHT = 900

ship = Actor("ship")
ship.x = WIDTH / 2
ship.y = HEIGHT - 60
ship.vx = 5


def draw():
    screen.blit("bg", (0, 0))
    ship.draw()


def update():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x < ship.x:
        ship.x -= ship.px

    if mouse_x > ship.x:
        ship.x += ship.vx


pgzrun.go()
```

## Asteroidy

Główne zagrożenie w naszej grze będą stanowić asteroidy "spadające" z góry ekranu.

### Przygotowujemy asteroidy

Czas przygotować asteroidy.
Chcemy, aby było w grze wyświetlało się kilka asteroid naraz. 
W tym celu potrzebna nam będzie **lista**. Lista pozwala nam przechowywać wiele elementów jeden po drugim, zapisanych w jednej zmiennej o typie listy właśnie.
Na początku tworzymy pustą listę, którą przechowamy w zmiennej **asteroids_list**. W celu utworzenia pustej listy do naszej zmiennej przypiszemy puste nawiasy kwadratowe: **[]**. Nową zmienną utworzymy pod statkiem, czyli zaraz nad funkcją *draw*.

```python
asteroids_list = []
```

Teraz utworzymy funkcję, za pomocą której będziemy dodawać losowe asteroidy w trakcie trwania gry.
Na początku asteroid będzie znajdował się nad ekranem, tak by efekt "spadania" wyglądał naturalniej. Na końcu naszego kodu, zaraz przed instrukcją *pgzrun.go()* tworzymy nową funkcję **add_asteroid**.

```python
def add_asteroid():
```

Na początku utworzymy nowego aktora z grafiki *asteroid1.png* i zapiszemy go w zmiennej **asteroid**.

```python
def add_asteroid():
    asteroid = Actor("asteroid1")
```

Przypiszmy teraz naszej asteroidzie właściwe współrzędne. Jako współrzędną $$x$$ przyjmiemy losową wartość z przedziału $$<20, WIDTH-20>$$ wylosowaną za pomocą funkcji `random.randint` z biblioteki *random*.


```python
def add_asteroid():
    ...
    asteroid.x = random.randint(20, WIDTH-20)
```

Do współrzędnej $$y$$ przypiszemy wartość $$-10$$, tak by nowa asteroida znalazła się ponad górną krawędzią ekranu.

```python
def add_asteroid():
    ...
    asteroid.y = -10
```

Teraz pozostało nam wylosować prędkość pionową, którą zapiszemy w asteroidzie w zmiennej $$vy$$. Wartość prędkości pionowej wylosujemy z przedziału $$<2, 10>$$, ponownie korzystając z funkcji `random.randint`.

```python
def add_asteroid():
    ...
    asteroid.vy = random.randint(2, 10)
```

Pozostało nam dopisać naszą nową asteroidę do listy asteroid. W tym celu skorzystamy z metody **append**, która dodaje nowy element do listy. Metodę tę wywołamy pisząc `asteroids_list.append` w nawiasach podając naszą nową asteroidę.

```python
def add_asteroid():
    ...
    asteroids_list.append(asteroid)
```

Nasza pełna funkcja *add_asteroid* przedstawiona jest poniżej.


```python
def add_asteroid():
    asteroid = Actor("asteroid1")
    asteroid.x = random.randint(20, WIDTH-20)
    asteroid.y = -10
    asteroid.vy = random.randint(2, 10)
    asteroids_list.append(asteroid)
```

### Dodajemy losowo asteroidy

W części aktualizującej (*update*) będziemy losowo dodawać asteroidy w każdej klatce, z odpowiednio małym prawdopodobieństwem. W tym celu sprawdzimy, czy wylosowana liczba rzeczywista z przedziału $$<0, 1)$$ jest mniejsza od jakiejś ustalonej wartości, np. $$0.05$$. Liczbę rzeczywistą wylosujemy za pomocą funkcji `random.random()`. Instrukcję warunkową z wspomnianym warunkiem dopisujemy na końcu funkcji *update*.

```python
def update():
    ...
    if random.random() < 0.05:
```

Jeżeli warunek jet spełniony to dodamy nową asteroidę wywołując naszą funkcję *add_asteroid*.

```python
def update():
    ...
    if random.random() < 0.05:
        add_asteroid()
```

### Przemieszczamy asteroidy

Teraz czas na aktualizację pozycji asteroid.
W tym celu musimy przejść przez wszystkie elementy naszej listy i dla każdego wykonać odpowiednie operacje.
Robimy to w części aktualizującej.
Ponieważ będziemy usuwać asteroidy, które wyleciały poza ekran, to w pętli musimy przejść przez **kopię** listy asteroid, którą tworzymy pisząc dwukropek w nawiasach kwadratowych po nazwie listy: `asteroids_list[:]`.

Dla zachowania porządku aktualizację asteroid zapiszemy w nowej funkcji **update_asteroids**, którą utworzymy zaraz pod funkcją *update*.

```python
def update_asteroids():
```

Zaczynamy od napisania pętli przechodzącej przez wszystkie asteroidy w kopii listy.

```python
def update_asteroids():
    for asteroid in asteroids_list[:]:
```

Dla każdej asteroidy będziemy przemieszczać ją zgodnie z jej prędkością, więc do jej współrzędnej $$y$$ dodajemy jej prędkość *vy*.

```python
def update_asteroids():
    for asteroid in asteroids_list[:]:
        asteroid.y += asteroid.vy
```

Żeby nasza gra nie spowalniała po pewnym czasie, powinniśmy na bieżąco usuwać asteroidy, których już nie widać na ekranie. Dlatego dopisujemy w pętli instrukcję warunkową sprawdzającą, czy asteroida wyleciała poza ekran, tzn. czy jej współrzędna $$y$$ jest większa od $$HEIGHT + 50$$ (dodajemy $$50$$ tak by cała asteroida zdążyła wylecieć poza ekran).

```python
def update_asteroids():
    for asteroid in asteroids_list[:]:
        asteroid.y += asteroid.vy
        if asteroid.y > HEIGHT + 50:
```

Jeżeli asteroida opuściła ekran gry to usuwamy ją z listy za pomocą metody **remove**, jako argument podając asteroidę do usunięcia, podobnie jak robiliśmy przy dodawaniu asteroidy do listy.

```python
def update_asteroids():
    for asteroid in asteroids_list[:]:
        asteroid.y += asteroid.vy
        if asteroid.y > HEIGHT + 50:
            asteroids_list.remove(asteroid)
```

Pozostało nam wywołać naszą nową funkcję na końcu funkcji *update*.

```python
def update():
    ...
    update_asteroids()
```

### Rysujemy asteroidy

Pozostało nam narysować asteroidy na ekranie. W tym celu w części rysującej (*draw*) musimy ponownie przejść przez całą listę i narysować każdą asteroidę osobno. Wewnątrz funkcji *draw*, zaraz po wypełnieniu ekranu grafiką tła, a przed narysowaniem statku (tak żeby statek był zawsze na wierzchu), dopisujemy pętlę przechodzącą przez każdą asteroidę z listy asteroid (tym razem nie musimy tworzyć kopii listy, ponieważ nie będziemy nic usuwać).

```python
def draw():
    ...
    for asteroid in asteroids_list:
    ...
```

Wewnątrz pętli rysujemy asteroidy wywołując metodę *draw* na zmiennej *asteroid*.

```python
def draw():
    ...
    for asteroid in asteroids_list:
        asteroid.draw()
    ...
```

Pełna funkcja rysująca pokazana jest poniżej.

```python
def draw():
    screen.blit("bg", (0, 0))
    for asteroid in asteroids_list:
        asteroid.draw()
        
    ship.draw()
```

### Pełny kod

```python
import pgzrun
import pygame
import random


WIDTH = 600
HEIGHT = 900

ship = Actor("ship")
ship.x = WIDTH / 2
ship.y = HEIGHT - 60
ship.vx = 5

asteroids_list = []


def draw():
    screen.blit("bg", (0, 0))
    for asteroid in asteroids_list:
        asteroid.draw()

    ship.draw()


def update():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x < ship.x:
        ship.x -= ship.px

    if mouse_x > ship.x:
        ship.x += ship.vx

    if random.random() < 0.05:
        add_asteroid()

    update_asteroids()
    

def update_asteroids():
    for asteroid in asteroids_list[:]:
        asteroid.y += asteroid.vy
        if asteroid.y > HEIGHT + 50:
            asteroids_list.remove(asteroid)


def add_asteroid():
    asteroid = Actor("asteroid1")
    asteroid.x = random.randint(20, WIDTH-20)
    asteroid.y = -10
    asteroid.vy = random.randint(2, 10)
    asteroids_list.append(asteroid)


pgzrun.go()
```

## Lasery

Nasz statek będzie strzelał laserami. To one będą pozwalały zniszczyć asteroidy, które stanowią zagrożenie.

### Przygotowujemy lasery

Podobnie jak asteroidy, także lasery będziemy przechowywać w liście. Tworzymy więc nową pustą listę, którą nazwiemy **lasers_list** i umieścimy zaraz pod listą asteroid.

```python
lasers_list = []
```

Teraz przyda nam się funkcja, która posłuży nam do dodawania nowych laserów do listy. Stworzymy więc pomocniczą funkcję **add_laser**, którą umieścimy zaraz pod funkcją *add_asteroid*.

```python
def add_laser():
```

Na początku funkcji utworzymy nowego aktora z grafiki *laser.png* i zapiszemy go w zmiennej o nazwie **laser**.

```python
def add_laser():
    laser = Actor("laser")
```

Teraz ustalimy początkową pozycję naszego lasera. Chcemy, żeby była taka sama jak pozycja statku, ponieważ to za jego pomocą strzelamy. W związku z tym do pozycji lasera (*laser.pos*) przypiszemy pozycję statku (*ship.pos*).

```python
def add_laser():
    ...
    laser.pos = ship.pos
```

Naszemu laserowi powinniśmy także nadać jakąś prędkość pionową (*laser.vy*), np. $$-8$$, by laser poruszał się do góry.

```python
def add_laser():
    ...
    laser.vy = -8
```

Wreszcie na końcu dodajemy nasz nowy laser do listy laserów (*lasers_list*) za pomocą metody *append*.

```python
def add_laser():
    ...
    lasers_list.append(laser)
```

Pełna funkcja dodająca nowy laser przedstawiona jest poniżej.

```python
def add_laser():
    laser = Actor("laser")
    laser.pos = ship.pos
    laser.vy = -8
    lasers_list.append(laser)
```

### Rysujemy lasery

Zanim przejdziemy do strzelania, narysujmy nasze lasery na ekranie. Oczywiście jeszcze nie mamy laserów do narysowania, ale gdy już będziemy mogli strzelać, to je zobaczymy. Wewnątrz funkcji `draw`, zaraz przed narysowaniem statku, a pod narysowaniem asteroid, dopisujemy pętlę przechodzącą przez wszystkie lasery na liście *lasers_list*.

```python
def draw():
    ...
    for laser in lasers_list:
    ...
```

Wewnątrz pętli będziemy rysować nasze lasery.

```python
def draw():
    ...
    for laser in lasers_list:
        laser.draw()
    ...
```

Pełna funkcja rysująca pokazana jest poniżej.

```python
def draw():
    screen.blit("bg", (0, 0))
    for asteroid in asteroids_list:
        asteroid.draw()

    for laser in lasers_list:
        laser.draw()

    ship.draw()
```

### Strzelamy

Czas na strzelanie laserami! Strzały będziemy oddawać po każdym kliknięciu myszy. Kliknięcia myszy odczytujemy za pomocą funkcji *on_mouse_down* z biblioteki *Pygame Zero*. Dopisujemy więc nową funkcję, na końcu naszego kodu, zaraz przed instrukcją `pgzrun.go()`.

```python
def on_mouse_down(pos):
```

Wewnątrz funkcji wywołamy naszą funkcję *add_laser*, aby dodać nowy laser do gry.

```python
def on_mouse_down(pos):
    add_laser()
```

Warto także skorzystać z dźwięku *laser* pisząc instrukcję `sounds.laser.play()`.

```python
def on_mouse_down(pos):
    add_laser()
    sounds.laser.play()
```

### Przemieszczamy lasery

W tym momencie nasze lasery są dość statyczne. Chcielibyśmy, żeby się poruszały, jak to lasery mają w zwyczaju, a przynajmniej tak przedstawiają to filmy science-fiction. Z laserami postąpimy podobnie jak z asteroidami i dodamy nową funkcję **update_lasers**, którą dla zachowania porządku dopiszemy zaraz pod funkcją *update_asteroids*.

```python
def update_lasers():
```

Chcemy aktualizować pozycję wszystkich laserów, potrzebna nam więc pętla przechodząca przez wszystkie lasery na liście *lasers_list*. Nasze lasery będziemy jednak usuwać, gdy wylecą poza ekran, więc potrzebna nam **kopia** listy, którą tworzymy pisząc **lasers_list[:]**, podobnie jak w przypadku asteroid.

```python
def update_lasers():
    for laser in lasers_list[:]:
```

Wewnątrz pętli przemieszczamy nasz laser zgodnie z jego prędkością, więc do współrzędnej $$y$$ dodajemy prędkość pionową lasera (*laser.vy*).

```python
def update_lasers():
    for laser in lasers_list[:]:
        laser += laser.vy
```

Teraz pora sprawdzić, czy laser wyleciał poza ekran. W tym celu sprawdzimy, czy jego pozycja $$y$$ jest mniejsza od ujemnej wartości jego wysokości. W ten sposób upewnimy się, że cały laser wyleciał poza ekran, a nie tylko jego część. Wysokość lasera możemy odczytać pisząc `laser.height`. Dopisujemy więc instrukcję warunkową.

```python
def update_lasers():
    for laser in lasers_list[:]:
        laser += laser.vy
        if laser.y < -laser.height:
```

Jeżeli laser wyleci poza ekran, to chcemy go usunąć z listy laserów i tym samym z naszej gry. Korzystamy więc z metody **remove**, tak jak wcześniej przy asteroidach.

```python
def update_lasers():
    for laser in lasers_list[:]:
        laser += laser.vy
        if laser.y < -laser.height:
            lasers_list.remove(laser)
```

Pozostało nam wywołać naszą nową funkcję na końcu funkcji *update*, tak by nasze lasery były aktualizowane.

```python
def update():
    ...
    update_lasers()
```

### Niszczymy asteroidy

Cóż to za lasery, które nie niszczą asteroid? Można powiedzieć, że są to całkowicie normalne lasery, ale nie w naszej grze! Czas zniszczyć kilka asteroid. W tym celu utworzymy nową funkcję **update_lasers_hits**, którą dopiszemy zaraz pod naszą poprzednią funkcją *update_lasers*.

```python
def update_lasers_hits():
```

Dla każdego laseru będziemy sprawdzać, czy trafił on w którąś z asteroid. Jeżeli tak, to usuniemy zarówno laser jak i asteroidę. Dopisujemy więc pętlę, która przejdzie przez wszystkie lasery w **kopii** listy *lasers_list*.

```python
def update_lasers_hits():
    for laser in lasers_list[:]:
```

Asteroid mamy wiele, jak więc sprawdzić, czy w którąś trafił laser? Potrzebna nam kolejna pętla, która przejdzie przez wszystkie asteroidy w **kopii** listy *asteroids_list*.

```python
def update_lasers_hits():
    for laser in lasers_list[:]:
        for asteroid in asteroids_list[:]:
```

Mamy już zarówno laser jak i asteroidę. Sprawdźmy więc, czy są w kolizji! W tym celu skorzystamy ze znanej nam funkcji *colliderect*.

```python
def update_lasers_hits():
    for laser in lasers_list[:]:
        for asteroid in asteroids_list[:]:
            if laser.colliderect(asteroid):
```

Jeżeli laser trafił w asteroidę, to usuwamy zarówno laser jak i asteroidę z odpowiednich list za pomocą metody *remove*.

```python
def update_lasers_hits():
    for laser in lasers_list[:]:
        for asteroid in asteroids_list[:]:
            if laser.colliderect(asteroid):
                lasers_list.remove(laser)
                asteroids_list.remove(asteroid)
```

Dopiszmy teraz wywołanie naszej nowej funkcji na koniec funkcji *update*.

```python
def update():
    ...
    update_lasers_hits()
```

Gdybyśmy teraz przetestowali naszą grę, to może się zdarzyć, że czasem wyłączy się z komunikatem błędu w konsoli. Dzieje się tak, gdy laser trafi w jedną asteroidę, usuniemy go z listy, ale jest także jednocześnie w kolizji z jeszcze inną asteroidą. Wówczas spróbujemy usunąć ten sam laser drugi raz, ale przecież już go wcześniej usunęliśmy, więc próba usunięcia usuniętego lasera zakończy się błędem. Możemy jednak temu zapobiec w bardzo prosty sposób. Wystarczy że dopiszemy do naszej funkcji *update_lasers_hits* instrukcję **break** zaraz po usunięciu lasera i asteroidy. Instrukcja **break** sprawi, że wyjdziemy z pętli przechodzącej po wszystkich asteroidach i przejdziemy do kolejnego lasera.

```python
def update_lasers_hits():
    for laser in lasers_list[:]:
        for asteroid in asteroids_list[:]:
            if laser.colliderect(asteroid):
                lasers_list.remove(laser)
                asteroids_list.remove(asteroid)
                break
```

### Pełny kod

```python
import pgzrun
import pygame
import random


WIDTH = 600
HEIGHT = 900

ship = Actor("ship")
ship.x = WIDTH / 2
ship.y = HEIGHT - 60
ship.vx = 5

asteroids_list = []
lasers_list = []


def draw():
    screen.blit("bg", (0, 0))
    for asteroid in asteroids_list:
        asteroid.draw()

    for laser in lasers_list:
        laser.draw()

    ship.draw()
    

def update():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x < ship.x:
        ship.x -= ship.px

    if mouse_x > ship.x:
        ship.x += ship.vx

    if random.random() < 0.05:
        add_asteroid()

    update_asteroids()
    update_lasers()
    update_lasers_hits()
    

def update_asteroids():
    for asteroid in asteroids_list[:]:
        asteroid.y += asteroid.vy
        if asteroid.y > HEIGHT + 50:
            asteroids_list.remove(asteroid)


def update_lasers():
    for laser in lasers_list[:]:
        laser += laser.vy
        if laser.y < -laser.height:
            lasers_list.remove(laser)


def update_lasers_hits():
    for laser in lasers_list[:]:
        for asteroid in asteroids_list[:]:
            if laser.colliderect(asteroid):
                lasers_list.remove(laser)
                asteroids_list.remove(asteroid)
                break


def add_asteroid():
    asteroid = Actor("asteroid1")
    asteroid.x = random.randint(20, WIDTH-20)
    asteroid.y = -10
    asteroid.vy = random.randint(2, 10)
    asteroids_list.append(asteroid)


def add_laser():
    laser = Actor("laser")
    laser.pos = ship.pos
    laser.vy = -8
    lasers_list.append(laser)


def on_mouse_down(pos):
    add_laser()
    sounds.laser.play()


pgzrun.go()
```

<!-- ## Pełna gra

```python
import pgzrun
import random
import pygame
import shelve

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

wyniki = shelve.open("wyniki")
if "highscore" not in wyniki:
    wyniki["highscore"] = 0
wyniki.close()

def draw():
    screen.blit("tlo", (0, 0))
    draw_meteory()
    draw_lasery()
    statek.draw()
    draw_punkty()
    draw_zycia()

    if statek.zycia == 0:
        screen.draw.text("Game Over", center=(WIDTH / 2, HEIGHT / 2), fontsize=90)

        wyniki = shelve.open("wyniki")
        highscore = wyniki["highscore"]
        wyniki.close()

        screen.draw.text("Best: " + str(highscore), center=(WIDTH / 2, HEIGHT / 2 + 80), fontsize = 90, color="yellow")


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
            if statek.zycia > 0:
                sounds.tarcza.play()
            else:
                sounds.eksplozja.play()
                sounds.game_over.play()
                music.fadeout(1)

                wyniki = shelve.open("wyniki")
                if statek.punkty > wyniki["highscore"]:
                    wyniki["highscore"] = statek.punkty
                wyniki.close()


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
                sounds.trafienie.play()
                break


def on_mouse_down():
    if statek.strzaly > 0:
        dodaj_laser()
        statek.strzaly -= 1
        clock.schedule(dodaj_strzal, 1)
        sounds.laser.play()


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

music.play("space")
music.set_volume(0.3)

pgzrun.go()
``` -->