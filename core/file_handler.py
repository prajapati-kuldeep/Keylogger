import os

LOG_FILE = "logger.txt"

def write_log(data):
    with open(LOG_FILE, "w") as f:
        f.write(data)

def read_log():
    if not os.path.exists(LOG_FILE):
        return ""
    with open(LOG_FILE, "r") as f:
        return f.read()
