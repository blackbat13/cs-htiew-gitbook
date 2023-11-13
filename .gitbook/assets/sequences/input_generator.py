from random import randint, random

with open("sequences.txt", "w") as file:
    for i in range(100):
        lst = [randint(1, 100) for _ in range(10)]
        rnd = random()
        if rnd < 0.3:
            lst.sort()
        elif rnd < 0.5:
            lst.sort(reverse=True)
        print(" ".join(map(str, lst)), file=file)

with open("sequences_test.txt", "w") as file:
    for i in range(10):
        lst = [randint(1, 100) for _ in range(10)]
        rnd = random()
        if rnd < 0.3:
            lst.sort()
        elif rnd < 0.5:
            lst.sort(reverse=True)
        print(" ".join(map(str, lst)), file=file)