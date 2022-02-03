# Efekt vintage

Opracowano na podstawie [http://www.gimpology.com/submission/view/authentic_vintage_effect](http://www.gimpology.com/submission/view/authentic_vintage_effect).

## Wstęp

Efekt vintage potrafi zmienić klasyczne zdjęcia w zdjęcia w stylu retro.
Efekt ten najlepiej działa na zdjęciach z żywymi kolorami (niebo, trawa, itp.).

W tutorialu skorzystamy z następującego zdjęcia: 

![Źródło: https://cc0.photo/2021/09/22/two-sailboats-on-the-duisburg-six-lake-plateau/](https://cc0.photo/download/4974/)

## Dostosowanie kolorów

Na początek zaczniemy od dostosowania kolorów zdjęcia.
Ponieważ każde zdjęcie jest unikalne, warto poeksperymentować z omówionymi tutaj ustawieniami.
Naszym celem będzie zwiększenie kontrastu, nasycenia i dostosowanie krzywych kolorów.

### 1. Zwiększamy kontrast

Wybieramy menu **Kolory->Jasność i kontrast** i zwiększamy kontrast, np. $$+20$$.

### 2. Zwiększamy nasycenie

Wybieramy menu **Kolory->Barwa i nasycenie**.
Zwiększamy nasycenie, np. $$+20$$.
Warto także dostosować barwę, np. $$-10$$.

### 3. Dostosowujemy krzywe kolorów

Wybieramy menu **Kolory->Krzywe**.
Z menu rozwijanego wybieramy po kolei każdy kanał: czerwony, zielony i niebieski.
Każdą krzywą dostosowujemy indywidualnie.

### 4. Zmniejszamy nasycenie

Ponownie wybieramy menu **Kolory->Barwa i nasycenie**.
Tym razem zmniejszamy nasycenie, np. $$-30$$.
Możemy także delikatnie zwiększyć jasność i zmniejszyć barwę.

## Dodajemy winietę

W grafice komputerowej winieta to efekt, w którym obraz przechodzi stopniowo od środka w czarne tło na krawędziach.
Taki efekt idealnie pasuje do zdjęcia w stylu retro.

### 1. Tworzymy nową warstwę

Najpierw tworzymy nową warstwę z przezroczystością.
W tym celu wybieramy menu **Warstwa->Nowa warstwa**.
Nazwijmy ją *Winieta*.
Jako wypełnienie wybieramy **Przezroczystość**.
Gdy nowa warstwa zostanie już utworzona, ustawiamy jej krycie na $$50%$$.

### 2. Tworzymy zaznaczenie

Mając zaznaczoną nową warstwę tworzymy zaznaczenie w formie elipsy za pomocą narzędzia **Zaznaczenie eliptyczne**.
Nasza elipsa powinna być wpisana w prostokąt zdjęcia.

### 3. Zmiękczamy zaznaczenie

Wybieramy menu **Zaznaczenie->Zmiękcz**.
Ustawiamy zmiękczenie na $$150 px$$.

### 4. Odwracamy zaznaczenie

Wybieramy menu **Zaznaczenie->Odwróć**.

### 5. Wypełniamy czarnym kolorem

Na koniec wypełniamy zaznaczenie czarnym kolorem za pomocą narzędzia **Wypełnienie kubełkiem**.

W ten sposób uzyskujemy efekt winiety.

## Dodajemy różowawy ton

### 1. Tworzymy nową warstwę

Dodajemy kolejną warstwę, tak jak poprzednio.
Nazwijmy ją *Róż*.
Ustawiamy krycie nowej warstwy na $$8%$$.

### 2. Wypełniamy warstwę kolorem

{% hint style="warning" %}
Przed przystąpieniem do tego kroku usuwamy wszystkie aktywne zaznaczenia: menu **Zaznaczenie->Brak**.
{% endhint %}

W celu uzyskania pożądanego efektu używamy narzędzia **Wypełnienie kubełkiem** i wypełniamy nową warstwę żywym kolorem różowym, np **#FF0090**.

## Efekt końcowy

W ten sposób dodaliśmy efekt retro do naszego zdjęcia. 
Zależnie od wybranych ustawień, nasze zdjęcie może teraz wyglądać np. tak:

![](../../../.gitbook/assets/vintage_effect.png)