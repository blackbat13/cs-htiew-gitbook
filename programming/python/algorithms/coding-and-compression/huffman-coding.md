# Kody Huffmana

## Opis problemu

{% content-ref url="../../../../algorithms/coding-and-compression/huffman-coding.md" %}
[huffman-coding.md](../../../../algorithms/coding-and-compression/huffman-coding.md)
{% endcontent-ref %}

## Implementacja

```python

class Node:
    def __init__(self, letter = "", value = 0, left = None, right = None):
        self.letter = letter
        self.value = value
        self.left = left
        self.right = right

def create_tree(text):
    nodes_list = []
    letters_set = set(text)
    nodes_list = [Node(letter, text.count(letter)) for letter in letters_set]
    nodes_list.sort(key=lambda el: el.value)
    while len(nodes_list) > 1:
        first = nodes_list.pop(0)
        second = nodes_list.pop(0)
        new_node = Node("", first.value + second.value, first, second)
        nodes_list.append(new_node)
        nodes_list.sort(key=lambda el: el.value)

    return nodes_list[0]

def create_codes(tree, codes, path):
    if tree.left is None and tree.right is None:
        codes[tree.letter] = path
        return

    if tree.left is not None:
        create_codes(tree.left, codes, path + "0")

    if tree.right is not None:
        create_codes(tree.right, codes, path + "1")

def compress(text, codes):
    compressed = ""
    for letter in text:
        compressed += codes[letter]

    return compressed


text = "papuga"
tree = create_tree(text)
codes = dict()
create_codes(tree, codes, "")

print(codes)

compressed = compress(text, codes)

print(compressed)
```
