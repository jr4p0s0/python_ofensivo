#!/usr/bin/env python3

import threading
import time
import multiprocessing
import requests

def tarea(num):
    print(f"\n [+] Proc {num} iniciando")
    time.sleep(2)
    print(f"\n [+] Proc {num} finalizado")

# thread1 = threading.Thread(target=tarea, args=(1,))
# thread2 = threading.Thread(target=tarea, args=(2,))

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()

# proc1 = multiprocessing.Process(target=tarea, args=(1,))
# proc2 = multiprocessing.Process(target=tarea, args=(2,))

# # proc1.start()
# # proc2.start()

# # proc1.join()
# # proc2.join()

# # print("\n [+] Hilos finalizados")

def request(url):
    response = requests.get(f"https://{url}")
    print(f"\n [+] URL: {response.url}: {len(response.content)} bytes")
    print(f"\n [+] Datos en binario: {response.content[:100]}")

dominios = ["www.google.com", "www.facebook.com", "www.youtube.com", "www.amazon.com", "www.udemy.com"]

startTime = time.time()

procesos = []
for url in dominios:
    proceso = multiprocessing.Process(target=request, args=(url,))
    proceso.start()
    procesos.append(proceso)
    
for proceso in procesos:
    proceso.join()    
    
print(f"\n [+] Tiempo de ejecución: {round(time.time() - startTime, 3)}")

import sys

print(sys.args)