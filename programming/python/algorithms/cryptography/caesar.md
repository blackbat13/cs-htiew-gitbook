# Szyfr Cezara

## Opis problemu

{% content-ref url="../../../../algorithms/cryptography/symmetric/caesar.md" %}
[caesar.md](../../../../algorithms/cryptography/symmetric/caesar.md)
{% endcontent-ref %}

## Szyfrowanie

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def encode(message: str, key: int) -> str:
    encoded = ""
    letter = 0
    for i in range(len(message)):
        letter = ord(message[i]) + key
        if letter > ord("z"):
            letter = ord("a") + letter - ord("z")

        encoded += chr(letter)

    return encoded


message = "computerscience"
encoded = encode(message, 3)
print(f"Encoded: {encoded}")
```
{% endcode %}

## Deszyfrowanie

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def decode(message: str, key: int) -> str:
    decoded = ""
    letter = 0
    for i in range(len(message)):
        letter = ord(message[i]) - key
        if letter < ord("a"):
            letter = ord("z") - (ord("a") - letter)

        decoded += chr(letter)

    return decoded


message = "frpsxwhuvflhqfh"
decoded = decode(message, 3)
print(f"Decoded: {decoded}")
```
{% endcode %}
