# Spójne składowe

## Opis problemu

{% content-ref url="../../../../algorithms/graphs/connected-components.md" %}
[connected-components.md](../../../../algorithms/graphs/connected-components.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
from typing import List


def dfs(graph: List[List[int]], visited: List[bool], node: int):
    if visited[node]:
        return

    visited[node] = True

    for new_node in graph[node]:
        if not visited[new_node]:
            dfs(graph, visited, new_node)


def count_connected_components(graph: List[List[int]]) -> int:
    result = 0
    visited = [False for _ in range(len(graph))]
    
    for i in range(len(graph)):
        if not visited[i]:
            result += 1
            dfs(graph, visited, i)

    return result;
    

graph = [
	[1, 6],
	[0, 6, 3, 2],
	[1, 3],
	[2, 1, 6, 4, 5],
	[3, 5],
	[4, 3, 6],
	[0, 1, 3, 5],
]

result = count_connected_components(graph)

print("Number of connected components in the graph:", result)
```
{% endcode %}

### Link do implementacji

{% embed url="https://ideone.com/68F4l6" %}
Spójne składowe
{% endembed %}
