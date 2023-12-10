# Liczby Fibonacciego

## Opis problemu

{% content-ref url="../../../../algorithms/integers/fibonacci-numbers.md" %}
[fibonacci-numbers.md](../../../../algorithms/integers/fibonacci-numbers.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```haskell
fib 1 = 1
fib 2 = 1
fib n = fib (n-1) + fib (n-2)

main = do
    print $ fib 10
```
{% endcode %}

## Opis

Funkcja `fib` przyjmuje jeden argument: numer `n` w ciągu Fibonacciego, dla którego ma zostać obliczona wartość.

1. **Warunki bazowe:** funkcja definiuje wartości dla pierwszego (1) i drugiego (2) elementu ciągu jako 1. To niezbędne warunki bazowe dla rekurencji.
2. **Rekurencyjne wywołanie:** dla każdej wartości `n` większej niż 2, funkcja oblicza wartość wywołując się rekurencyjnie dwa razy: `fib (n-1)` i `fib (n-2)`, a następnie sumując otrzymane wyniki. To właśnie tworzy ciąg Fibonacciego.

W głównym programie (`main`) wywołujemy funkcję `fib` dla konkretnej wartości `n`, w tym przypadku 10. Wynik, czyli dziesiąty element ciągu Fibonacciego, jest następnie wyświetlany.
