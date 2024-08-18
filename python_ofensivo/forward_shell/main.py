#!/usr/bin/env python3

from forward_shell import ForwardShell
import signal
import sys
from termcolor import colored

def signal_handler(sig, frame):
    print(colored('\n[!] Saliendo...\n', 'red'))
    my_forward_shell.remove_data()
    sys.exit(0)
    
signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    my_forward_shell = ForwardShell()
    my_forward_shell.run()
    
