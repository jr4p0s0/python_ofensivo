#!/usr/bin/env python3

import datetime

ahora = datetime.datetime.now() # fecha y hora actual

print(f"\n [+] Fecha y hora actual: {ahora}")

fecha = datetime.date(2021, 12, 31) # fecha específica

print(f"\n [+] Fecha específica: {fecha}")

hora = datetime.time(23, 59, 59) # hora específica

print(f"\n [+] Hora específica: {hora}")

FyH = datetime.datetime(2021, 12, 31, 23, 59, 59) # fecha y hora específica

print(f"\n [+] Fecha y hora específica: {FyH}")

'''
+---------------------+
'''

ahora = datetime.datetime.now()

anio = ahora.year
mes = ahora.month
dia = ahora.day
hora = ahora.hour
minuto = ahora.minute
segundo = ahora.second

print(f"\n [+] Fecha: {dia}/{mes}/{anio}")
print(f"\n [+] Hora: {hora}:{minuto}:{segundo}")


