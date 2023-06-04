# Drzewo przedziałowe

## Opis problemu

{% content-ref url="../../../../algorithms/structures/segment-trees.md" %}
[segment-trees.md](../../../../algorithms/structures/segment-trees.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```cpp
#include <cstdio>
#include <iostream>
using namespace std;

class SumSegmentTree {
  struct node {
    int value, from, to, lazy;
    node *left, *right;

    node(int from, int to) {
      this->from = from;
      this->to = to;
      this->value = 0;
      this->lazy = 0;
      this->left = nullptr;
      this->right = nullptr;
    }

    void print(string tabulation = "") {
      printf("%s[%d, %d]: (val: %d, lazy: %d)\n", tabulation.c_str(),
             this->from, this->to, this->value, this->lazy);
      if (this->from != this->to) {
        this->left->print(tabulation + "\t");
        this->right->print(tabulation + "\t");
      }
    }

    void change(int from, int to, int value) {
      if (this->from == from && this->to == to) {
        this->lazy += value;
        return;
      }

      int middle = (this->from + this->to) / 2;

      this->value += this->lazy * (this->to - this->from + 1);
      this->left->lazy += this->lazy;
      this->right->lazy += this->lazy;
      this->lazy = 0;

      this->value += value * (to - from + 1);

      if (from <= middle) {
        if (to <= middle) {
          this->left->change(from, to, value);
        } else {
          this->left->change(from, middle, value);
          this->right->change(middle + 1, to, value);
        }
      } else {
        this->right->change(from, to, value);
      }
    }

    int getValue(int from, int to) {
      if (this->from == from && this->to == to) {
        return this->value + this->lazy * (this->to - this->from + 1);
      }

      int middle = (this->from + this->to) / 2;

      this->value += this->lazy * (this->to - this->from + 1);
      this->left->lazy += this->lazy;
      this->right->lazy += this->lazy;
      this->lazy = 0;

      if (from <= middle) {
        if (to <= middle) {
          return this->left->getValue(from, to);
        } else {
          return this->left->getValue(from, middle) +
                 this->right->getValue(middle + 1, to);
        }
      } else {
        return this->right->getValue(from, to);
      }
    }
  };

  node *root;

  node *build(int from, int to, int tab[]) {
    node *current = new node(from, to);
    if (from == to) {
      current->value = tab[from];
      return current;
    }

    current->left = build(from, (from + to) / 2, tab);
    current->right = build(((from + to) / 2) + 1, to, tab);
    current->value = current->left->value + current->right->value;
    return current;
  }

public:
  SumSegmentTree(int length, int tab[]) {
    this->root = build(0, length - 1, tab);
  }

  void print() { this->root->print(); }

  void change(int from, int to, int value) {
    this->root->change(from, to, value);
  }

  int getValue(int from, int to) { return this->root->getValue(from, to); }
};

int main() {
  int tab[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

  SumSegmentTree sumSegmentTree = SumSegmentTree(10, tab);

  sumSegmentTree.print();

  printf("\n\n[3, 5] = %d\n", sumSegmentTree.getValue(3, 5));

  sumSegmentTree.change(3, 5, 2);

  printf("\n\n[3, 5] + 2\n");

  sumSegmentTree.print();

  printf("\n\n[3, 5] = %d\n", sumSegmentTree.getValue(3, 5));

  return 0;
}
```
{% endcode %}
