#!/usr/bin/env python3

import argparse
import socket
import subprocess
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor
import signal
import sys
import threading

stop_event = threading.Event()

def def_handler(sig, frame):
    print(colored("\n\n [!] Exiting program...\n", "red"))
    stop_event.set() # set the stop event to stop the threads
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Ctrl+C handler

def get_arguments():
    parser = argparse.ArgumentParser(description="ICMP scanner: Scan for live hosts")
    parser.add_argument("-t", "--target", dest="target_str", required=True, help="Target IP address to scan ports (Ex: -t 192.168.1.1-200)")
    options = parser.parse_args()

    return options.target_str

def parse_target(target_str):

    targets = []
    
    if "-" in target_str:
        target = target_str.split("-")
        target_start = target[0].split(".")
        target_end = target[1]
        for i in range(int(target_start[3]), int(target_end)+1):
            targets.append(target_start[0] + "." + target_start[1] + "." + target_start[2] + "." + str(i))
    else:
        targets.append(target_str)
    
    print(colored(f"\n [*] Scanning {target_str} for live hosts", "blue"))
    return targets

def scan_ips(targets):
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(ip_scanner, targets)
    
def ip_scanner(target):
    
    while not stop_event.is_set():
        try:
            ret = subprocess.run(["ping", "-c", "1", target], timeout=1, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if ret.returncode == 0:
                print(colored(f"\n\t[+] {target} is up", "green"))
                
        except subprocess.TimeoutExpired:
            pass
        break

def main():
    target_str = get_arguments()
    targets = parse_target(target_str)
    scan_ips(targets)
    
if __name__ == "__main__":
    main()
