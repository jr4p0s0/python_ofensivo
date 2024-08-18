#!/usr/bin/env python3

import socket
    
def start_client():
    host = "localhost"
    port = 12345
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        while True:
            message = input("\n [?] Introduce un mensaje: ")
            client_socket.sendall(message.encode())
            
            if message.strip() == "exit":
                break
            
            data = client_socket.recv(1024).strip().decode()
            print(f"\n [+] Datos recibidos: {data}")
    
start_client()