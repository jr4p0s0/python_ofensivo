#!/usr/bin/env python3

import subprocess
import re
import argparse
from termcolor import colored
import sys
import signal


def def_handler(sig, frame):
    print(colored("\n\n [!] Exiting program...\n", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Ctrl+C handler

def get_arguments():
    parser = argparse.ArgumentParser(description="MAC changer")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change its MAC address (Ex: -i eth0)")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="New MAC address (Ex: -m 00:11:22:33:44:55)")
    options = parser.parse_args()
    
    return options

def is_valid_input(interface, new_mac):
    
    is_valid_interface = re.match(r"^[a-zA-Z0-9]*$", interface)
    is_valid_mac = re.match(r"^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$", new_mac)
    
    return is_valid_interface and is_valid_mac

def change_mac_address(interface, new_mac):
    
    # Check if the interface exists
    if is_valid_input(interface, new_mac):
        print(colored(f"\n [+] Changing MAC address for {interface} to {new_mac}", "blue"))
        subprocess.run(["ifconfig", interface, "down"])
        subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.run(["ifconfig", interface, "up"])
        print(colored(f"\n [+] MAC address for {interface} changed to {new_mac}\n", "green"))
        subprocess.run(["ifconfig", interface])
    else:
        print(colored("\n [!] Invalid input", "red"))
        return

def main():
    args = get_arguments()
    change_mac_address(args.interface, args.new_mac)
    
if __name__ == "__main__":
    main()