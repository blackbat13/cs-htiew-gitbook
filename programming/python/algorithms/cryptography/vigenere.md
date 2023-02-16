# Szyfr Vigenere'a

## Opis problemu

{% content-ref url="../../../../algorithms/cryptography/symmetric/vigenere.md" %}
[vigenere.md](../../../../algorithms/cryptography/symmetric/vigenere.md)
{% endcontent-ref %}

## Szyfrowanie

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def encode(message: str, key: str) -> str:
    encoded = ""
    key_index = 0
    
    for letter in message:            
        k = ord(key[key_index]) - ord('a')
        encoded_letter = ord(letter) + k
        
        if encoded_letter > ord('z'):
            encoded_letter = ord('a') + encoded_letter - ord('z')

        encoded += chr(encoded_letter)
        key_index += 1
        key_index %= len(key)

    return encoded


message = "computerscience"
key = "cat"

encoded = encode(message, key)

print(f"Encoded: {encoded}")
```
{% endcode %}

## Deszyfrowanie

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def decode(message: str, key: str) -> str:
    decoded = ""
    key_index = 0
    
    for letter in message:
        k = ord(key[key_index]) - ord('a')
        decoded_letter = ord(letter) - k
        
        if decoded_letter < ord('a'):
            decoded_letter = ord('z') - (ord('a') - decoded_letter)

        decoded += chr(decoded_letter)
        key_index += 1
        key_index %= len(key)

    return decoded


message = "eogrungrmeixpcx"
key = "cat"

decoded = decode(message, key)

print(f"Decoded: {decoded}")
```
{% endcode %}
