# Gra w monety ze sztuczną inteligencją

## Wstęp

Gra w monety to jedna z gier dla dwóch graczy, której zasady można bardzo szybko i łatwo przyswoić.
Na stole leżą sobie monety, a gracze grają na przemian.
W swojej turze gracz może zabrać ze stołu $$1$$, $$3$$ lub $$4$$ monety (o ile na stole pozostała odpowiednia liczba monet).
Gracz, który zabierze ze stołu ostatnie monety, przegrywa.

Jak widać jest to gra z prostymi zasadami, chociaż nie koniecznie łatwo w nią wygrać.
Dlatego jest to idealna gra do zaprezentowania działania sztucznej inteligencji.

Tak, dzisiaj stworzymy grę, w której naszym przeciwnikiem będzie komputer sterowany przez sztuczną inteligencję!

### Czego się nauczysz

- Tworzenia klas
- Wykorzystania sztucznej inteligencji do wykonywania ruchów

## Biblioteka

W celu stworzenia gracza sterowanego przez sztuczną inteligencję skorzystamy z biblioteki **easyAI**.
Najpierw musimy ją jednak zainstalować.
W **terminalu** wpisujemy poniższe polecenie i zatwierdzamy przyciskiem enter.

```
pip install easyAI
```

## Klasa gry

Na początku nasza gra będzie miała charakter tekstowy.
Dopiero później, gdy podstawy będą już działać, dodamy do niej grafikę.
Zaczynamy więc od stworzenia pliku `gameOfCoins.py` w którym zapiszemy implementację naszej tekstowej gry.

### Importujemy biblioteki

Na początek wystarczy nam jedna biblioteka: **easyAI**.
Ponieważ będziemy korzystać z wielu modułów tej biblioteki, zaimportujemy je wszystkie.

```python
from easyAI import *
```

### Tworzymy klasę gry

Nasza gra będzie opisana w osobnej **klasie**, ponieważ taki jest wymóg biblioteki.
**Klasa** w programowaniu to coś jak schemat, według którego tworzymy różne **obiekty**.
Można sobie wyobrazić, że **klasa** to instrukcja konstrukcji samochodu, a **obiekt** to konkretny samochód.
Możemy mieć wiele samochodów stworzonych według tego samego schematu, ale różniących się np. kolorem lakieru.
Podobnie możemy mieć kilka **obiektów** utworzonych na podstawie tej samej **klasy**.

Naszą klasę nazwiemy **GameOfCoins** i stworzymy w oparciu o klasę **TwoPlayerGame** z biblioteki easyAI.

```python
class GameOfCoins(TwoPlayerGame):
```

### Inicjalizujemy obiekt klasy

Klasa powinna mieć metodę, która pozwoli nam na utworzenie nowego obiektu (**instancji**) klasy.
Taka metoda ma specjalną nazwę: `__init__` (skrót od **initialization** czyli inicjalizacja z angielskiego).
Przy towrzeniu nowej gry powinniśmy do niej przekazać jeden parametr: informację na temat graczy.

```python
class GameOfCoins(TwoPlayerGame):
    def __init__(self, players=None):
```

Wewnątrz funkcji inicjalizującej zapamiętujemy przekazany parametr w tworzonym obiekcie klasy, do którego odnosimy się poprzez słowo kluczowe **self**.

```python
class GameOfCoins(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players
```

Powinniśmy także zdefiniować początkową liczbę monet na stole, np. $$17$$.
Liczbę monet zapamiętamy w zmiennej **pile**.

```python
class GameOfCoins(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players
        self.pile = 17
```

Na końcu potrzebujemy jeszcze iformacji o tym, który z graczy zaczyna jako pierwszy.
Jak to zwykle bywa, zaczyna gracz o numerze jeden.

```python
class GameOfCoins(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players
        self.pile = 17
        self.current_player = 1
```

### Określamy dostępne ruchy

Przygotowaliśmy podwaliny pod naszą grę, teraz czas określić jej reguły.
Zaczniemy od listy dozwolonych ruchów.
W tym celu dopisujemy do naszej klasy metodę **possible_moves**.

```python
class GameOfCoins(TwoPlayerGame):
    ...
    def possible_moves(self):
```

Ruchy powinniśmy zwrócić w formie listy ruchów, a same ruchy powinny mieć format tekstowy (**string**).
W naszej grze mamy trzy możliwe ruchy, tak jak wspomnieliśmy wcześniej.

```python
class GameOfCoins(TwoPlayerGame):
    ...
    def possible_moves(self):
        return ["1", "3", "4"]
```

### Wykonujemy ruch

Wiemy już, jakie ruchy możemy wykonywać w grze.
Co powinno się jednak wydarzyć po wykonaniu ruchu?
Jak powinien się zmienić stan gry?
To musimy zdefiniować za pomocą metody **make_move**, która jako parametr przyjmuje ruch do wykonania.

```python
class GameOfCoins(TwoPlayerGame):
    ...
    def make_move(self, move):
```

Po wykonaniu wybranego ruchu nasza liczba dostępnych monet powinna się zmniejszyć o liczbę zgodną z ruchem.
Odejmujemy więc wartość ruchu od zmiennej **pile**, pamiętając o tym, że najpierw musimy zamienić ruch z tekstu na liczbę całkowitą.

