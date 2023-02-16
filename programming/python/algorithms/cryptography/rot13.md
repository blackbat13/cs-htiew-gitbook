# Szyfr ROT13

## Opis problemu

{% content-ref url="../../../../algorithms/cryptography/symmetric/rot13.md" %}
[rot13.md](../../../../algorithms/cryptography/symmetric/rot13.md)
{% endcontent-ref %}

## Szyfrowanie

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def encode(message: str) -> str:
    encoded = ""
    letter = 0
    
    for i in range(len(message)):
        letter = ord(message[i]) + 13
        
        if letter > ord("z"):
            letter = ord("a") + letter - ord("z")

        encoded += chr(letter)

    return encoded


message = "computerscience"

encoded = encode(message)

print(f"Encoded: {encoded}")
```
{% endcode %}

## Deszyfrowanie

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def decode(message: str) -> str:
    decoded = ""
    letter = 0
    
    for i in range(len(message)):
        letter = ord(message[i]) - 13
        
        if letter < ord("a"):
            letter = ord("z") - (ord("a") - letter)

        decoded += chr(letter)

    return decoded


message = "pczdihrfgpvrbpr"

decoded = decode(message)

print(f"Decoded: {decoded}")
```
{% endcode %}
