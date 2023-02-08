# Sortowanie bąbelkowe

## Opis problemu

{% content-ref url="../../../../algorithms/sorting/bubble-sort.md" %}
[bubble-sort.md](../../../../algorithms/sorting/bubble-sort.md)
{% endcontent-ref %}

## Implementacja

```kotlin
fun bubbleSort(array: MutableList<Int>) {
	var sorted = false
	var i = 1
    while (!sorted) {
    	sorted = true
        for(j in array.count() - 1 downTo i) {
            if(array[j] < array[j - 1]) {
                val tmp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = tmp
                sorted = false
            }
        }
        
        i++
    }
}

fun main() {
    val array = mutableListOf(7, 3, 0, 1, 5, 2, 5, 19, 10, 5)

    bubbleSort(array)

    println(array)
}
```

### Link do implementacji

{% embed url="https://ideone.com/1hHW2V" %}
Sortowanie bąbelkowe
{% endembed %}