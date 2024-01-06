def exercise1():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    count = 0
    for name in names_list:
        if name[-1] == "a":
            count += 1

    print(count)


def exercise2():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    count = 0
    for name in names_list:
        for i in range(1, len(name) - 1):
            if name[i] == "e":
                count += 1
                break

    print(count)


def exercise3():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    names_lengths = [len(name) for name in names_list]
    min_length = min(names_lengths)
    max_length = max(names_lengths)

    min_names = [name for name in names_list if len(name) == min_length]
    max_names = [name for name in names_list if len(name) == max_length]

    print("Najkrótsze imiona:")
    print("Długość:", min_length)
    print("Imiona:", ", ".join(min_names))
    print()
    print("Najdłuższe imiona:")
    print("Długość:", max_length)
    print("Imiona:", ", ".join(max_names))


def count_vowels(text):
    vowels = "aeiouy"
    count = 0
    for character in text:
        if character in vowels:
            count += 1

    return count


def exercise4():
    names_list = []
    with open(file_name) as file:
        names_list = file.read().split()

    vowels_counters = [count_vowels(name) for name in names_list]
    max_vowels = max(vowels_counters)
    max_vowels_names = [
        names_list[i]
        for i in range(len(names_list))
        if vowels_counters[i] == max_vowels
    ]

    print("\n".join(sorted(max_vowels_names)))


file_name = "names.txt"

for i in range(1, 5):
    print(f"Zadanie {i}:")
    exec(f"exercise{i}()")
    print()
