import psutil
import time

# Sample list of known keylogger process names (for demo)
known_keyloggers = ['keylogger', 'keylogger.exe', 'kl.exe']

def detect_keylogger():
    print("Scanning for suspicious keylogger processes...")
    while True:
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                process_name = proc.info['name'].lower()
                if process_name in known_keyloggers:
                    print(f"[ALERT] Possible keylogger detected: {process_name} (PID: {proc.info['pid']})")
                    proc.terminate()
                    print("Process terminated.")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        time.sleep(10)  # Scan every 10 seconds

if __name__ == "__main__":
    detect_keylogger()
