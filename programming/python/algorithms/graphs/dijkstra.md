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
import math
from typing import List, Tuple


def dijkstra(graph: List[List[Tuple[int, int]]], node: int) -> List[int]:
    queue: List[(int, int, int)] = []
    distances = [math.inf] * len(graph)
        
    distances[node] = 0

    for (next_node, distance) in graph[node]:
        queue.append((node, next_node, distance))

    while len(queue) > 0:
        from_node, node, new_distance = queue[0]
        new_distance += distances[from_node]
        queue.pop(0)
        
        if new_distance < distances[node]:
            distances[node] = new_distance
            
            for (next_node, distance) in graph[node]:
                queue.append((node, next_node, distance))

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
