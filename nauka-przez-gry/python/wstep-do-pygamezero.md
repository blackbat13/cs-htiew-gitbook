# Wstęp do PygameZero

## Wstęp

Poznaliśmy już niezbędne podstawy programowania w języku Python, pora więc przejść do tworzenia bardziej interaktywnych gier dwuwymiarowych. W tym celu wykorzystamy bibliotekę przeznaczoną właśnie do tworzenia takich gier: **PyGameZero**. Nie jest ona częścią domyślnej instalacji języka Python, musimy więc ją samodzielnie zainstalować.

### Czego się nauczysz

TODO

## Instalacja biblioteki

Na dole ekranu programu PyCharm szukamy zakładki **Terminal.** Otwieramy ją i w oknie, które się pojawi wpisujemy następujące polecenie:

`pip install pgzero`

Zatwierdzamy je przyciskiem _Enter_ i czekamy aż biblioteka się zainstaluje.

TODO - filmik

## Szablon

Na samym początku utworzymy bardzo prosty szablon. Będziemy z niego wielokrotnie korzystać przy tworzeniu naszych gier. Tak naprawdę, praktycznie zawsze będziemy od tego właśnie zaczynać.

Tworzymy nowy plik o nazwie `szablon.py`, który zaraz wypełnimy treścią.

### Importujemy bibliotekę

TODO

```python
import pgzrun
```

### Określamy wymiary okna gry

TODO

```python
WIDTH = 800
HEIGHT = 600
```

### Tworzymy część rysującą

TODO

```python
def draw():
    pass
```

### Tworzymy część aktualizującą

TODO

```python
def update():
    pass
```

### Dodajemy polecenie uruchamiające grę

TODO

```python
pgzrun.go()
```

### Pełen program z komentarzami

```python
# Korzystamy z biblioteki do tworzenia gier: PyGame Zero
import pgzrun

# Określamy szerokość i wysokość okna gry
WIDTH = 800
HEIGHT = 600


# Tutaj będziemy rysować wszystko na ekranie
def draw():
    pass


# Tutaj będziemy aktualizować stan gry: przyznawać punkty, poruszać postaciami itd.
def update():
    pass


# Uruchamiamy grę
pgzrun.go()
```

### Testujemy działanie

Teraz czas uruchomić naszą "grę". Postępujemy standardowo: prawy przycisk myszy w edytorze -> _Run 'szablon'_. Naszym oczom powinien ukazać się piękny, czarny ekran o wymiarach 800 na 600 pikseli. Świetnie!

Efekt może nie jest bardzo satysfakcjonujący, ale to oznacza, że biblioteka zainstalowana została poprawnie i możemy przejść do tworzenia naszych gier!

TODO - filmik

## Pętla gry

TODO - wyjaśnienie podstawowych mechanik, jak działa draw i update

### Pętla rysująca

TODO

### Pętla aktualizująca

TODO
