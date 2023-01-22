# Konwersja w systemie U2

## Opis problemu

{% content-ref url="../../../../algorytmy/numeral-systems/u2.md" %}
[System U2](../../../../algorytmy/numeral-systems/u2.md)
{% endcontent-ref %}

## Z U2 do dziesiętnego

{% code overflow="wrap" lineNumbers="true" %}
```python
def u2_to_decimal(number: str) -> int:
    power = 2 ** (len(number) - 1)
    result = 0
    
    if number[0] == "1":
        result -= power
        
    for index in range(1, len(number)):
        power //= 2
        digit = number[index]
        
        if digit == "1":
            result += power

    return result


number_u2 = "10000001"

number_decimal = u2_to_decimal(number_u2)

print(f"{number_u2} (U2) = {number_decimal} (10)")
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/5KbrSA" %}
Konwersja z systemu U2 do dziesiętnego
{% endembed %}