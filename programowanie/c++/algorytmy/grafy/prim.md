# Prim

## Opis problemu

{% content-ref url="../../../../algorytmy/grafowe/prim.md" %}
[prim.md](../../../../algorytmy/grafowe/prim.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

struct edge {
    int from;
    int to;
    int distance;

    edge(int from, int to, int distance) {
        this->from = from;
        this->to = to;
        this->distance = distance;
    }

    bool operator<(const edge &rhs) const {
        return distance > rhs.distance;
    }
};

void prim(vector<vector<edge> > &graph, vector<edge> &minSpanningTree, int node) {
    priority_queue<edge> edges;
    
    vector<bool> visited = vector<bool>(graph.size());
    visited[node] = true;
    
    minSpanningTree = vector<edge>();

    for (int i = 0; i < graph[node].size(); i++) {
        edges.push(graph[node][i]);
    }

    while (!edges.empty()) {
        edge current = edges.top();
        edges.pop();

        if (visited[current.to]) {
            continue;
        }

        visited[current.to] = true;
        minSpanningTree.push_back(current);

        for (int i = 0; i < graph[current.to].size(); i++) {
            edge next = graph[current.to][i];
            if (!visited[next.to]) {
                edges.push(next);
            }
        }
    }
}

int main() {
	vector<vector<edge> > graph = {
		{edge(0, 1, 5), edge(0, 6, 5)}, 
		{edge(1, 0, 5), edge(1, 6, 5), edge(1, 3, 3), edge(1, 2, 3)},
		{edge(2, 1, 3), edge(2, 3, 1)},
		{edge(3, 2, 1), edge(3, 1, 3), edge(3, 6, 3), edge(3, 4, 5), edge(3, 5, 4)},
		{edge(4, 3, 5), edge(4, 5, 2)},
		{edge(5, 4, 2), edge(5, 3, 4), edge(5, 6, 5)},
		{edge(6, 0, 5), edge(6, 1, 5), edge(6, 3, 3), edge(6, 5, 5)},
	};
	
	vector<edge> minSpanningTree;
    
    prim(graph, minSpanningTree, 0);

    for(edge current : minSpanningTree) {
        cout << current.from << " <-(" << current.distance << ")-> " << current.to << endl;
    }

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/PR4Noz" %}
Algorytm Prima
{% endembed %}

### Opis implementacji

Na pocz??tku definiujemy struktur?? `edge` do reprezentacji kraw??dzi grafu (**linia 8**). Poniewa?? mamy do czynienia z grafem wa??onym, w strukturze przechowujemy trzy warto??ci: 

* wierzcho??ek pocz??tkowy kraw??dzi - zmienna `from` (**linia 9**),
* wierzcho??ek docelowy kraw??dzi - zmienna `to` (**linia 10**),
* waga/d??ugo???? kraw??dzi - zmienna `distance` (**linia 11**)

Dla u??atwienia definiujemy tak??e konstruktor dla naszej struktury (**linia 13**). Poniewa?? kraw??dzie chcemy przechowywa?? w kolejce priorytetowej, musimy tak??e zdefiniowa?? `operator<` do por??wnywania kraw??dzi (**linia 19**). Warto tutaj zwr??ci?? uwag?? na to, ??e kolejka priorytetowa z stl jest typu max, co oznacza, ??e domy??lnie zwraca??aby nam kraw??d?? o najwi??kszej wadze. Poniewa?? do algorytmu Prima potrzebujemy pobiera?? kraw??dzie o najmniejszej wadze najpierw, odwracamy porz??dek kraw??dzi podczas por??wnywania ich wagi (**linia 20**).

![Przyk??adowy graf wykorzystany w implementacji](../../../../.gitbook/assets/example_graph_weighted.png)

{% embed url="http://graphonline.ru/en/?graph=DZlFqSBPNgdHwNXK" %}
