#!/usr/bin/env python3

import scapy.all as scapy


def process_packet(packet):
    if packet.haslayer(scapy.DNSRR):
        qname = packet[scapy.DNSQR].qname
        print(qname)


scapy.sniff(iface="wlp4s0", filter="udp and port 53", store=False, prn=process_packet)