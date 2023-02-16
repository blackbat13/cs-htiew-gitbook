# Szyfr Trithemius"a

## Opis problemu

{% content-ref url="../../../../algorithms/cryptography/symmetric/trithemius.md" %}
[trithemius.md](../../../../algorithms/cryptography/symmetric/trithemius.md)
{% endcontent-ref %}

## Szyfrowanie

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def encode(message: str) -> bool:
    encoded = ""
    k = 0
    letter = 0
    
    for i in range(len(message)):
        letter = ord(message[i]) + k
        
        if letter > ord("z"):
            letter = ord("a") + letter - ord("z")

        encoded += chr(letter)
        k += 1
        k %= 26

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
    k = 0
    letter = 0
    
    for i in range(len(message)):   
        letter = ord(message[i]) - k
        
        if letter < ord("a"):
            letter = ord("z") - (ord("a") - letter)

        decoded += chr(letter)
        k += 1
        k %= 26

    return decoded


message = "cposyykyblspzps"

decoded = decode(message)

print(f"Decoded: {decoded}")
```
{% endcode %}
