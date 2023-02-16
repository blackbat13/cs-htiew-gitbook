# Szyfr płotkowy

## Opis problemu

{% content-ref url="../../../../algorithms/cryptography/symmetric/rail-fence.md" %}
[rail-fence.md](../../../../algorithms/cryptography/symmetric/rail-fence.md)
{% endcontent-ref %}

## Szyfrowanie

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def encode(message: str, key: int) -> str:
    encoded = ""

    for k in range(key):
        if k == key - 1:
            jump = (key - 1) * 2
        else:
            jump = (key - (k + 1)) * 2
            
        i = k
        
        while i < len(message):
            encoded += message[i]
            i += jump

    return encoded


message = "computer science"

encoded = encode(message, 3)

print(f"Encoded: {encoded}")
```
{% endcode %}

## Deszyfrowanie

### Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def decode(message: str, key: int) -> str:
    decoded = list(message)
    j = 0

    for k in range(key):
        if k == key - 1:
            jump = (key - 1) * 2
        else:
            jump = (key - (k + 1)) * 2
            
        i = k
        
        while i < len(message):
            decoded[i] = message[j]
            j += 1
            i += jump

    return "".join(decoded)


message = "cu eoptrsinemecc"

decoded = decode(message, 3)

print(f"Decoded: {decoded}")
```
{% endcode %}
