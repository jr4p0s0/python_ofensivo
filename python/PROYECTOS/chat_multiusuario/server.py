#!/usr/bin/env python3

import socket
import threading
import ssl

def client_thread(c_socket, clients, usernames):
    
    print(f"\n [+] Nuevo hilo para {c_socket}")
    
    username = c_socket.recv(1024).decode() # Receive the username from the client
    usernames[c_socket] = username # Add the username to the dictionary
    
    print(f"\n [+] Nombre de usuario: {username}")
    
    for client in clients:
        if client is not c_socket:
            client.sendall(f"\n[+] {username} se ha unido al chat\n\n".encode())
    
    while True:
        try: 
            message = c_socket.recv(1024).decode() # Receive the message from the client
            
            if not message:
                break
            
            if message == "list_users":
                users = f"\n [*] Usuarios conectados: {', '.join(usernames.values())}\n\n"
                c_socket.sendall(users.encode())
                continue
            
            print(f"\n [+] {username} > {message}")
                
            for client in clients:
                if client is not c_socket:
                    client.sendall(f"{message}\n".encode())
        except:
            break
    
    c_socket.close()
    clients.remove(c_socket)
    del usernames[c_socket]
    print(f"\n [!] {username} ha abandonado el chat")


def server_program():
    
    host = 'localhost'
    port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4, TCP
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reuse the socket | TIME_WAIT state
    
    server_socket.bind((host, port)) # Bind the socket to the address
    server_socket = ssl.wrap_socket(server_socket, server_side=True, certfile="server-cert.pem", keyfile="server-key.key")
    
    server_socket.listen() # Listen for incoming connections

    print("\n [+] Servidor a la espera de conexiones...")
    
    clients = [] # List of clients (sockets)
    usernames = {} # Dictionary of usernames (key: client_socket, value: username)

    while True:
        c_socket, c_addr = server_socket.accept() 
        clients.append(c_socket)
        
        print(f"\n [+] Conexión establecida con {c_addr}")

        thread = threading.Thread(target=client_thread, args=(c_socket, clients, usernames))
        thread.daemon = True # Quitting without waiting for the thread to finish
        thread.start()
    
    server_socket.close()
        

if __name__ == "__main__":
    server_program()