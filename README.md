# Android Penetration Testing Tool
![image](https://github.com/user-attachments/assets/7af00cd9-7f1f-4581-ac55-2d1ee4971afa)

This project is an Android penetration testing tool that helps users create and manage payloads to establish remote connections to Android devices for educational and security testing purposes. The tool integrates Metasploit features like session management and payload generation within a command-line interface (CLI).

**Developed by Dr. Salah Abd Alhadi & Mohammad Abbas Shareef**

---

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Tool Options](#tool-options)
5. [Notes](#notes)
6. [License](#license)

---

## Requirements

To use this tool, ensure the following dependencies are installed on your system:

- Python 3.6+
- Metasploit Framework
- `pymetasploit3` Python library
- `msfvenom` and `msfconsole`
- `apktool` (for APK manipulation)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/MohammedAlkifaee/Android_Penetration_Tool.git]
   cd yourrepository
   ```

2. **Install the required Python packages**:
   Use a virtual environment for better dependency management:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install pymetasploit3
   ```

3. **Install Metasploit Framework** if not installed:
   ```bash
   sudo apt update
   sudo apt install metasploit-framework
   ```

4. **Ensure `apktool`, `msfvenom`, and `zipalign` are installed**:
   ```bash
   sudo apt install apktool
   ```

---

## Usage

1. **Start Metasploit RPC Server**:
   Open a new terminal and run:
   ```bash
   msfconsole -x "load msgrpc ServerHost=127.0.0.1 ServerPort=4444 User=msf Pass=12345678"
   ```

2. **Run the Tool**:
   In the main terminal, execute:
   ```bash
   python main.py
   ```

---

## Tool Options

After launching the tool, select the desired option from the menu:

1. **Set your host and port**: Configure the IP and port settings for the payload.
2. **Start Metasploit listener**: Initiate the listener session in Metasploit.
3. **Generate APK payload**: Use `msfvenom` to create an Android APK with a reverse TCP payload.
4. **Inject APK payload**: Integrate the payload into an existing APK (requires `apktool`).
5. **List active sessions**: Display currently active Metasploit sessions.
6. **Interact with a session**: Connect to an active session.
7. **Exit**: Close the tool.

---

## Notes

- **Permissions**: The payload APK includes multiple permissions, such as camera and location access, to demonstrate testing capabilities.
- **Testing**: Use the tool only within a controlled environment and with authorized devices.
  
---

## License

This project is for educational and ethical testing purposes only. Ensure compliance with applicable laws and guidelines.
