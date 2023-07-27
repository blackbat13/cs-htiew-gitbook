# Rozwiązania

## Zadanie 1

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def zadanie1():
    path = "input/kik.txt"
    with open(path, "r") as file:
        punkty = [list(map(float, str.split(" "))) for str in file.read().split("\n")]
        inside = 0
        outside = 0
        for punkt in punkty:
            x = punkt[0]
            y = punkt[1]
            dist = x * x + y * y
            if dist <= 1:
                inside += 1
            else:
                outside += 1

        print(f"inside: {inside}, outside: {outside}")
```
{% endcode %}

### Wynik

```
W kole: 8136
Poza kołem: 1864
```

## Zadanie 2

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def zadanie2():
    path = "input/kik.txt"
    with open(path, "r") as file:
        punkty = [list(map(float, str.split(" "))) for str in file.read().split("\n")]

        max_length = 0
        current_length = 0
        for punkt in punkty:
            x = punkt[0]
            y = punkt[1]
            dist = x * x + y * y
            if dist <= 1:
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
            else:
                current_length = 0

        print()
        print(f"{max_length}")
```
{% endcode %}

### Wynik

```
Długość sekwencji: 43
```

## Zadanie 3

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def zadanie3():
    path = "input/kik.txt"
    with open(path, "r") as file:
        punkty = [list(map(float, str.split(" "))) for str in file.read().split("\n")]
        xs = [punkt[0] for punkt in punkty]
        xs.sort()
        print()
        print(((xs[len(xs) // 2] - xs[len(xs) // 2 - 1]) / 2) + xs[len(xs) // 2 - 1])
```
{% endcode %}

### Wynik

```
k: -0.0028421983934499573
```

## Zadanie 4

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def zadanie4():
    path = "input/kik.txt"
    with open(path, "r") as file:
        punkty = [list(map(float, str.split(" "))) for str in file.read().split("\n")]
        punkty = punkty[:100]
        punkty = [[int(punkt[0] * 1000), int(punkt[1] * 1000)] for punkt in punkty]
        for i in range(len(punkty)):
            for j in range(1, len(punkty) - i):
                x1 = punkty[j][0]
                y1 = punkty[j][1]
                x2 = punkty[j - 1][0]
                y2 = punkty[j - 1][1]
                if x1 < x2 or (x1 == x2 and y1 < y2):
                    punkty[j - 1][0], punkty[j][0] = punkty[j][0], punkty[j - 1][0]
                    punkty[j - 1][1], punkty[j][1] = punkty[j][1], punkty[j - 1][1]

        with open("kik_posortowane.txt", "w") as out_file:
            for punkt in punkty:
                print(f"{punkt[0]} {punkt[1]}", file=out_file)
```
{% endcode %}

### Wynik

```
-900 -803
-864 -724
-859 199
-855 903
-854 879
-822 850
-775 -474
-774 869
-726 496
-707 -99
-677 600
-660 780
-639 -832
-633 -375
-599 -329
-594 718
-570 670
-560 365
-551 987
-542 469
-489 -282
-487 -362
-470 -442
-440 0
-439 449
-416 -328
-406 438
-400 100
-396 -563
-389 -75
-372 875
-364 371
-325 619
-322 -321
-320 820
-300 -825
-284 -22
-265 250
-238 -290
-235 -896
-201 -900
-195 -254
-140 -249
-140 -69
-137 100
-131 -811
-114 243
-100 -612
-93 -440
-69 309
-52 -770
-26 -861
-6 -176
115 -199
119 678
126 145
197 -5
300 152
300 495
303 -812
310 234
329 673
351 260
354 896
355 290
359 -673
369 776
379 300
380 -468
381 -572
400 -282
400 348
409 -301
432 868
435 -21
446 776
453 -477
500 669
513 800
514 815
526 315
566 241
579 -214
586 -687
589 364
600 713
629 -579
657 990
661 -415
737 -483
799 199
800 691
800 819
800 921
830 794
878 167
920 -345
924 373
925 -465
927 -510
```
