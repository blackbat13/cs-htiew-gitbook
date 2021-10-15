# Instrukcje warunkowe

## Prosta instrukcja warunkowa

```python
temperatura = int(input("Podaj temperaturę: "))
if temperatura < 5:
    print("Zimno!")
```

## Rozwinięta instrukcja warunkowa

```python
temperatura = int(input("Podaj temperaturę: "))
if temperatura < 5:
    print("Zimno!")
else:
    print("Cieplej!")
```

## Pełna instrukcja warunkowa

```python
temperatura = int(input("Podaj temperaturę: "))
if temperatura < 5:
    print("Zimno!")
elif temperatura < 20:
    print("Umiarkowanie!")
else:
    print("Ciepło!")
```
