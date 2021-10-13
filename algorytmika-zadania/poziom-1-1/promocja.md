# Promocja

## Opis

W Topolandii żyje sobie farmer imieniem Włodzimir. Włodzimir zajmuje się sprzedażą mleka, pozyskanego ze swoich dorodnych krów pasących się na bujnych łąkach Topolandii. Ostatnio postanowił zastosować specjalną promocję: za $$3$$ puste butelki po mleku możesz dostać $$1$$ pełną butelkę mleka gratis! Ile butelek mleka możesz wypić korzystając z tej promocji, jeżeli masz już zakupionych $$n$$ butelek mleka?

PS. Pan Włodzimir z chęcią pożyczy Ci puste butelki, jeżeli je potem oddasz.

Źródło: [https://onlinejudge.org/external/111/11150.pdf](https://onlinejudge.org/external/111/11150.pdf)

### Specyfikacja

#### Dane

* $$n$$ - liczba zakupionych butelek mleka z przedziału$$[1,200]$$

#### Wynik

* Maksymalna liczba butelek mleka , które można wypić, korzystając z promocji. 

### Przykład

#### Dane

```
n := 8
```

#### Wynik

```
12
```

{% hint style="info" %}
#### Wyjaśnienie

Na początku mamy $$8$$ pełnych butelek mleka. Jeżeli pożyczymy jedną pustą butelkę, to możemy nasze $$9$$ pustych butelek wymienić na $$3$$ nowe. Wypijamy $$3$$ butelki mleka i wymieniamy je na jedną butelkę mleka. Wypijamy i ją, a na końcu oddajemy pustą butelkę. Wypiliśmy więc najpierw $$8$$ , potem $$3$$ i na końcu $$1$$ butelkę mleka:

$$8+3+1=12$$ 
{% endhint %}
