# PRODIGY_CY_05
# 📡 Python Packet Sniffer (Educational Use Only)

This is a basic IP packet sniffer written using raw sockets in Python.

## ⚠️ Disclaimer

This tool is intended **only for educational and ethical hacking purposes** on **networks you own or have permission to test**. Unauthorized sniffing is illegal and unethical.

## 🚀 Features

- Captures raw IP packets (Windows only, admin required)
- Uses raw sockets
- Easy to modify for protocol filtering (ICMP, TCP, etc.)

## 🔧 Requirements

- Windows OS (for `SIO_RCVALL`)
- Python 3
- Admin/root privileges

## ▶️ Usage

1. Replace the IP in `core.py` with your machine's actual IP.
2. Run:

```bash
python -m packet_sniffer.core
