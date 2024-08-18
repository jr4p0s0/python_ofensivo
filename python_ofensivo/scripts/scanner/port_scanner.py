#!/usr/bin/env python3

import socket
from termcolor import colored
import argparse
from concurrent.futures import ThreadPoolExecutor
import sys
import signal
from threading import Event

open_sockets = []

stop_event = Event()

def def_handler(sig, frame):
    print(colored("\n\n [!] Exiting program...\n", "red"))
    stop_event.set() # set the stop event to stop the threads
    for s in open_sockets:
        s.close()

    sys.exit(1)

signal.signal(signal.SIGINT, def_handler) # Ctrl+C handler

def get_arguments():
    parser = argparse.ArgumentParser(description="Port scanner")
    parser.add_argument("-t", "--target", dest="target", required=True, help="Target IP address to scan ports (Ex: -t 192.168.1.1)")
    parser.add_argument("-p", "--port", dest="port", required=True, help="Port range to scan (Ex: -p 1-1024)")
    options = parser.parse_args()
    
    return options.target, options.port


def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4 and TCP
    s.settimeout(0.5) # 0.1 seconds timeout
    open_sockets.append(s) 
    return s

def port_scanner(port, target):
    
    while not stop_event.is_set():
        s = create_socket()
        try:
            s.connect((target, port))
            s.sendall(b'HEAD / HTTP/1.1\r\n\r\n')
            response = s.recv(1024).decode(errors='ignore')
            if response:
                response = response.split("\n")
                print(colored(f"\n [+] Port {port} is open", "green"))
                print(colored("\n [*] ", "blue"), end="")
                for line in response:
                    print(colored(f"\t {line}", "blue"))
            else:       
                print(colored(f"\n [+] Port {port} is open", "green"))
                
        except (ConnectionRefusedError, socket.timeout):
            pass
        finally:
            s.close()
        break
    
def scan_ports(target, ports):
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(lambda port: port_scanner(port, target), ports)
        # need to use lambda function to pass just the iterable port to the function port_scanner, otherwise it will be an error

def parse_ports(ports_str):
    
    try:
        if "-" in ports_str:
            start, end = map(int, ports_str.split("-"))
            return range(start, end+1)
        elif "," in ports_str and '' not in ports_str:
            return ports_str.split(",")
        else: 
            return [int(ports_str)]
    
    except (ValueError, TypeError):
            print(colored("\n [-] Invalid port range\n\n", "red"))
            sys.exit(1)

def main():
    
    target, ports_str = get_arguments()
    ports = parse_ports(ports_str)
    scan_ports(target, ports)

if __name__ == '__main__':
    main()