#!/usr/bin/env python3

import socket
import threading
    
def start_server():
    host = "localhost"
    port = 12345
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        
        print(f"\n [+] Servidor escuchando en {host}:{port}")
        
        conn, addr = server_socket.accept()
        
        with conn:
            print(f"\n [+] Conexión establecida con {addr}")
            
            while True:
                data = conn.recv(1024)
                
                if not data:
                    break
                
                print(f"\n [+] Datos recibidos: {data.decode()}")
                conn.sendall(data)


class ClientThread(threading.Thread):
    def __init__(self, conn, addr):
        super().__init__()
        self.conn = conn
        self.addr = addr
        
        print(f"\n [+] Nueva conexión desde {self.addr}")
        
    def run(self):
        with self.conn:
            print(f"\n [+] Conexión establecida con {self.addr}")
            
            while True:
                data = self.conn.recv(1024) # recibir datos
                message = data.decode() # decodificar datos
                # quitar saltos de línea
                
                if message.replace("\n", "") == "exit": 
                    print(f"\n [!] Conexión con {self.addr} finalizada")
                    break
                
                if not data:
                    break
                
                print(f"\n [+] Datos recibidos: {message.strip()}")
                self.conn.send(data) # enviar datos

def start_server2():
    HOST = 'localhost'
    PORT = 12345
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reutilizar dirección si está ocupada
        s.bind((HOST, PORT))
        print(f"\n [+] Servidor escuchando en {HOST}:{PORT}")        
        while True:
            
            s.listen()
            conn, addr = s.accept()
            
            new_thread = ClientThread(conn, addr)
            new_thread.start()

start_server2()