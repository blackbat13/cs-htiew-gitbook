# Wampiry

Pan Józef von Stąd jest znanym badaczem wampirów. Od wielu lat prowadzi zapiski dotyczące tych niezwykłych stworzeń, które zebrał i zapisał w kilku plikach tekstowych. Zebrane informacje dotyczą:

- Klanów (Klany.txt)
  - numer identyfikacyjny klanu;
  - nazwa klanu;
  - data założenia klanu;
  - kraj, w którym klan został założony.
- Wampirów (Wampiry.txt)
  - numer identyfikacyjny wampira;
  - imię wampira;
  - data urodzenia wampira;
  - data przemiany w wampira;
  - kraj pochodzenia wampira;
  - numer identyfikacyjny klanu, do którego wampir przynależy.
- Ofiar (Ofiary.txt)
  - numer identyfikacyjny ofiary;
  - imię ofiary;
  - data urodzenia;
  - data zgonu.
- Ataków (Ataki.txt)
  - numer identyfikacyjny ataku;
  - numer identyfikacyjny wampira, który dokonał ataku;
  - numer identyfikacyjny ofiary ataku;
  - data ataku;
  - lokalizacja ataku, jedna z trzech wartości:
    - "Wampir" - atak miał miejsce w kraju pochodzenia wampira;
    - "Klan" - atak miał miejsce w kraju założenia klanu;
    - "Zagranica" - atak miał miejsce w innym kraju, niezwiązanym z wampirem ani klanem (takie miejsca nie interesują Pana Józefa).

Wszystkie dane oddzielone są średnikami, a pierwszy wiersz każdego pliku zawiera nagłówki kolumn. Daty podane są w formacie "DD.MM.RRRR". Pomóż Panu Józefowi przeprowadzić analizę zebranych danych i odpowiedzieć na poniższe pytania.

## Dane

{% file src="../../../../.gitbook/assets/Klany.txt" %}
Klany.txt
{% endfile %}

{% file src="../../../../.gitbook/assets/Wampiry.txt" %}
Wampiry.txt
{% endfile %}

{% file src="../../../../.gitbook/assets/Ofiary.txt" %}
Ofiary.txt
{% endfile %}

{% file src="../../../../.gitbook/assets/Ataki.txt" %}
Ataki.txt
{% endfile %}

## Zadanie 1

Wypisz, w kolejności alfabetycznej, **imiona** wszystkich wampirów pochodzących z Rumunii.

## Zadanie 2

Utwórz zestawienie zawierające imię wampira oraz liczbę dokonanych przez niego ataków. Wyniki posortuj rosnąco po liczbie ataków.

## Zadanie 3

Utwórz zestawienie zawierające imię wampira, datę przemiany oraz datę pierwszego ataku. Wyniki posortuj rosnąco po czasie, jaki upłynął od przemiany do pierwszego ataku. Wypisz tylko te wampiry, które dokonały co najmniej jednego ataku.

## Zadanie 4

Wypisz imiona wszystkich wampirów, które nie dokonały żadnego ataku. Wynik posortuj alfabetycznie po imionach.

## Zadanie 5

Wypisz imię wampira, który musiał najdłużej czekać na przemianę od swoich urodzin. Jeżeli jest kilku takich wampirów, wypisz wszystkich.

## Zadanie 6

Utwórz zestawienie zawierające imię ofiary, datę ataku, imię wampira, który dokonał ataku, oraz nazwę klanu, do którego należy wampir.

## Zadanie 7

Utwórz zestawienie zawierające imię ofiary oraz liczbę ataków, które zostały na nią przeprowadzone. Posortuj alfabetycznie po imionach.

## Zadanie 8

Wypisz imiona wszystkich ofiar, które zginęły bezpośrednio w wyniku ataku, tzn. data jednego z ataków przeprowadzonego na daną ofiarę jest równa jej dacie zgonu. Posortuj alfabetycznie po imionach.

## Zadanie 9

Utwórz zestawienie zawierające nazwę kraju, liczbę wampirów pochodzących z tego kraju, liczbę klanów założonych w tym klanie, oraz liczbę ataków przeprowadzonych w tym kraju. Posortuj alfabetycznie po nazwie kraju.

## Zadanie 10

Wypisz nazwy wszystkich klanów, które nie posiadają członków. Posortuj alfabetycznie po nazwach.

## Zadanie 11

Utwórz zestawienie zawierające imię wampira oraz zaokrąglone w górę: liczbę dni, liczbę miesięcy i liczbę lat, które upłynęły od urodzin do przemiany. Wyniki posortuj alfabetycznie po imionach.

## Zadanie 12

Utwórz zestawienie zawierające imię wampira, jego datę urodzenia, datę przemiany oraz wiek wampira w momencie przemiany. Wyniki posortuj alfabetycznie po imionach.

## Zadanie 13

Utwórz zestawienie zawierające imię ofiary oraz liczbę dni, które upłynęły od pierwszego do ostatniego ataku.
