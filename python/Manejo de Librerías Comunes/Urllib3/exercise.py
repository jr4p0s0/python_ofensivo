#!/usr/bin/env python3

import urllib3

http = urllib3.PoolManager()

response = http.request("GET", "https://www.google.com")

print(f"\n [+] Código de estado: {response.status}")
print(f"\n [+] Data: {response.data.decode('iso-8859-1')}")