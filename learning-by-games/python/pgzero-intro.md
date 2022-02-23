# Wstęp do PygameZero

## Wstęp

Poznaliśmy już niezbędne podstawy programowania w języku Python, pora więc przejść do tworzenia bardziej interaktywnych gier dwuwymiarowych. W tym celu wykorzystamy bibliotekę przeznaczoną właśnie do tworzenia takich gier: **PyGameZero**. Nie jest ona częścią domyślnej instalacji języka Python, musimy więc ją samodzielnie zainstalować.

### Czego się nauczysz

* Instalacji bibliotek
* Zasady działania podstawowego szablonu PygameZero
* Podziału kodu na części (funkcje)

## Instalacja biblioteki

Na dole ekranu programu PyCharm szukamy zakładki **Terminal.** Otwieramy ją i w oknie, które się pojawi wpisujemy następujące polecenie:

`pip install pgzero`

Zatwierdzamy je przyciskiem _Enter_ i czekamy aż biblioteka się zainstaluje.

## Szablon

Na samym początku utworzymy bardzo prosty szablon. Będziemy z niego wielokrotnie korzystać przy tworzeniu naszych gier. Tak naprawdę, praktycznie zawsze będziemy od tego właśnie zaczynać.

Tworzymy nowy plik o nazwie `szablon.py`, który zaraz wypełnimy treścią.

### Importujemy bibliotekę

Na początku importujemy zainstalowaną bibliotekę, a dokładnie jej konkretny moduł: _pgzrun_.
Pozwoli on nam uruchamiać tworzone gry.

```python
import pgzrun
```

### Określamy wymiary okna gry

Na początek określamy wymiary okna naszej gry. Zacznijmy klasycznie od wymiarów $$800\times600$$.
W zależności od zapotrzebowania będziemy te wymiary dostosowywać do konkretnych gier.

Wymiary określamy podając szerokość (ang. *width*) i wysokość (ang. *height*) okna gry.
Ważne jest, żeby nazwy zmiennych były w tym wypadku napisane **drukowanymi literami**.

```python
WIDTH = 800
HEIGHT = 600
```

### Tworzymy część rysującą

Jedną z najważniejszych części każdej gry jest część rysująca, w której będziemy określać, co ma zostać wyświetlone na ekranie.
Dopiero zaczynamy i nie mamy jeszcze nic do narysowania, dlatego dodajemy polecenie _pass_, które określa, że mamy *spasować*, czyli nic nie robić.

```python
def draw():
    pass
```

### Tworzymy część aktualizującą

Drugą kluczową częścią każdej gry jest część aktualizująca (ang. *update*).
Podobnie jak wcześniej, nie mamy jeszcze nic do aktualizacji, więc tutaj także dodajemy _pass_.

```python
def update():
    pass
```

### Dodajemy polecenie uruchamiające grę

Na samym końcu naszego kodu dodajemy polecenie, które uruchomi naszą grę.
To polecenie powinno **zawsze** znajdować się **na końcu** kodu.

```python
pgzrun.go()
```

I to wszystko! Teraz możemy przejść do testowania.

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

Teraz czas uruchomić naszą "grę". Postępujemy standardowo: prawy przycisk myszy w edytorze -> _Run 'szablon'_. Naszym oczom powinien ukazać się piękny, czarny ekran o wymiarach $$800$$ na $$600$$ pikseli. Świetnie!

Efekt może nie jest bardzo satysfakcjonujący, ale to oznacza, że biblioteka zainstalowana została poprawnie i możemy przejść do tworzenia naszych gier!

## Pętla gry

Gra działa w nieskończonej, ukrytej pętli. Przez cały czas, od uruchomienia aż do zakończenia gry wykonywane są dwie główne akcje: rysowanie i aktualizacja.
Nazywamy to **pętlą gry**. Co każdą klatkę animacji aktualizowane są pozycje graczy, ich interakcja z graczem i sobą nawzajem, życia przeciwników, punkty itp.
Ogólnie aktualizowany jest **stan gry**. Wszystkie te zmiany są także nanoszone na ekran, czyli rysowane w oknie gry.