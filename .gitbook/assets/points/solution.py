def exercise1():
    tab = [[0] * width for _ in range(height)]
    with open(file_name) as file:
        for line in file:
            row, col = map(int, line.split())
            tab[row - 1][col - 1] += 1

    count = 0
    for row in range(height):
        for col in range(width):
            if tab[row][col] > 0:
                count += 1
    
    print(count)


def exercise2():
    tab = [[0] * width for _ in range(height)]
    with open(file_name) as file:
        for line in file:
            row, col = map(int, line.split())
            tab[row - 1][col - 1] += 1

    row_sums = [0] * height
    col_sums = [0] * width
    for row in range(height):
        for col in range(width):
            row_sums[row] += tab[row][col]
            col_sums[col] += tab[row][col]

    count_rows = 0
    count_cols = 0

    for el in row_sums:
        if el > 1:
            count_rows += 1

    for el in col_sums:
        if el > 1:
            count_cols += 1

    print("Wiersze:", count_rows)
    print("Kolumny:", count_cols)


def exercise3():
    tab = [[0] * width for _ in range(height)]
    with open(file_name) as file:
        for line in file:
            row, col = map(int, line.split())
            tab[row - 1][col - 1] += 1

    count = 0
    for row in range(height):
        for col in range(width):
            if tab[row][col] > 1:
                count += 1
    
    print(count)


def exercise4():
    tab = [[0] * width for _ in range(height)]
    with open(file_name) as file:
        for line in file:
            row, col = map(int, line.split())
            tab[row - 1][col - 1] += 1

    max_val = max(max(row) for row in tab)

    print("Wartość:", max_val)
    print("Współrzędne:")

    for row in range(height):
        for col in range(width):
            if tab[row][col] == max_val:
                print(row + 1, col + 1)


def exercise5():
    tab = [[0] * width for _ in range(height)]
    with open(file_name) as file:
        for line in file:
            row, col = map(int, line.split())
            tab[row - 1][col - 1] += 1

    count = 0
    for row in range(height):
        for col in range(width):
            current_count  = 0
            for change in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + change[0], col + change[1]
                if 0<=new_row<height and 0<=new_col<width and tab[new_row][new_col] > 1:
                    current_count += 1
                    break

            if current_count == 0:
                count += 1

    print(count)


def exercise6():
    tab = [[0] * width for _ in range(height)]
    with open(file_name) as file:
        for line in file:
            row, col = map(int, line.split())
            tab[row - 1][col - 1] += 1

    counters = [0] * (max(max(row) for row in tab) + 1)
    for row in range(height):
        for col in range(width):
            counters[tab[row][col]] += 1
    
    for i in range(len(counters)):
        print(f"Wartość {i}: {counters[i]}")


file_name = "points_test.txt"
width = 10
height = 10

for i in range(1, 7):
    print(f"Zadanie {i}:")
    exec(f"exercise{i}()")
    print()
