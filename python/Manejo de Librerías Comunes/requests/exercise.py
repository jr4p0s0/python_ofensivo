#!/usr/bin/env python3

import requests # Importante no nombrar al archivo como requests.py

url = "https://www.google.com"

response = requests.get(url)

print(f"\n [+] Código de estado: {response.status_code}")

print(f"\n [+] Headers: {', '.join([header for header in response.headers])}")

print(f"\n [+] Cookies: {', '.join([cookie.name for cookie in response.cookies])}")

print(f"\n [+] URL: {response.url}")

with open("index.html", "w") as file:
    file.write(response.text)

print("\n [+] Archivo index.html creado")


'''
+---------------------------------------------------------------------------------------------------------------------+
'''

response = requests.get("https://httpbin.org/basic-auth/foo/bar", auth=("foo", "bar"))

print(f"\n [+] Código de estado: {response.status_code}")

print(f"\n [+] text: {response.text}")

