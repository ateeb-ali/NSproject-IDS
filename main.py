# main.py

from scapy.all import sniff
from detector import detect

print("Starting Simple IDS...")
print("Press CTRL+C to stop.\n")

sniff(prn=detect, store=False)
