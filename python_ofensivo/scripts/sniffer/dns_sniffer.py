#!/usr/bin/env python3

import scapy.all as scapy
import signal
import sys
from termcolor import colored

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo de DNS Sniffer...\n", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def process_packet(packet):
    
    if packet.haslayer(scapy.DNSRR):
        qname = packet[scapy.DNSQR].qname
        qname = qname.decode("utf-8")
        exclude_keyword = ["cloud", "bing", "static", "traffic", "api"]
        if not any(keyword in qname for keyword in exclude_keyword) and qname not in domains_seen:
            domains_seen.add(qname)
            print(colored(f"[+] Request: {qname}", "green"))

def sniff(interface):
    scapy.sniff(iface=interface, filter="udp and port 53", store=False, prn=process_packet)

def main():
    print(colored("[*] DNS Sniffer started. Waiting for DNS requests...", "yellow"))
    sniff("wlp4s0")

if __name__ == "__main__":
    global domains_seen
    domains_seen = set()
    main()

