# C++ - rozwiązanie

{% code overflow="wrap" lineNumbers="true" %}
```cpp
#include <cstdio>
#include <iostream>
#include <set>
#include <map>

using namespace std;

int main()
{
    int n;
    string str;
    map<string, int> counters;
    set<string> countries;

    scanf("%d", &n);

    for (int i = 0; i < n; ++i)
    {
        cin >> str;
        counters[str]++;
        countries.insert(str);
        getline(cin, str);
    }

    for (auto &el : countries)
    {
        printf("%s %d\n", el.c_str(), counters[el]);
    }

    return 0;
}
```
{% endcode %}
