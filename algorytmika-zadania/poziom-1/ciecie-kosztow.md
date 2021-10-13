# Cięcie kosztów

## Opis

Pewna firma postanowiła przeprowadzić redukcję zatrudnienia. Celem jest cięcie kosztów. Pracownicy pracują w zespołach trzyosobowych. W ramach jednego zespołu zarobki pracowników mogą się różnić. Zarząd postanowił, że z każdego takiego zespołu zostaną zwolnione dwie osoby o skrajnych zarobkach, tzn.: osoba zarabiająca najwięcej i osoba zarabiająca najmniej. Kto przetrwa redukcję i pozostanie zatrudniony?

Źródło: [https://onlinejudge.org/external/117/11727.pdf](https://onlinejudge.org/external/117/11727.pdf)

### Specyfikacja

#### Dane

* $$a,b,c$$ - trzy liczby naturalne określające zarobki pracowników, wszystkie w zakresie $$[1000, 10000]$$

#### Wynik

* Zarobki pracownika, który pozostanie zatrudniony

### Przykład

#### Dane

```
a := 1500
b := 1200
c := 1800
```

**Wynik: **$$1500$$

{% hint style="info" %}
#### Wyjaśnienie

Najmniejsza z wartości to $$1200$$, a największa do $$1800$$, pozostaje więc $$1500$$.
{% endhint %}
