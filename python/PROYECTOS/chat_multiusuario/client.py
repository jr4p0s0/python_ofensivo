#!/usr/bin/env python3

import socket
import threading
from customtkinter import *
import ssl

def send_message(c_socket, username, text_widget, entry_widget):
    
    message = entry_widget.get() # Get the message from the entry widget
    
    if message:
        c_socket.sendall(f"{username} > {message}".encode()) # Send the message to the server 
        entry_widget.delete(0, 'end') # Clear the entry widget
        
        text_widget.configure(state='normal') # Enable the text widget
        text_widget.insert('end', f"{username} > {message}\n") # Display the message
        text_widget.configure(state='disabled') # Disable the text widget
            

def receive_messages(c_socket, text_widget):
        
        while True:
            try:
                message = c_socket.recv(1024).decode() # Receive the message from the server
                text_widget.configure(state='normal') # Enable the text widget
                text_widget.insert('end', message) # Display the message
                text_widget.configure(state='disabled') # Disable the text widget
            except:
                print("\n [+] Error al recibir el mensaje")
                c_socket.close()
                break
            
def list_users(c_socket):
    c_socket.sendall("list_users".encode()) # Send the command to the server
    
def exit_req(window, c_socket, username):
    c_socket.sendall(f"\n[!] El usuario {username} ha abandonado el chat\n".encode()) # Send the command to the server
    c_socket.close()
    
    window.quit()
    window.destroy()
    

def client_program():
    
    host = 'localhost'
    port = 12345
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPV4, TCP
    
    client_socket = ssl.wrap_socket(client_socket)
    
    client_socket.connect((host, port)) # Connect to the server

    username = input("\n [+] Introduce tu nombre de usuario: ")
    
    client_socket.sendall(username.encode()) # Send the username to the server
    
    window = CTk()
    window.title("Chat")
    window.geometry("600x400")
    
    upper_frame = CTkFrame(window)
    upper_frame.pack(fill='both', padx=7, pady=7)
    
    text_title_info = CTkLabel(upper_frame, text=f"AppChat", font=("Hack Nerd Font", 20))
    text_title_info.pack(pady=7, side='left', padx=7)
    
    text_title_info_username = CTkLabel(upper_frame, text=f"Usuario: {username}", font=("Hack Nerd Font", 15))
    text_title_info_username.pack(pady=7, side='right', padx=7)
    
    
    text_widget = CTkTextbox(window, state='disabled', font=("Hack Nerd Font", 15)) # Disable the text widget to prevent editing; only for display
    text_widget.pack(expand=True, fill='both', padx=7, pady=7)
    
    frame_widget = CTkFrame(window)
    frame_widget.pack(fill='both', padx=7, pady=7)
    
    button = CTkButton(frame_widget, text="Enviar", command=lambda: send_message(client_socket, username, text_widget, entry_widget), 
                        width=12,
                        font=("Hack Nerd Font", 15),
                        corner_radius=10,  
                        fg_color="#000000")
    button.pack(fill='both', pady=5, padx=5, side='right')
    
    button_list = CTkButton(window, text="Listar Usuarios", command=lambda: list_users(client_socket), 
                        width=12,
                        font=("Hack Nerd Font", 15),
                        corner_radius=10,  
                        fg_color="#000000")
    button_list.pack(pady=5, padx=5)
    
    
    button_exit = CTkButton(window, text="Salir", command=lambda: exit_req(window, client_socket, username), 
                        width=12,
                        font=("Hack Nerd Font", 15),
                        corner_radius=10,  
                        fg_color="#000000")
    button_exit.pack(pady=5, padx=5)
    
    entry_widget = CTkEntry(frame_widget, font=("Hack Nerd Font", 15))
    entry_widget.bind("<Return>", lambda event: send_message(client_socket, username, text_widget, entry_widget))
    entry_widget.pack(fill='both', pady=5, padx=5, side='left', expand=True)
    
    thread = threading.Thread(target=receive_messages, args=(client_socket, text_widget))
    thread.daemon = True # Quitting without waiting for the thread to finish
    thread.start()
    
    window.mainloop()
    
    client_socket.close()    
    

if __name__ == '__main__':
    client_program()