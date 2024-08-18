# DNS Spoofer con Scapy y Netfilterqueue

## Introducción

En este laboratorio vamos a aprender a realizar un ataque de DNS Spoofing utilizando Scapy y Netfilterqueue.

Lo primero, debemos definir una politica de IPtables para aceptar el trafico de red y redirigirlo a la cola de Netfilterqueue.

```bash
iptables -I INPUT -j NFQUEUE --queue-num 0
```

```bash
iptables -I OUTPUT -j NFQUEUE --queue-num 0
```

```bash
iptables -I FORWARD -j NFQUEUE --queue-num 0
```

```bash
iptables --policy FORWARD ACCEPT
```
