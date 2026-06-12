# Mini Network Port Scanner 🔍

A lightweight, fast, and multi-threaded network port scanner built with Python. 
This tool scans a target IP address to identify open ports (scanning standard ports 1-1024) and demonstrates core networking concepts and object-oriented scripting.

## Features
* **Speed:** Utilizes `concurrent.futures.ThreadPoolExecutor` for fast multi-threaded scanning.
* **Accuracy:** Uses Python's built-in `socket` library for reliable TCP connections.
* **Data Management:** Automatically saves scan results into a clean, formatted text file.
* **User-friendly:** Clear console output with start/end timestamps.

## Prerequisites
* Python 3.x installed

## Usage
1. Clone the repository:
   ```bash
   git clone [https://github.com/giorgimelikidze06/Python-Port-Scanner.git](https://github.com/giorgimelikidze06/Python-Port-Scanner.git)
   ```
2. Navigate to the directory and run the script:
   ```bash
   python scanner.py
   ```
3. Enter the target IP address when prompted (e.g., `127.0.0.1` for local testing).

## Technical Concepts Demonstrated
* Socket Programming / Networking basics
* Multi-threading in Python for performance optimization
* File I/O operations (saving results to a `.txt` file)
* Error handling and exception management
