# 🛡 Anti-Keylogger (Python)

This project is a basic Anti-Keylogger tool written in Python. It scans the system for known keylogger processes and automatically terminates them to help protect user privacy and security.

---

##  Features

- Continuously monitors running processes on the system
- Detects known keylogger programs by name
- Terminates suspicious processes if found
- Simple and lightweight — ideal for learning and testing
- Helps raise awareness about keylogging and basic cybersecurity

---

## 🛠 Technologies Used

- Python 3
- `psutil` library for process monitoring

---

##  How It Works

1. The program maintains a list of known keylogger process names (e.g., `keylogger.exe`, `kl.exe`).
2. It runs in a loop, checking all active system processes.
3. If it detects a process name matching the list, it logs a warning and attempts to terminate the process.
4. Scans are repeated every 10 seconds to ensure continuous protection.

---

## Getting Started

###  Prerequisites

Make sure you have Python 3 installed. Then install `psutil`:

```bash
pip install psutil
