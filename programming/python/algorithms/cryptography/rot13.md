# Szyfr ROT13

## Opis problemu

{% content-ref url="../../../../algorithms/cryptography/symmetric/rot13.md" %}
[rot13.md](../../../../algorithms/cryptography/symmetric/rot13.md)
{% endcontent-ref %}

## Szyfrowanie

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def is_letter(letter: str) -> bool:
    return ord('a') <= ord(letter) <= ord('z')


def encode(message: str) -> str:
    encoded = ""
    letter = 0
    
    for i in range(len(message)):
        if not is_letter(message[i]):
            encoded += message[i]
            continue
            
        letter = ord(message[i]) + 13
        
        if letter > ord('z'):
            letter = ord('a') + letter - ord('z')

        encoded += chr(letter)

    return encoded


message = "computer science"

encoded = encode(message)

print(f"Encoded: {encoded}")
```
{% endcode %}

## Deszyfrowanie

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def is_letter(letter: str) -> bool:
    return ord('a') <= ord(letter) <= ord('z')


def decode(message: str) -> str:
    decoded = ""
    letter = 0
    
    for i in range(len(message)):
        if not is_letter(message[i]):
            decoded += message[i]
            continue
            
        letter = ord(message[i]) - 13
        
        if letter < ord('a'):
            letter = ord('z') - (ord('a') - letter)

        decoded += chr(letter)

    return decoded


message = "pczdihrf gpvrbpr"

decoded = decode(message)

print(f"Decoded: {decoded}")
```
{% endcode %}
