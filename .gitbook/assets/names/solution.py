def exercise1():
    names_list = []
    with open("names_test.txt") as file:
        names_list = file.read().split()

    count = 0
    for name in names_list:
        if name[-1] == "a":
            count += 1

    return count

def exercise2():
    names_list = []
    with open("names_test.txt") as file:
        names_list = file.read().split()

    count = 0
    for name in names_list:
        for i in range(1, len(name) - 1):
            if name[i] == "e":
                count += 1
                break
            
    return count

def exercise3():
    numbers_list = []
    with open("duplicates.txt") as file:
        numbers_list = list(map(int, file.read().splitlines()))

    numbers_dict = dict()
    for num in numbers_list:
        if num in numbers_dict:
            numbers_dict[num] += 1
        else:
            numbers_dict[num] = 1

    min_count = min(numbers_dict.values())
    min_num = 101

    for num in numbers_dict:
        if numbers_dict[num] == min_count and num < min_num:
            min_num = num

    return min_num

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += 1
        
    return True

def exercise4():
    numbers_list = []
    with open("duplicates.txt") as file:
        numbers_list = list(map(int, file.read().splitlines()))

    count = 0
    for num in numbers_list:
        if is_prime(num):
            count += 1

    return count
    

print("Exercise 1:", exercise1())
print("Exercise 2:", exercise2())
# print("Exercise 3:", exercise3())
# print("Exercise 4:", exercise4())