# BFS

BFS (*Breadth First Search*) to algorytm przeszukiwania grafu, który przeszukuje wierzchołki w kolejności ich odległości od źródła, odwiedzając najpierw wierzchołki bezpośrednio sąsiadujące ze źródłem, następnie wierzchołki, które są dwa kroki od źródła, i tak dalej.

## Opis działania algorytmu

BFS zaczyna od wybranego wierzchołka (zwanego wierzchołkiem źródłowym/początkowym) i odwiedza wszystkie wierzchołki na tym samym poziomie (czyli w tej samej odległości od wierzchołka źródłowego) przed przejściem do następnego poziomu. W praktyce oznacza to, że algorytm BFS "rozszerza" się na wszystkie kierunki jednocześnie, co jest użyteczne w takich zastosowaniach jak znajdowanie najkrótszej ścieżki w grafie nieważonym.

## Zastosowania

BFS ma wiele zastosowań w praktyce, między innymi:

- Wyszukiwanie elementu w grafie.
- Wyszukiwanie najkrótszej ścieżki w grafie nieważonym.
- Sprawdzanie, czy graf jest spójny.
- Wyszukiwanie cykli w grafie.
- Rozwiązywanie problemów takich jak problem labiryntu, problem ścieżki Hamiltona itp.

## Złożoność obliczeniowa

Złożoność czasowa algorytmu BFS wynosi $$O(V + E)$$, gdzie $$V$$ to liczba wierzchołków, a $$E$$ to liczba krawędzi, ponieważ każdy wierzchołek i każda krawędź są przeszukiwane dokładnie raz.

## Implementacja

Algorytm BFS jest zwykle implementowany za pomocą struktury danych zwaną **kolejką**, która zachowuje wierzchołki do odwiedzenia. Początkowo, wierzchołek startowy jest dodawany do kolejki. Następnie, dopóki kolejka nie jest pusta, wierzchołek jest usuwany z kolejki, a wszystkie jego niewizytowane sąsiednie wierzchołki są dodawane do kolejki. Operacje są powtarzane, aż kolejka zostanie opróżniona.

Poniżej znajdziesz przykładowe implementacje w wybranych językach.

### C++

{% content-ref url="../../programming/c++/algorithms/graphs/bfs.md" %}
[bfs.md](../../programming/c++/algorithms/graphs/bfs.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/graphs/bfs.md" %}
[bfs.md](../../programming/python/algorithms/graphs/bfs.md)
{% endcontent-ref %}
