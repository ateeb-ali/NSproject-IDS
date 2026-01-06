# logger.py

from datetime import datetime

def log_alert(message):
    with open("alerts.log", "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] {message}\n")
