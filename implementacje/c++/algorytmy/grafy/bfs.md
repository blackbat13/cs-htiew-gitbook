---
description: Przeszukiwanie grafu wszerz
---

# BFS

## Opis problemu

{% content-ref url="../../../../grafowe/bfs.md" %}
[bfs.md](../../../../grafowe/bfs.md)
{% endcontent-ref %}

## Implementacja

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

/// Incidence list of the graph
vector<vector<int> > graph;

/// True if node was visited, false otherwise
vector<bool> visited;

/// Prepares example graph adding vertices to incidence list
void prepareExampleGraph() {
    graph = vector<vector<int> >(7);
    graph[0].push_back(1);
    graph[0].push_back(6);

    graph[1].push_back(0);
    graph[1].push_back(6);
    graph[1].push_back(3);
    graph[1].push_back(2);

    graph[2].push_back(1);
    graph[2].push_back(3);

    graph[3].push_back(2);
    graph[3].push_back(1);
    graph[3].push_back(6);
    graph[3].push_back(4);
    graph[3].push_back(5);

    graph[4].push_back(3);
    graph[4].push_back(5);

    graph[5].push_back(4);
    graph[5].push_back(3);
    graph[5].push_back(6);

    graph[6].push_back(0);
    graph[6].push_back(1);
    graph[6].push_back(3);
    graph[6].push_back(5);
}

/// Iterative bfs algorithm
/// \param node - starting node to visit
void bfs(int node) {
    queue<int> nodes;

    nodes.push(node);

    while (!nodes.empty()) {
        node = nodes.front();
        nodes.pop();
        if (visited[node]) {
            continue;
        }

        visited[node] = true;
        cout << "Visited node: " << node << endl;

        for (int i = 0; i < graph[node].size(); i++) {
            int next_node = graph[node][i];
            if (!visited[next_node]) {
                nodes.push(next_node);
            }
        }
    }
}

int main() {
    prepareExampleGraph();
    visited = vector<bool>(graph.size(), false);

    bfs(0);

    return 0;
}
```

### Link do implementacji

{% embed url="https://ideone.com/fNxldF" %}
Przeszukiwanie grafu wszerz - BFS
{% endembed %}

### Opis implementacji

Funkcja `prepareExampleGraph` przygotowuje przykładowy graf w formie listy sąsiedztwa zapisanej w dynamicznej tablicy typu `vector`. Przykładowy graf (przedstawiony także na poniższym rysunku) ma 7 wierzchołków (numerowanych od zera) i jest nieskierowany.

Po utworzeniu przykładowego grafu (**linia 72**) przygotowujemy tablicę `visited` i początkowo wypełniamy ją wartościami `false` (**linia 73**). W tej tablicy zapamiętujemy dla każdego wierzchołka, czy został on już odwiedzony, czy jeszcze nie. W tej implementacji korzystamy z dynamicznej tablicy typu `vector`, można jednak równie dobrze wykorzystać statyczną tablicę (jeżeli z góry znamy liczbę wierzchołków grafu).

Funkcja `bfs`  przyjmuje jeden parametr - numer (identyfikator, indeks) początkowego wierzchołka, od którego chcemy zacząć przeszukiwanie. Na początku tworzymy kolejkę `nodes`, w której będziemy przechowywali kolejne wierzchołki do przetworzenia (**linia 48**). Początkowo do kolejki dodajemy tylko pierwszy wierzchołek, przekazany jako parametr funkcji (**linia 50**).

Następnie przetwarzamy kolejne wierzchołki z kolejki, tak długo jak w tej kolejce jest jeszcze coś do przetworzenia (**linia 52**). W pętli pobieramy pierwszy wierzchołek z kolejki (**linia 53**) i usuwamy go z kolejki (**linia 54**). Następnie sprawdzamy, czy został już wcześniej odwiedzony, odwołując się do tablicy `visited` (**linia 55**). Jeżeli wierzchołek został już wcześniej odwiedzony, to nie chcemy go ponownie przetwarzać, więc przechodzimy do kolejnego obrotu pętli (**linia 56**).

Jeżeli wierzchołek nie został jeszcze odwiedzony, to oznaczamy go jako odwiedzony (**linia 59**) i wypisujemy jego numer (**linia 60**). Następnie  przechodzimy przez wszystkich sąsiadów aktualnie przetworzonego wierzchołka (**linia 62**). W pomocniczej zmiennej `next_node` zapamiętujemy numer przetwarzanego sąsiada, pobranego z listy sąsiedztwa (**linia 63**). Następnie sprawdzamy, czy wierzchołek ten był już odwiedzony (**linia 64**), a jeżeli nie, to dodajemy go do kolejki (**linia 65**).

![Przykładowy graf wykorzystany w implementacji](../../../../.gitbook/assets/example_graph.png)

{% embed url="http://graphonline.ru/en/?graph=iyeQZmXVpPfZWqYG" %}
