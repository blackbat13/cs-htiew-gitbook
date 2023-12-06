import math
import statistics
import collections


file_name = "integers.txt"


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

    print(counter)


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
        if numbers[i] < 20:
            current_lcm = (current_lcm * numbers[i]) // math.gcd(current_lcm, numbers[i])

    print("NWW:", current_lcm)


def is_prime(num):
    """
    Funkcja zwraca True, jeśli num jest liczbą pierwszą, w przeciwnym wypadku zwraca False
    """
    if num <= 1:
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        
        i += 1

    return True


def ex8():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    counter = 0

    for num in numbers:
        if is_prime(num):
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

    min_pair = (0,0)
    max_pair = (0,0)
    min_sum = 500
    max_sum = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if math.gcd(numbers[i], numbers[j]) == 1:
                sum_pair = numbers[i] + numbers[j]
                if sum_pair < min_sum:
                    min_pair = (numbers[i], numbers[j])
                    min_sum = sum_pair
                elif sum_pair > max_sum:
                    max_pair = (numbers[i], numbers[j])
                    max_sum = sum_pair
    
    print("Para o największej sumie:", max_pair)
    print("Para o najmniejszej sumie:", min_pair)


def ex11():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))


    for num in numbers:
        factors_sum = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                factors_sum += i
                if num // i != i:
                    factors_sum += num // i
            i += 1

        if factors_sum == num:
            print(num)


def ex12():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    print(statistics.median(numbers))


def ex13():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    counters = collections.Counter(sorted(numbers))
    most_common = counters.most_common(1)[0]
    print("Najpopularniejsza liczba:", most_common[0])
    print("Liczba wystąpień:", most_common[1])


def ex14():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    counter = 0

    for num in numbers:
        is_power_of_two = True
        while num > 1:
            if num % 2 != 0:
                is_power_of_two = False
                break

            num //= 2

        if is_power_of_two:
            counter += 1

    print(counter)


def ex15():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    more_zeros = 0
    more_ones = 0
    zeros_eq_ones = 0

    for num in numbers:
        binary = str(bin(num))[2:]
        zero_count = binary.count("0")
        one_count = binary.count("1")
        if zero_count > one_count:
            more_zeros += 1
        elif zero_count < one_count:
            more_ones += 1
        else:
            zeros_eq_ones += 1

    print("Więcej zer:", more_zeros)
    print("Mniej zer:", more_ones)
    print("Tyle samo:", zeros_eq_ones)


def ex16():
    with open(file_name) as file:
        numbers = list(map(int, file.read().split()))

    counter = 0

    for num in numbers:
        i = 2
        while num % i != 0:
            i += 1

        if is_prime(num // i):
            counter += 1

    print(counter)
        

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

print("\nZadanie 11:")
ex11()

print("\nZadanie 12:")
ex12()

print("\nZadanie 13:")
ex13()

print("\nZadanie 14:")
ex14()

print("\nZadanie 15:")
ex15()

print("\nZadanie 16:")
ex16()