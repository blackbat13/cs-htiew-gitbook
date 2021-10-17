# Wyszukiwanie binarne

## Opis problemu

{% content-ref url="../../../../algorytmy/wyszukiwanie/wyszukiwanie-binarne.md" %}
[wyszukiwanie-binarne.md](../../../../algorytmy/wyszukiwanie/wyszukiwanie-binarne.md)
{% endcontent-ref %}

## Wersja iteracyjna

### Implementacja

```kotlin
fun binarySearch(array: List<Int>, number: Int): Int {
  var left = 0
  var right = array.count() - 1

  while (left < right) {
    val middle = (left + right) / 2

    if (number < array[middle]) {
      right = middle
    } else if (number > array[middle]) {
      left = middle + 1
    } else {
      return middle
    }
  }

  if (left < array.count() && array[left] == number) {
    return left
  }

  return -1
}

fun main() {
  val array = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  val number = 8

  val index = binarySearch(array, number)

  if (index == -1) {
    println("Szukanej liczby nie ma na liscie")
  } else {
    println("Szukana liczba znajduje sie pod indeksem $index")
  }
}
```

### Link do implementacji

{% embed url="https://ideone.com/n8oV0L" %}
Wyszukiwanie binarne - wersja iteracyjna
{% endembed %}

### Opis implementacji

TODO

## Wersja rekurencyjna

### Implementacja

```kotlin
fun binarySearch(array: List<Int>, number: Int, left: Int, right: Int): Int {
  if(left == right && array[left] == number) {
    return left
  }
  else if (left >= right) {
    return -1
  }

  val middle = (left + right) / 2

  if (number < array[middle]) {
    return binarySearch(array, number, left, middle)
  } else if (number > array[middle]) {
    return binarySearch(array, number, middle + 1, right)
  } else {
    return middle
  }
}

fun main() {
  val array = listOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  val number = 8

  val index = binarySearch(array, number, 0, array.count())

  if (index == -1) {
    println("Szukanej liczby nie ma na liscie")
  } else {
    println("Szukana liczba znajduje sie pod indeksem $index")
  }
}
```

### Link do implementacji

{% embed url="https://ideone.com/F0QMN2" %}
Wyszukiwanie binarne - wersja rekurencyjna
{% endembed %}

### Opis implementacji

TODO
