# Sortowanie bąbelkowe

## Opis problemu

{% content-ref url="../../../../algorithms/sorting/bubble-sort.md" %}
[bubble-sort.md](../../../../algorithms/sorting/bubble-sort.md)
{% endcontent-ref %}

## Implementacja

{% code overflow="wrap" lineNumbers="true" %}
```julia
function bubbleSort(array)
    sorted = false
    i = 2
    while !sorted
        sorted = true
        for j = length(array):-1:i
            if array[j] < array[j - 1]
                tmp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tmp
                sorted = false
            end
        end

        i += 1
    end
end


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]

bubbleSort(array)

println(array)
```
{% endcode %}

### Link do implementacji

{% embed url="https://replit.com/@damiankurpiewski/BubbleSort-Julia" %}
Sortowanie bąbelkowe
{% endembed %}