# Basic Keylogger (Ethical Monitoring) ⌨️🛡️

This project is a **Python-based Basic Keylogger** developed as **Task-04** during a **Cyber Security Internship at Prodigy InfoTech**. 
The tool records keystrokes and saves them to a local text file to demonstrate how input monitoring and endpoint logging function for educational and security research purposes.



### ⚠️ Ethical Use Notice

This tool is designed strictly for **learning, authorized testing, and ethical analysis**. 
* **Permission Required:** Never use this tool on a computer you do not own or without explicit, written consent.
* **Educational Purpose:** Created to understand how malware (Spyware) operates and how SOC teams detect such activity.
* **Local Logging Only:** Captured data is stored locally on the host machine and is NOT transmitted over a network.
* **Prohibited Use:** Any unauthorized use of this tool for malicious purposes is strictly illegal and unethical.

### 2. ⚙️ How It Works

The tool utilizes the `pynput` library to create a background "Listener" thread that monitors hardware interrupts from the keyboard.

1.  **Listener Initialization:** The script starts a non-blocking thread that waits for a `KeyPress` event.
2.  **Event Handling:** When a key is pressed, the `on_press` function captures the character.
3.  **Data Formatting:** Alphanumeric keys are recorded directly, while special keys (Space, Enter, Esc) are mapped to readable strings.
4.  **Persistent Logging:** The data is appended to `keylog.txt` in real-time using Python's File I/O.
5.  **Termination:** The process continues until the user presses the `Esc` key, triggering the `on_release` stop condition.



### 🛠️ Features

* **Real-time Capture:** Monitors and logs keystrokes in the background using thread-based listeners.
* **Special Key Handling:** Automatically converts hardware events like `Space`, `Enter`, and `Tab` into readable text.
* **Dynamic File Pathing:** Uses the `os` module to ensure compatibility across different environments.
* **Safe Exit Mechanism:** Includes a programmed escape sequence (Pressing `Esc`) to stop the listener.

### 🚀 How to Run

#### Requirements
* Python 3.x
* `pynput` library

#### 1. Install Dependencies:
```bash
pip install pynput
```

#### 2. Run the Script:
```bash
python keylogger.py
```

#### 📝 Example Output (keylog.txt):
```bash
Hello [Key.shift]World [Key.enter]
This is a test of Task 04. [Key.tab] Logged successfully.
```
