# Algorytmy liniowe (Linear algorithms)

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

{% tab title="EN" %}
## Introduction

What is an **Algorithm**? Instruction, recipe, flow chart... An algorithm describes the solution of a certain problem. We distinguish various types of algorithms, and we will start with their simplest type - linear algorithms.

## Linear algorithm

A linear algorithm is a serial instruction in which we follow step by step, line by line, operation by operation. 

A number of questions arise in the construction of the algorithm. How detailed should the algorithm be? What operations must we include in it and what can we omit? What operations are available? What kind of description should we use? These are only some of the important points to consider. 

Let's take a look at the example below.

### Example 1

Imagine that you have to prepare a jam sandwich. This is our **problem**. For this problem, we will propose an example solution in the form of an **algorithm**.

```
1. Take a slice of bread
2. Take the butter 
3. Take the jam 
4. Take the knife 
5. Brush the bread with butter 
6. Brush the bread with jam
```

As you can see, the example above is an **algorithm** for making a jam sandwich. However, let's consider its correctness and accuracy. Are all required operations included? Can any of the already present ones be omitted? Maybe we should also add instructions on how to unscrew the jar? Or maybe open the fridge to get the jam and close it afterwards. Or maybe we should also consider the situation when there is no jam and you need to go to the store. Or maybe it's Sunday and the shops are closed. Or maybe, maybe... We can think like this endlessly and we have to stop somewhere.

## Problem specification

First of all, we begin with the **specification**. The specification defines what input the algorithm takes and what should be its output. In other words, it is a formal problem statement. Let's go back to our example.

### Example 2

Let's start by formalizing our problem of making a jam sandwich with the help of the specification.

#### Specification

**Input**:

* A slice of bread
* A butter
* A jam

**Output**:

* A jam sandwich

Now we can move on to the algorithm. As you can see, we have three inputs: a slice of bread, butter, and jam. Then we don't have to worry about preparing these things. Usually in the algorithm notation we will skip reading the data, which means that in this case we will omit the instructions for taking bread, butter and jam. We simply assume, according to the specification, that they are given to us in advance and available to our algorithm.

#### Algorytm

```
1. Take the knife
2. Brush the bread with butter 
3. Brush the bread with jam
```

And in this case, we limited ourselves to a certain set of operations and to a certain level of detail. As we will move to more advanced IT algorithms, it will become clearer what operations we can perform and what not.
{% endtab %}
{% endtabs %}
