# Palindrom

## Opis problemu

{% content-ref url="../../../../algorytmy/tekstowe/palindrom.md" %}
[palindrom.md](../../../../algorytmy/tekstowe/palindrom.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def is_palindrome(a: str) -> bool:
    return a == a[::-1]


a = "kajak"

if is_palindrome(a):
    print(f'{a} jest palindromem')
else:
    print(f'{a} nie jest palindromem')
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/nsapMq" %}
Test palindromu
{% endembed %}
