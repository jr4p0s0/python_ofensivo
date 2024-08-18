#!/usr/bin/env python3

import scapy.all as scapy
import argparse
from termcolor import colored
import sys
import signal
import subprocess


def def_handler(sig, frame):
    print(colored("\n\n [!] Exiting program...\n", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Ctrl+C handler

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP scanner")
    parser.add_argument("-t", "--target", dest="target", required=True, help="Target IP address/addresses to scan (Ex: -t 192.168.1.1 or -t 192.168.1.0/24)")
    options = parser.parse_args()
    
    return options.target

def scan_ips(target):
    arp_request = scapy.ARP(pdst=target)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    arp_request_broadcast = broadcast/arp_request # Appending the ARP request to the broadcast MAC address
    
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=10, verbose=False) # Send the packet and receive the response
    ips = []
    macs = []
    if answered:
        print(colored("\n [+] Found devices in the network, getting info...", "green"))
        for element in answered:
            ips.append(element[1].psrc)
            macs.append(element[1].hwsrc)
        nmap_scan(ips)
        

def nmap_scan(ips):
    # from nmap take the list of ips and scan them, just get the lines that contain the MAC address
    # and print them
    ips_str = " ".join(ips) # Convert the list of IPs to a string separated by spaces
    
    nmap_command = f"nmap -sP {ips_str}"
    nmap_scan = subprocess.run(nmap_command, shell=True, capture_output=True, text=True)
    
    # look for the lines that contain the MAC address
    ip_line = []
    mac_line = []

    for line in nmap_scan.stdout.split("\n"):
        if "MAC Address" in line:
            mac_line.append(line)
        if "Nmap scan report for" in line:
            ip_line.append(line.split(" ")[4])
        if "Unknown" in line:
            # scan os detection
            osScan = subprocess.run(f"nmap -O {ip_line[-1]}", shell=True, capture_output=True, text=True, timeout=15)
            
            for line in osScan.stdout.split("\n"):
                if "OS details" in line:
                    mac_line.pop()
                    mac_line.append(line)
    
    for i in range(len(ip_line)):
        print(colored(f"\n\t [+] IP: {ip_line[i].split()[-1]}", "blue"))
        print(colored(f"\t [+] {mac_line[i]}", "blue"))
                

def main():
    target = get_arguments()
    scan_ips(target)

if __name__ == "__main__":
    main()