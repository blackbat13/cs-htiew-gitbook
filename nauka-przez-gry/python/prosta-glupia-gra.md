---
description: '"This game is silly!"'
---

# Prosta (naiwna) gra

## Wstęp

Na początku pisałem, że tworzenie aplikacji konsolowym jest nudne. Od czegoś jednak trzeba zacząć! Zanim wskoczymy do świata gier dwuwymiarowych, stworzymy naszą pierwszą grę "tekstową". Nauczymy się w ten sposób zupełnych podstaw programowania, takich jak interakcja z użytkownikiem (graczem), tworzenie zmiennych, modyfikowanie ich i wypisywanie komunikatów na ekranie.

### Czego się nauczysz

* Tworzenia zmiennych i prostych operacji na nich
* Komunikacji z użytkownikiem

## Gra

Jak wskazuje tytuł, nasza gra będzie prosta, a nawet można powiedzieć, że naiwna! Będzie to gra dla dwóch graczy: człowiek kontra komputer.  Przebieg gry jest prosty: najpierw pierwszy gracz podaje swoją liczbę, a następnie drugi podaje swoją. Celem jest podanie liczby większej od przeciwnika. Wygrywa ten, kto poda większą wartość!

#### Przykład

* **Gracz**: 14
* **Komputer**: 15, wygrałem!

Prosta gra, prawda? Jest jednak pewien problem. Jeżeli zaczynamy jako pierwsi, to nie mamy szansy wygrać! Wystarczy, że przeciwnik poda wartość o jeden większą od naszej i w ten sposób wygrywa. Dlatego na wstępie wspomniałem, że ta gra jest nie tylko prosta, ale wręcz naiwna!

Jest to jednak idealna gra na początek. Przejdźmy więc do działania!

### Tworzymy nowy projekt

{% embed url="https://youtu.be/WxS5iz4bNxM" %}

### Tworzymy nowy plik

TODO - filmik

### Wczytujemy liczbę od gracza

Zaczynamy od wczytania liczby od użytkownika. W tym celu skorzystamy z polecenia `input`. Jako **parametr** tego polecenia, który zapisujemy w nawiasach okrągłych, podajemy komunikat, który ma zostać wyświetlony na ekranie.  W Pythonie komunikaty i teksty podajemy w cudzysłowie:

```python
input("Podaj liczbę: ")
```

Nie wystarczy jednak tylko wywołać odpowiednie polecenie. Musimy jeszcze gdzieś **zapisać** jego wynik, a konkretnie w nowej **zmiennej**, którą nazwiemy `liczba_tekst`:

```python
liczba_tekst = input("Podaj liczbę: ")
```

Gdy używamy polecenia `input`, to wartość wpisana przez użytkownika będzie zawsze wczytana jako **tekst**. My jednak potrzebujemy liczbę. W tym celu skorzystamy z kolejnego polecenia: `int`. Posłuży nam ono do zamiany tekstu na liczbę. Jako parametr tego polecenia podajemy tekst do zamiany na liczbę, w naszym przypadku ten tekst zapisany jest w zmiennej `liczba_tekst`:

```python
int(liczba_tekst)
```

Oczywiście wynik polecenia musimy gdzieś zapisać. Zapamiętamy go w nowej zmiennej o nazwie `liczba`:

```python
liczba = int(liczba_tekst)
```

Jak dotąd mamy w naszym programie dwa polecenia: wczytanie wartości od użytkownika i zamianę jej na liczbę.

```python
liczba_tekst = input("Podaj liczbę: ")
liczba = int(liczba_tekst)
```

Już teraz warto uruchomić program i sprawdzić, czy wszystko działa.

{% hint style="warning" %}
Pamiętaj, żeby testować swoje programy jak najczęściej! Pozwoli to na bieżąco rozwiązywać wszelkie błędy i uniknąć późniejszej frustracji.
{% endhint %}

### Tworzymy nową, większą liczbę

Przejdźmy teraz do roli komputera. Jego zadaniem jest wypisanie liczby o jeden większej od tej, którą podał użytkownik. W tym celu utworzymy nową liczbę, o jeden większą od tej wczytanej od użytkownika. Tworzymy nową zmienną `nowa_liczba` i przypisujemy do niej wynik dodania liczby $$1$$ do wartości wczytanej od użytkownika zapisanej w zmiennej `liczba`:

```python
nowa_liczba = liczba + 1
```

### Wypisujemy nową liczbę

Teraz pozostało nam wypisać nowo utworzoną liczbę, a następnie komunikat o wygranej. W tym celu skorzystamy z polecenia `print`, które jako parametr przyjmuje zmienną, lub komunikat do wypisania. Zaczniemy od wypisania naszej nowej liczby:

```python
print(nowa_liczba)
```

Nie oczekujemy, że polecenie `print` zwróci nam jakąś wartość, jego zadaniem jest tylko wypisanie komunikatu na ekranie. 

### Wypisujemy komunikat o wygranej

Na koniec wypiszemy jeszcze komunikat _Wygrałem_. Pamiętamy, że komunikaty i teksty podajemy w cudzysłowie.

```python
print("Wygrałem!")
```

Składamy wszystko w całość i mamy gotową grę!

### Gotowa gra z komentarzami

```python
# Wczytujemy od użytkownika wartość w formie tekstu
liczba_tekst = input("Podaj liczbę: ")

# Zamieniamy wczytaną wcześniej wartość na liczbę całkowitą
liczba = int(liczba_tekst)

# Tworzymy nową liczbę większą o 1 od tej, którą podał użytkownik
nowa_liczba = liczba + 1

# Wypisujemy nową liczbę w konsoli
print(nowa_liczba)

# A następnie wypisujemy informację o wygranej komputera
print("Wygrałem!")
```

### Uruchamiamy grę

{% embed url="https://replit.com/@damiankurpiewski/NaiwnaGra" %}

TODO - filmik

## Zadania dodatkowe

TODO



