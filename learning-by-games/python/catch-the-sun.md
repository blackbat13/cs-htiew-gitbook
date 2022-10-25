# Złap słońce

## Wstęp

Każdy potrzebuje witaminy D, złapmy więc trochę słońca! Nie jest to jednak tak proste, jakby się mogło wydawać! Słońce nagle znika i pojawia się w losowych miejscach. Za każde celne kliknięcie w słońce dostajemy punkt, a za każde pudło tracimy punkt! Im więcej mamy punktów, tym słońce szybciej się porusza! Ile punktów uda Ci się zdobyć?

### Czego się nauczysz

* Jak dodać i narysować postać w grze: aktora
* Jak zmieniać pozycję aktora na ekranie
* Jak odczytywać kliknięcia myszy i wykrywać ich kolizję z aktorem
* Jak wyświetlać i zliczać punkty

### Materiały do pobrania

#### Grafiki

Umieszczamy w katalogu **images**.

![Źródło: [kenney.nl](https://www.kenney.nl/)](../../.gitbook/assets/sun.png)

### Importujemy biblioteki

Zastanówmy się, jakich "narzędzi" będziemy potrzebować. Podstawowym elementem będzie oczywiście nasza biblioteka do tworzenia gier. Docelowo nasze słońce będzie się pojawiało w **losowych** miejscach na ekranie, przyda nam się także biblioteka do liczb losowych. 

Dodajemy więc odpowiednie polecenia na samym początku pliku **main.py** w edytorze:

```python
import pgzrun
import random
```

### Określamy wymiary okna gry

Nasza gra nie musi mieć dużego okna. Co więcej, im mniejsze będzie okno gry, tym gra będzie łatwiejsza! Dlaczego? Słońce będzie miało mniej miejsca do ucieczki, łatwiej więc będzie je złapać. Zacznijmy więc od niewielkiego, dość standardowego wymiaru $800\times600$. W każdej chwili możemy te wymiary zmienić.

```python
WIDTH = 800
HEIGHT = 600
```

### Tworzymy tło

Nasza gra, jak i każda inna, powinna mieć jakieś tło. To będzie prosta gra, więc i niech tło będzie proste: wypełnimy je wybranym przez siebie kolorem. Ponieważ słońce zazwyczaj możemy zaobserwować na niebieskim niebie, takiego też koloru użyjemy. W celu wypełnienia tła wybranym kolorem skorzystamy z metody `screen.fill`, do której jako **argument** przekażemy wybrany kolor za pomocą jego angielskiej nazwy *skyblue*, podanej w formie tekstu:

```python
screen.fill("skyblue")
```

Zachęcam do sprawdzenia innych kolorów i wybrania takiego, który Tobie odpowiada. Pamiętaj: to Twoja gra!

Wypełnienie kolorem umieścimy w części rysującej, tzn. w części `draw`. Pełna implementacja funkcji rysującej wygląda więc następująco:

```python
def draw():
    screen.fill("skyblue")
```

### Pozostałe elementy szablonu

Na koniec pozostało nam uzupełnić nasz program o pozostałe wymagane elementy szablonu, czyli funkcję aktualizującą i polecenie uruchamiające grę.

```python
def update():
    pass


pgzrun.go()
```

### Pełny program z komentarzami

```python
# Importujemy bibliotekę Pygame Zero do tworzenia gier
import pgzrun
# Imporujemy bibliotekę do liczb losowych
import random

# Określamy szerokość i wysokość okna gry
WIDTH = 800
HEIGHT = 600


def draw():
    # Wypełniamy ekran wybranym kolorem
    screen.fill("skyblue")


def update():
    pass


# Uruchamiamy grę
pgzrun.go()
```

### Testujemy działanie

W tym momencie warto już uruchomić naszą "grę" i sprawdzić, czy wszystko działa. Na razie powinniśmy zobaczyć jedynie okno gry wypełnione jasnoniebieskim kolorem, ale od czegoś trzeba zacząć! 

## Rysowanie słońca

Teraz zajmiemy się dodaniem do gry naszej głównej postaci: słońca. Postacie w *pygame zero* reprezentować będziemy jako **aktorów**. Każdy aktor ma swoje właściwości, takie jak grafika czy położenie na ekranie. Aktorzy mogą też wchodzić w interakcję z innymi postaciami (także aktorami) i pozostałymi elementami gry.

### Tworzymy nowego aktora gry

Zaczniemy od utworzenia naszego nowego aktora: słońca. W tym celu potrzebna nam będzie nowa zmienna, w której zapamiętamy informacje o aktorze. Zmienną nazwiemy *sun*, czyli słońce po angielsku. Naszego aktora utworzymy zaraz na początku naszego programu, zaraz pod zdefiniowaniem rozmiarów okna gry. W celu utworzenia nowego aktora skorzystamy z polecenia `Actor`, a jako argument podamy nazwę grafiki reprezentującej nasze słońce. Pamiętaj, że grafika musi się znajdować w katalogu **images**.

```python
sun = Actor("sun")
```

### Rysujemy słońce na ekranie

Gdy już utworzyliśmy naszego aktora, czas go narysować na ekranie. W tym celu dodamy instrukcję `sun.draw()` na **końcu** części rysującej (`draw`).

```python
def draw():
    screen.fill("skyblue")
    sun.draw()
```

### Pełny program

```python
import pgzrun
import random


WIDTH = 800
HEIGHT = 600

# Tworzymy nową postać, nowego aktora naszej gry, na podstawie grafiki sun.png
sun = Actor("sun")


def draw():
    screen.fill(kolor_tla)
    # Rysujemy słońce
    sun.draw()


def update():
    pass


pgzrun.go()
```

### Testujemy działanie

Uruchamiamy i testujemy! Naszym oczom powinno ukazać się słońce, umieszczone w lewym górnym rogu okna gry.

## Uciekające słońce

W tym momencie nasze słońce jest dość statyczne. Chcemy jednak, by zaznało trochę ruchu i "skakało" po ekranie w losowych miejscach.

### Przemieszczamy słońce w losowe miejsce

Zacznijmy od przemieszczenia słońca w losowe miejsce. Będziemy teraz pracować w części **aktualizującej** (`update`), ponieważ nasze słońce powinno się przemieszczać przez cały czas trwania gry. Aby przemieścić słońce w inne miejsce na ekranie, powinniśmy zmienić jego **współrzędne**, tzn. parametry `sun.x` oraz `sun.y`. Przypiszemy im losowe wartości korzystając z metody `random.randint`, do której jako parametry przekażemy przedział, z którego chcemy wylosować wartość. Musimy pamiętać, że współrzędna $x$ powinna się mieścić w szerokości (**WIDTH**) ekranu, a współrzędna $y$ powinna się mieścić w wysokości (**HEIGHT**) ekranu. Dodatkowo warto dodać niewielki margines, powiedzmy $80$ pikseli, tak aby nasze słońce nie wychodziło poza brzegi okna gry.

W części aktualizującej (`update`) usuwamy więc instrukcję `pass` i dopisujemy losowanie nowych współrzędnych naszego słońca.

```python
def update():
    sun.x = random.randint(80, WIDTH - 80)
    sun.y = random.randint(80, HEIGHT - 80)
```

Gdy teraz uruchomimy naszą grę zobaczymy, że słońce faktycznie skacze po ekranie w losowych miejscach. Jest jednak zbyt szybkie, byśmy dali radę je złapać. Musimy je spowolnić.

### Odliczamy czas

Aby spowolnić nasze słońce dodamy do niego swego rodzaju **timer**. Jego zadaniem będzie odliczanie w dół, aż do zera. Gdy timer dojdzie do zera, to dopiero wtedy przemieścimy nasze słońce w inne, losowe miejsce i ponownie ustawimy timer. Na początku dopisujemy timer do naszego słońca, zaraz pod linijką w której tworzymy aktora. Zaczniemy od wartości zero, tak aby już na samym początku słońce przemieściło się w losowe miejsce.

```python
sun = Actor("sun")
sun.timer = 0
```

Teraz, w części aktualizującej, powinniśmy zmniejszać nasz timer o jeden w każdej **klatce** gry. Następnie sprawdzimy, czy timer osiągnął wartość mniejszą lub równą zero, a jeżeli tak, to ustawimy słońce w losowym miejscu (tak jak poprzednio) i ustawimy timer na jakąś ustaloną z góry wartość, np $60$. Zakładając, że nasza gra będzie działać w sześćdziesięciu klatkach na sekundę, to wartość $60$ będzie odpowiadać jednej sekundzie.

```python
def update():
    sun.timer -= 1

    if sun.timer <= 0:
        sun.x = random.randint(80, WIDTH - 80)
        sun.y = random.randint(80, HEIGHT - 80)
        sun.timer = 60
```

### Pełny program

```python
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

sun = Actor("sun")
sun.timer = 0


def draw():
    screen.fill("skyblue")
    sun.draw()


def update():
    sun.timer -= 1

    if sun.timer <= 0:
        sun.x = random.randint(80, WIDTH - 80)
        sun.y = random.randint(80, HEIGHT - 80)
        sun.timer = 60


pgzrun.go()
```

### Testujemy działanie

Uruchamiamy ponownie i sprawdzamy, czy nasze słońce porusza się już w bardziej sensowny sposób.

## Zliczanie punktów

Czas na zliczanie punktów. W tym celu będziemy potrzebowali miejsce (zmienną), gdzie zapamiętamy punkty. Wyświetlimy je na ekranie i będziemy dodawać (lub odejmować) za każde kliknięcie.

### Wyświetlamy punkty

Na początku dopiszemy punkty do naszego aktora, podobnie jak zrobiliśmy z parametrem *timer*. Punkty zaczynamy zliczać od zera.

```python
sun = Actor("sun")
sun.timer = 0
sun.points = 0
```

Teraz czas wyświetlić punkty na ekranie, tak abyśmy mogli sprawdzać, czy naliczają się poprawnie. W tym celu skorzystamy z metody `screen.draw.text`, którą umieścimy na samym końcu części rysującej (`draw`).

```python
screen.draw.text(str(sun.points), center=(WIDTH / 2, 50), color="red", fontsize=100)
```

Pełna implementacja funkcji rysującej wygląda więc następująco:

```python
def draw():
    screen.fill("skyblue")
    sun.draw()
    screen.draw.text(str(sun.points), center=(WIDTH / 2, 50), color="red", fontsize=100)
```

### Zliczanie punktów

W celu zliczania punktów skorzystamy z metody odczytującej kliknięcia na ekranie.

```python
def on_mouse_down(pos):
    if sun.collidepoint(pos):
        sun.points += 1
        sun.timer = 0
    else:
        sun.points -= 1
        sun.timer = 0
```

### Zwiększanie poziomu trudności

Aby gra stawała się coraz trudniejsza, im więcej mamy punktów, uzależnimy wartość parametru *timer* od liczby zdobytych punktów. W tym celu zmodyfikujemy linijkę w części aktualizującej, gdzie resetujemy nasz licznik.

```python
sun.timer = 60 - sun.points
```

Pełna implementacja funkcji aktualizującej wygląda więc następująco:

```python
def update():
    sun.timer -= 1

    if sun.timer <= 0:
        sun.x = random.randint(80, WIDTH - 80)
        sun.y = random.randint(80, HEIGHT - 80)
        sun.timer = 60 - sun.points
```

### Pełny program

```python
import pgzrun
import random

WIDTH = 800
HEIGHT = 600

sun = Actor("sun")
sun.timer = 0
sun.points = 0


def draw():
    screen.fill("skyblue")
    sun.draw()
    screen.draw.text(str(sun.points), center=(WIDTH / 2, 50), color="red", fontsize=100)


def update():
    sun.timer -= 1

    if sun.timer <= 0:
        sun.x = random.randint(80, WIDTH - 80)
        sun.y = random.randint(80, HEIGHT - 80)
        sun.timer = 60 - sun.points


def on_mouse_down(pos):
    if sun.collidepoint(pos):
        sun.points += 1
        sun.timer = 0
    else:
        sun.points -= 1
        sun.timer = 0


pgzrun.go()
```

### Testujemy działanie

Czas zagrać w naszą grę! Ile punktów Tobie uda się zdobyć?