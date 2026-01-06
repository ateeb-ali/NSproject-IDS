# detector.py

from rules import MAX_PACKETS_PER_IP
from logger import log_alert

ip_counter = {}
port_counter = {}

def load_signatures():
    try:
        with open("rules.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except:
        return []

SIGNATURES = load_signatures()

def detect(packet):
    alerts = []

    # IP flood detection
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src

        if src_ip not in ip_counter:
            ip_counter[src_ip] = 1
        else:
            ip_counter[src_ip] += 1

        if ip_counter[src_ip] == MAX_PACKETS_PER_IP:
            msg = f"Possible DoS attack from {src_ip}"
            alerts.append(msg)

    # Port scan detection
    if packet.haslayer("TCP"):
        src = packet["IP"].src
        dport = packet["TCP"].dport

        key = (src, dport)
        if key not in port_counter:
            port_counter[key] = 1
        else:
            port_counter[key] += 1

        if len([k for k in port_counter if k[0] == src]) == 20:
            msg = f"Possible port scan from {src}"
            alerts.append(msg)

    # Signature detection
    if packet.haslayer("Raw"):
        payload = str(packet["Raw"].load).lower()

        for sig in SIGNATURES:
            if sig.lower() in payload:
                msg = f"Suspicious payload detected from {packet['IP'].src} keyword: {sig}"
                alerts.append(msg)

    # Print and log alerts
    for alert in alerts:
        print("ALERT:", alert)
        log_alert(alert)
