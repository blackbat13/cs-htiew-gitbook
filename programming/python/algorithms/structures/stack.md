# Stos

## Opis problemu

{% content-ref url="../../../../algorithms/structures/stack.md" %}
[stack.md](../../../../algorithms/structures/stack.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
class Stack:
    def __init__(self):
        self._value = None
        self._next = None
        
    def push(self, value):
        if self._value is None:
            self._value = value
            return
        
        new_el = Stack()
        new_el._value = self._value
        new_el._next = self._next
        self._next = new_el
        self._value = value
        
    def top(self):
        return self._value
    
    def pop(self):
        if self._next is None:
            self._value = None
            return
        
        self._value = self._next._value
        self._next = self._next._next
    
    def empty(self) -> bool:
        return self._value is None
    
    def clear(self):
        self._value = None
        
        if self._next is not None:
            self._next.clear()
            self._next = None
        
        
if __name__ == "__main__":
    stack = Stack()
    
    for el in [5, 8, 3, 1, 9]:
        stack.push(el)
        
    while not stack.empty():
        print(stack.top())
        stack.pop()
```
{% endcode %}
