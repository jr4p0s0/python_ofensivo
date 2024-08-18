#!/usr/bin/env python3

from mitmproxy import http
from mitmproxy import ctx

def request(packet):
    ctx.log.info(f"[+] URL visitada por la victima: {packet.pretty_url}")
    
def response(packet):
    ctx.log.info(f"[+] Response: {packet.pretty_url}")