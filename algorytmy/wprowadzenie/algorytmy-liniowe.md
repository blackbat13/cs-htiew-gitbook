# Algorytmy liniowe

{% tabs %}
{% tab title="PL" %}
## Wstęp

Czym jest algorytm? Instrukcja, przepis, schemat postępowania... Algorytm opisuje rozwiązanie pewnego problemu. Wyróżniamy różnego rodzaju algorytmy, a zaczniemy od ich najprostszego rodzaju - algorytmów liniowych.

## Algorytm liniowy

Algorytm liniowy to szeregowa instrukcja, w której podążamy krok po kroku, linijka po linijce, operacja po operacji.

Przy konstrukcji  algorytmu pojawia się szereg pytań. Jak bardzo szczegółowy powinien być algorytm? Jakie operacje musimy w nim zawrzeć, a jakie możemy pominąć? Jakie operacje są dostępne? Jakiego sposobu opisu powinniśmy używać? To tylko część z ważnych kwestii, które należy rozważyć. 

Przyjrzyjmy się poniższemu przykładowi.

### Przykład 1

Wyobraźmy sobie, że mamy przygotować kanapkę z dżemem. To jest nasz problem. Dla tego problemu, zaproponujemy przykładowe rozwiązanie w postaci **algorytmu**.

```
1. Weź kromkę chleba
2. Weź masło
3. Weź dżem
4. Weź nóż
5. Posmaruj chleb masłem
6. Posmaruj chleb dżemem
```

Jak widać, powyższy przykład jest algorytmem przygotowania kanapki z dżemem. Zastanówmy się jednak nad jego poprawnością i dokładnością. Czy wszystkie wymagane operacje są zawarte? Czy może któreś z już obecnych można pominąć? Może powinniśmy także dodać instrukcję odkręcenia słoika? A może także otwarcia lodówki, żeby wyciągnąć dżem i zamknięcia jej potem. A może powinniśmy także rozważyć sytuację, gdy nie ma dżemu i trzeba pójść do sklepu. A może jest niedziela i sklepy są zamknięte. A może,  a może... Takie rozważania możemy snuć w nieskończoność i trzeba gdzieś się zatrzymać.

## Specyfikacja problemu

Przede wszystkim zaczynamy od **specyfikacji**. Specyfikacja określa, jakie dane wejściowe przyjmuje algorytm i co powinno być jego wynikiem. Innymi słowy, jest to formalne określenie problemu. Wróćmy do naszego przykładu.

### Przykład 2

Zacznijmy od sformalizowania naszego problemu przygotowania kanapki z dżemem za pomocą specyfikacji.

#### Specyfikacja

**Dane**:

* Kromka chleba
* Masło
* Dżem

**Wynik**:

* Kanapka z dżemem

Teraz możemy przejść do algorytmu. Jak widać, mamy trzy dane wejściowe: kromkę chleba, masło oraz dżem. W takim razie o przygotowanie tych rzeczy nie musimy się martwić. Zazwyczaj w zapisie algorytmu będziemy pomijać wczytywanie danych, co oznacza, że w tym przypadku pomijamy instrukcje opisujące wzięcie chleba, masła i dżemu. Po prostu zakładamy, zgodnie ze specyfikacją, że są one nam z góry dane i dostępne dla naszego algorytmu.

#### Algorytm

```
1. Weź nóż
2. Posmaruj chleb masłem
3. Posmaruj chleb dżemem
```

I w tym przypadku ograniczyliśmy się do pewnego zbioru operacji i do pewnego poziomu szczegółowości. Gdy przejdziemy do bardziej informatycznych algorytmów stanie się bardziej jasne, jakie operacje możemy wykonywać, a jakie nie. 
{% endtab %}
{% endtabs %}
