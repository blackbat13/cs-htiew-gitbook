# Wyróżnienie elementu

Opracowano na podstawie: [http://boitblog.blogspot.com/2013/12/reveal-color-of-selected-object-in-image.html](http://boitblog.blogspot.com/2013/12/reveal-color-of-selected-object-in-image.html)

## Wstęp

W celu wyróżnienia danego elementu na zdjęciu, np. do reklamy produktu, możemy skorzystać z prostego efektu.
Zmieniamy zdjęcie na czarno-białe, a tylko wyróżniony element zostawiamy kolorowy.
Efekt ten najlepiej działa z obiektami w żywych i jaskrawych kolorach.

W tutorialu skorzystamy z następującego zdjęcia:

![Źródło: https://cc0.photo/2021/10/06/apple-impaled-on-a-fence-crown/](https://cc0.photo/download/5049/)

## Tworzymy wersję czarno-białą

Najpierw stworzymy wersję naszego zdjęcia w odcieniach szarości.

### 1. Duplikujemy warstwę

Wybieramy menu **Warstwa->Powiel warstwę** lub używamy skrótu **Shift+Ctrl+D**.
Klikamy prawym przyciskiem myszy na nowej warstwie i wybieramy **Modyfikuj atrybuty warstwy...**.
Zmieniamy nazwę naszej warstwy na *Szara* i zatwierdzamy.

### 2. Desaturacja

Zaznaczamy warstwę *Szara* i wybieramy menu **Kolory->Desaturacja->Desaturacja...**.
Jako tryb wybieramy **Jasność (HSL)** i zatwierdzamy.

### 3. Poprawiamy jasność i kontrast

Dostosowujemy jasność i kontrast czarno-białego zdjęcia tak, by wyglądało na bardziej *wyprane* i *wyblakłe*.
W tym celu wybieramy menu **Kolory->Jasność i kontrast...**.
Zwiększamy jasność, np. do $$50$$ i zmniejszamy kontrast, np. do $$-15$$.

## Wyróżniamy element

Mamy już czarno-białe zdjęcie. Teraz pora uwidocznić oryginalny kolor wybranego elementu.
Elementem, który wyróżnimy, będzie jabłko.

### Zaznaczamy element

Korzystając z narzędzi zaznaczania, np. **Odręczne zaznaczanie obszarów**, zaznaczamy element zdjęcia, który chcemy wyróżnić.
Im dokładniej to zrobimy, tym lepszy efekt uzyskamy.

{% hint style="info" %}
Dla ułatwienia pracy możemy tymczasowo ukryć warstwę *Szara* klikając przy niej ikonkę oka.
{% endhint %}

### Zmiękczamy zaznaczenie

Gdy już jesteśmy zadowoleni z naszego zaznaczenia, warto je delikatnie zmiękczyć.
W tym celu wybieramy menu **Zaznaczenie->Zmiękcz...** i ustawiamy np. $$2 px$$.

### Dodajemy kanał alfa

Zanim będziemy mogli wyciąć nasze zaznaczenie i tym samym zrobić *dziurę* w warstwie, musimy najpierw dodać kanał alfa do naszej warstwy.
Zaznaczamy warstwę *Szara* i wybieramy **Warstwa->Przezroczystość->Dodaj kanał alfa**.

### Wycinamy zaznaczenie

Teraz przyszła pora na użycie hipotetycznych nożyczek.
Wybieramy menu **Edycja->Wyczyść** albo używamy przycisku **Delete**.
Następnie czyścimy zaznaczenie (menu **Zaznaczenie->Brak** lub skrót **Shift+Ctrl+A**).

### Poprawiamy kolory

Na koniec warto jeszcze bardziej podkreślić wyróżniony element.
W tym celu wybieramy menu **Kolory->Barwa i nasycenie...** i zmniejszamy jasność, np. na $$-15$$.

## Efekt końcowy

![](../../../.gitbook/assets/color_reveal.png)

