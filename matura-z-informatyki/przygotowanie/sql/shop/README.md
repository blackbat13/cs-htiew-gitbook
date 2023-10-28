# Sklep

Rozważmy następującą bazę danych:

```mermaid
erDiagram
    Zamowienia }o--|| Artykuly : ""
    Zamowienia }o--|| Klienci : ""
    Artykuly {
        INTEGER id_art PK
        TEXT nazwa
        REAL cena
    }
    Klienci {
        INTEGER id_kl PK
        TEXT imie
        TEXT nazwisko
        TEXT miasto
        TEXT ulica
        TEXT kod_pocztowy
    }
    Zamowienia {
        INTEGER id_zam PK
        INTEGER id_art FK
        INTEGER id_kl FK
        INTEGER ilosc_egz
        DATE data_zam
    }
```

Tabela *Zamowienia* zawiera historię wszystkich złożonych zamówień na artykuły.

Podaj instrukcje SQL realizujące poniższe zadania.

## Zadanie 1

Wyświetlenie imienia i nazwiska każdego klienta, który 18 marca 2016 roku dokonał co najmniej jednego zakupu.

## Zadanie 2

Wyświetlenie danych wszystkich zamówień, które zostały dokonane w maju 2015 roku.

## Zadanie 3

Wyświetlenie dla każdego klienta całkowitego kosztu jego zamówień.

## Zadanie 4

Wyświetlenie imienia i nazwiska każdego klienta, który dokonał zamówienia przed 2010 rokiem.

## Zadanie 5

Wyświetlenie danych każdego klienta, którego imię kończy się na literę ‘a’.

## Zadanie 6

Wyświetlenie danych wszystkich klientów, posortowanych rosnąco po nazwisku.

## Zadanie 7

Wyświetlenie dla każdego artykułu jego nazwy i ilości osób, które kupiły dany artykuł.

## Zadanie 8

Wyświetlenie nazwy miasta, id i nazwy każdego artykułu, którego ilość sprzedanych sztuk klientom z tego miasta przekroczyła $$100$$.

## Zadanie 9

Wyświetlenia dla każdego artykułu ilość jego sprzedanych egzemplarzy.

## Zadanie 10

Wypisanie wszystkich artykułów zaczynających się od słowa „komputer” wraz z ceną zwiększoną o $$10\%$$.

## Zadanie 11

Wyliczenie ilości artykułów, których nikt nie zamówił.

## Zadanie 12

Wylistowanie nazwiska każdego klienta, który zamówił co najmniej jeden artykuł o *id_art* równym $$10$$ oraz dokładnie $$2$$ artykuły o *id_art* równym $$20$$.
