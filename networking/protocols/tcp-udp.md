# TCP i UDP

Protokoły UPD i TCP są używane do przesyłania danych - lub pakietów informacji - przez Internet w oparciu o protokół IP.

### TCP

**Transmission Control Protocol**. Protokół połączeniowy. Gdy maszyna A wysyła dane do maszyny B, maszyna B jest powiadamiana o nadejściu danych, a następnie przesyła potwierdzenie odbioru.

**Przykładowe zastosowania**: e-mail, przeglądanie sieci.

### UDP

**User Datagram Protocol**. Protokół bezpołączeniowy. Mówiąc najprościej, gdy maszyna A wysyła pakiety do komputera B, strumień jest niekierunkowy. Oznacza to, że transmisja danych odbywa się bez ostrzeżenia odbiorcy (maszyny B), a odbiorca otrzymuje dane bez konieczności potwierdzania tego nadawcy danych (maszynie A).

**Przykładowe zastosowania**: wideo-rozmowy, strumieniowanie muzyki.

## TCP vs UDP

|            **TCP**            |             **UDP**            |
| :---------------------------: | :----------------------------: |
|          Połączeniowy         |         Bezpołączeniowy        |
|        Strumień bajtów        |       Strumień wiadomości      |
|            Unicast            |  Unicast, Multicast, Broadcast |
|  Kontrola przepływu i błędów  |          Brak kontroli         |
| Pakiet nazywany **segmentem** | Pakiet nazywany **datagramem** |

![Źródło: https://i.redd.it/duv11av99nm11.png](../.gitbook/assets/tcp_udp_meme.png)

## Schematy routingu

Wiadomości w sieci mogą być rozsyłane na wiele sposobów. Poniżej omówione są najważniejsze z nich.

### Unicast

Komunikacja typu jeden-do-jeden. Z jednego miejsca w sieci do innego, tzn. jeden nadawca i jeden odbiorca. Można to porównać do prywatnej rozmowy dwóch osób.

![Public Domain, https://commons.wikimedia.org/w/index.php?curid=909335](../.gitbook/assets/Unicast.svg)

### Multicast

Komunikacja grupowa typu jeden-do-wielu-z-wielu. Wiadomość jest wysyłana do grupy urządzeń w sieci jednocześnie. Można to przyrównać do rozmowy z grupą znajomych.

![Public Domain, https://commons.wikimedia.org/w/index.php?curid=909339](../.gitbook/assets/Multicast.svg)

### Broadcast

Komunikacja typu jeden-do-wszystkich. Wiadomość wysyłana jest do wszystkich urządzeń w sieci. Można to porównać do stanięcia na środku placu i wykrzykiwania swojej wiadomości.

![Public Domain, https://commons.wikimedia.org/w/index.php?curid=909337](../.gitbook/assets/Broadcast.svg)
