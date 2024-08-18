#!/usr/bin/env python3

import netfilterqueue
import scapy.all as scapy
import signal
import sys
from termcolor import colored
import subprocess

def def_handler(signal, frame):
    print(colored("\n[!] Closing program...\n", 'red'))
    sys.exit(0)
    
signal.signal(signal.SIGINT, def_handler)

subprocess.run("iptables -D INPUT -j NFQUEUE --queue-num 0", shell=True)
subprocess.run("iptables -D OUTPUT -j NFQUEUE --queue-num 0", shell=True)
subprocess.run("iptables -D FORWARD -j NFQUEUE --queue-num 0", shell=True)
subprocess.run("iptables --policy FORWARD ACCEPT", shell=True)
subprocess.run("./enable_ip_forward.sh 0", shell=True)
# Change MAC to 00:11:22:33:44:55

subprocess.call("python3 macchanger.py -i wlp4s0 -m 64:49:7d:e6:66:94", shell=True)