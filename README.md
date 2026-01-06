# Simple Network Intrusion Detection System (IDS)

This project is a beginner friendly Network based Intrusion Detection System built using Python and Scapy.  
It monitors live network traffic and detects basic suspicious activities such as flooding, port scanning, and malicious payload patterns.

The main goal of this project is to help students understand how intrusion detection works in a simple and practical way.

---

## Features

- Live packet sniffing  
- Detection of excessive traffic from a single IP  
- Basic port scan detection  
- Signature based detection using keywords  
- Real time alerts on screen  
- Alert logging in a file  

---

## Technologies Used

- Python  
- Scapy library  
- Windows or Linux OS  

---
```bash
ids_project/
│
├── main.py
├── detector.py
├── rules.py
├── logger.py
├── rules.txt
├── requirements.txt
└── README.md
```


---

## How It Works

1. The system captures live network packets using Scapy  
2. Each packet is analyzed for suspicious behavior  
3. Predefined rules are applied to detect possible attacks  
4. When an intrusion is detected, an alert is shown  
5. All alerts are saved in a log file for future reference  

---

## How To Run

1. Open terminal in the project folder  
2. Install dependencies  
```bash
pip install -r requirements.txt
```
3. Run the IDS as administrator  
```bash
python main.py
```

---

## Testing The System

You can test the IDS using simple commands.

Flood test  
```bash
ping 127.0.0.1 -t
```

Port scan test if you have nmap installed
```bash
nmap 127.0.0.1
```

---

## Future Improvements

- Add machine learning based detection  
- Create a web dashboard for alerts  
- Add automatic response features  
- Improve accuracy of detection rules  

---
## Notice
Developed for academic and learning purposes




## Project Structure

