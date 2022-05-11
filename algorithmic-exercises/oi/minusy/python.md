# Python

# Uwaga

Chociaż rozwiązanie jest stosunkowo proste, to Python jest niestety zbyt wolny do tego zadania, dlatego w niektórych testach zostanie przekroczony limit czasu.

## Implementacja

```python
plus = False
result = ""
n = int(input())

for i in range(n - 1):
    sign = input()

    if sign == "-" and plus:
        result += ")"
        plus = False
    elif sign == "+" and not plus:
        result += "("
        plus = True

    result += "-"

if plus:
    result += ")"

print(result)
```