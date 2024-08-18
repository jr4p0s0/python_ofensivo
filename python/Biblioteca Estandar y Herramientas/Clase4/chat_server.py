#!/usr/bin/env python3

import socket

def start_chat_server():
    
    host = "localhost"
    port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reutilizar dirección
    server_socket.bind((host, port))
    server_socket.listen(1)
    
    print(f"\n [+] Servidor escuchando en {host}:{port}")
    
    conn, addr = server_socket.accept()
    
    print(f"\n [+] Conexión establecida con {addr}")
    
    while True:
        data = conn.recv(1024).strip().decode()
        print(f"\n [+] Mensaje del cliente: {data}")
        
        if data == "exit":
            break
        
        server_message = input("\n [?] Introduce un mensaje para el cliente: ")
        conn.sendall(server_message.encode())
    
    conn.close()
        
        

start_chat_server()