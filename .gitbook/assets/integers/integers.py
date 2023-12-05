import math


file_name = "integers_test.txt"


def ex1():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    min_val = min(numbers)
    max_val = max(numbers)

    print("Minimum:", min_val, "Pozycja:", numbers.index(min_val) + 1)
    print("Maksimum:", max_val, "Pozycja:", numbers.index(max_val) + 1)


def ex2():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    sum_val = sum(numbers)
    avg_val = sum_val / len(numbers)

    print("Suma:", sum_val)
    print(f"Średnia: {avg_val:.2f}")


def ex3():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    counter = 0

    for num in numbers:
        if num % 2 == 0:
            counter += 1

    print("Parzyste:", counter)


def ex4():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    even = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)

    print("Minimum parzyste:", min(even))
    print("Maksimum parzyste:", max(even))


def ex5():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    counter = 0

    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            counter += 1

    print(counter)


def ex6():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    gcd_list = []

    for i in range(1, len(numbers)):
        gcd_list.append(math.gcd(numbers[i - 1], numbers[i]))

    print("Maksimum NWD:", max(gcd_list))
    print("Minimum NWD:", min(gcd_list))

def ex7():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    current_lcm = 1

    for i in range(1, len(numbers)):
        if numbers[i] < 100:
            current_lcm = (current_lcm * numbers[i]) // math.gcd(current_lcm, numbers[i])

    print("NWW:", current_lcm)


def ex8():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    counter = 0

    for num in numbers:
        is_prime = num > 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
            i += 1
        if is_prime:
            counter += 1

    print(counter)


def ex9():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    numbers_sum = []

    for num in numbers:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10
            num //= 10
        
        numbers_sum.append(digit_sum)

    min_sum = min(numbers_sum)
    max_sum = max(numbers_sum)

    print("Minimalna suma cyfr:", min_sum, "Liczba:", numbers[numbers_sum.index(min_sum)])
    print("Maksymalna suma cyfr:", max_sum, "Liczba:", numbers[numbers_sum.index(max_sum)])


def ex10():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))


    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if math.gcd(numbers[i], numbers[j]) == 1:
                print(numbers[i], numbers[j])


print("Zadanie 1")
ex1()

print("\nZadanie 2:")
ex2()

print("\nZadanie 3:")
ex3()

print("\nZadanie 4:")
ex4()

print("\nZadanie 5:")
ex5()

print("\nZadanie 6:")
ex6()

print("\nZadanie 7:")
ex7()

print("\nZadanie 8:")
ex8()

print("\nZadanie 9:")
ex9()

print("\nZadanie 10:")
ex10()