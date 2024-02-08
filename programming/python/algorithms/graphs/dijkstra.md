---
description: Najkrótsze ścieżki z zadanego wierzchołka
---

# Dijkstra

## Opis problemu

{% content-ref url="../../../../algorithms/graphs/dijkstra.md" %}
[dijkstra.md](../../../../algorithms/graphs/dijkstra.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
from math import inf
from typing import List, Tuple
from queue import Queue


def dijkstra(graph: List[List[Tuple[int, int]]], node: int) -> List[int]:
    q = Queue()
    distances = [inf] * len(graph)
        
    distances[node] = 0

    for (next_node, distance) in graph[node]:
        q.put((node, next_node, distance))

    while not q.empty():
        from_node, node, new_distance = q.get()
        new_distance += distances[from_node]
        
        if new_distance < distances[node]:
            distances[node] = new_distance
            
            for (next_node, distance) in graph[node]:
                q.put((node, next_node, distance))

    return distances


graph = [
    [(1, 5), (6, 5)],
    [(0, 5), (6, 5), (3, 3), (2, 3)],
    [(1, 3), (3, 1)],
    [(2, 1), (1, 3), (6, 3), (4, 5), (5, 4)],
    [(3, 5), (5, 2)],
    [(4, 2), (3, 4), (6, 5)],
    [(0, 5), (1, 5), (3, 3), (5, 5)],
]

distances = dijkstra(graph, 0)

print(distances)
```
{% endcode %}
