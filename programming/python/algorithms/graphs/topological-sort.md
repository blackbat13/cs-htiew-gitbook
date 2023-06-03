# Sortowanie topologiczne

## Opis problemu

{% content-ref url="../../../../algorithms/graphs/topological-sort.md" %}
[topological-sort.md](../../../../algorithms/graphs/topological-sort.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```python
def topological_sort(graph):
  in_ranks = [0] * len(graph)
  removed = [False] * len(graph)
  result = []
    
  for i in range(len(graph)):
    for j in range(len(graph[i])):
        in_ranks[graph[i][j]] += 1

  change = True

  while change and len(result) < len(graph):
    change = False
        
    for i in range(len(graph)):
      if removed[i] or in_ranks[i] > 0:
        continue
      

      change = True
      result.append(i)
      removed[i] = True
            
      for j in range(len(graph[i])):
          in_ranks[graph[i][j]] -= 1

  return result


graph = [
		[2],
		[0, 2],
		[],
		[1, 0, 4],
		[2, 1],
		[0, 4],
]

result = topological_sort(graph)
    
if len(result) < len(graph):
  print("Graph has a cycle")
else:
  for el in result:
    print(el, end=" ")

  print()
```
{% endcode %}