```python
class GameOfCoins(TwoPlayerGame):
    ...
    def make_move(self, move):
        self.pile -= int(move)
```

### Koniec gry

Czas zadecydować, kiedy gra się kończy.
To określamy za pomocą funkcji **is_over**.

```python
class GameOfCoins(TwoPlayerGame):
    ...
    def is_over(self):
```

Nasza gra kończy się, gdy skończą się monety na stole.
Sprawdzamy więc stan pozostałych monet i zwracamy stosowną informację.

```python
class GameOfCoins(TwoPlayerGame):
    ...
    def is_over(self):
        return self.pile <= 0
```

### Wyświetlanie stanu gry

W celu ułatwienia sobie rozgrywki, tak żebyśmy nie musieli wszystkiego pamiętać, warto co każdy ruch wyświetlać stan obecnej gry.
Do tego posłuży nam metoda **show**.

```python
class GameOfCoins(TwoPlayerGame):
    ...
    def show(self):
```

Z perspektywy gracza najważniejsza jest liczba pozostałych na stole monet, taką więc informację wyświetlamy na ekranie.

```python
class GameOfCoins(TwoPlayerGame):
    ...
    def show(self):
        print(f"{self.pile} monet pozostało na stole")
```

### Punktacja AI

Aby sztuczna inteligencja mogła nauczyć się grać w naszą grę, musi wiedzieć, kiedy wygrywa, a kiedy nie.
W tym celu dołożymy do naszej gry punktację, którą zdefiniujemy z pomocą metody **scoring**.

```python
class GameOfCoins(TwoPlayerGame):
    ...
    def scoring(self):
```

Punktacja będzie zależna od tego, ile monet pozostało w grze.
Gdy monety się skończyły, to znaczy, że sztuczna inteligencja wygrała i powinna dostać punkty.
W każdym innym przypadku nie przyznajemy punktów.

```python
class GameOfCoins(TwoPlayerGame):
    ...
    def scoring(self):
        if self.pile <= 0:
            return 100
        else:
            return 0
```

### Pełna klasa gry

Tak powinna wyglądać teraz nasza klasa gry w monety.

```python
class GameOfCoins(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players
        self.pile = 17
        self.current_player = 1

    def possible_moves(self):
        return ["1", "3", "4"]

    def make_move(self, move):
        self.pile -= int(move)

    def is_over(self):
        return self.pile <= 0

    def show(self):
        print(f"{self.pile} monet pozostało na stole")

    def scoring(self):
        if self.pile <= 0:
            return 100
        else:
            return 0
```

### Tworzymy grę i gramy!

Pod naszą klasą, w tzw. **kodzie głównym**, utworzymy następującą instrukcję warunkową:

```python
if __name__ == "__main__":
```

Dzięki zastosowaniu takiej konstrukcji, kod który zaraz napiszemy wykona się tylko, gdy uruchomimy ten konkretny plik gry.
Będzie to przydatne później, gdy będziemy korzystać z właśnie tworzonego pliku ptzy tworzeniu interfejsu graficznego.

W celu utworzenia gry potrzebujemy informacji na temat graczy.
Pierwszy z nich będzie człowiekiem, a drugi będzie sztuczną inteligencją.
Sztuczna inteligencja musi działać według jakiegoś algorytmu, który na początku musimy zdefiniować.

```python
if __name__ == "__main__":
    algorithm = Negamax(13)
```

Skorzystamy z algorytmu **Negamax**. Jako parametr podajemy liczbę kroków naprzód, które sztuczna inteligencja ma "przewidywać".

Teraz tworzymy obiekt naszej gry.
Jako parametr podajemy listę złożoną z dwóch graczy: gracza sterowanego przez człowieka (**Human_Player**) i gracza sterowanego przez sztuczną inteligencję (**AI_Player**).

```python
if __name__ == "__main__":
    algorithm = Negamax(13)
    game = GameOfCoins([Human_Player(), AI_Player(algorithm)])
```

Na koniec pozostało nam uruchomić naszą grę i zagrać!
Czy uda Ci się pokonać sztuczną inteligencję?
Spróbuj różnych parametrów przy definiowaniu algorytmu **Negamax**.
Sprawdź jak wpływa to na przebieg rozgrywki.

```python
if __name__ == "__main__":
    algorithm = Negamax(13)
    game = GameOfCoins([Human_Player(), AI_Player(algorithm)])
    game.play()
```

### Pełna gra

```python
from easyAI import *


class GameOfCoins(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players
        self.pile = 17
        self.current_player = 1

    def possible_moves(self):
        return ["1", "3", "4"]

    def make_move(self, move):
        self.pile -= int(move)

    def is_over(self):
        return self.pile <= 0

    def show(self):
        print(f"{self.pile} monet pozostało na stole")

    def scoring(self):
        if self.pile <= 0:
            return 100
        else:
            return 0


if __name__ == "__main__":
    algorithm = Negamax(13)
    game = GameOfCoins([Human_Player(), AI_Player(algorithm)])
    game.play()
```