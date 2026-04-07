# Keylogger

## Overview
This project demonstrates a basic keystroke logging system designed for educational and security testing purposes. It captures keyboard input, stores it locally, and sends the recorded data via email using an SMTP server.

---

## Features

### 1. Keylogger
- Captures all keyboard inputs from the target system  
- Runs in the background until terminated  

### 2. File Logging
- Stores all captured keystrokes in a file named `logger.txt`  
- The file is saved upon script termination  

### 3. Email Reporting
- Automatically sends logged keystrokes to a configured email address  
- Uses SMTP credentials defined in `services/email_service.py`  

### 4. Self-Deletion Mechanism
- If specific conditions are met (e.g., detection of `"logger.py"` in logs), the script deletes itself  
- Designed to simulate stealth behavior in controlled environments  

---

## Installation

1. Clone or download the project files  

2. Configure email credentials:
   - Open `services/email_service.py`  
   - Update the following fields:
     - SMTP server host  
     - Email address  
     - SMTP username and password  

3. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
1. Setup Mail Service
Create an account at **Mailtrap** or use a temporary test email account and Obtain your SMTP credentials.

2. Configure Script
Insert your SMTP username and password into the designated variables within `services/email_service.py`

3. Run the **Keylogger**
```bash
python logger.py
```
## 4. Execution Behavior

* The script begins capturing keystrokes immediately
* All keystrokes are recorded into `logger.txt`

---

## 5. Termination

* Press the `ESC (Escape)` key to stop the keylogger

Upon termination:

* `logger.txt` is finalized
* `main.py` executes automatically
* Logged data is sent via email

---

## Output

| File         | Description                                                  |
| ------------ | ------------------------------------------------------------ |
| `logger.txt` | Contains all recorded keystrokes captured during the session |

---

## Requirements

* Python 3.x
* `pynput` library (for capturing keyboard events)

Install manually if needed:

```bash
pip install pynput
```

---

## Security Note

This project includes a self-deletion feature:

* If the script detects certain predefined strings (e.g., `"logger.py"` in logs), it removes itself from the system

This behavior is implemented strictly for demonstrating **evasion techniques** in cybersecurity studies.

---

## ⚠️ Disclaimer

This tool is intended strictly for **educational purposes** and **authorized security testing only**.

Unauthorized use of keyloggers is **illegal and unethical**. Always obtain explicit consent before running this software on any system.

---

## Author Notes

This project is a simplified demonstration of:

* Input monitoring
* File handling
* SMTP-based communication
* Basic stealth techniques