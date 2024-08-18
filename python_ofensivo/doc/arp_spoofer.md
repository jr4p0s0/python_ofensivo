# ARP Spoofer con Scapy

## Introducción

En este laboratorio vamos a aprender a realizar un ataque de ARP Spoofing utilizando Scapy.

El ARP Spoofing es un ataque que consiste en enviar mensajes ARP falsos a una red local, con el objetivo de asociar la dirección MAC de un dispositivo con la dirección IP de otro dispositivo. De esta forma, el atacante puede interceptar y modificar el tráfico de red entre dos dispositivos.

Debemos definir una política de IPtables para aceptar el reenvio de tráfico de red.

```bash
iptables --policy FORWARD ACCEPT
```

**MUY IMPORTANTE**: Este ataque necesita que la MAC esté bien configurada, podemos hacer uso del script `macchanger.py` para cambiar la MAC de la interfaz de red. **NO OLVIDAR VOLVER A LA MAC ORIGINAL AL FINALIZAR EL LABORATORIO**.
**TAMBIEN SON IMPORTANTES LAS POLITICAS DE IPTABLES**.

**MUY IMPORTANTE 2**: EL ARCHIVO */proc/sys/net/ipv4/ip_forward* DEBE TENER EL VALOR 1 PARA QUE EL REENVIO DE PAQUETES FUNCIONE.

