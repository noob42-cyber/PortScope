# PortScope

A lightweight TCP port scanner built from scratch in Python using the built-in `socket` library.

This project was created to understand how TCP connections, sockets, ports, timeouts, and concurrent scanning work at a practical level.

## Features

- Scan TCP ports on an IPv4 address
- Custom start and end port
- Detect open TCP ports
- Configurable connection timeout
- Live scanning progress
- Concurrent port scanning for improved performance
- Uses Python's built-in `socket` module
- No external scanning libraries required

## Requirements

- Python 3.11 or newer
- No external Python packages are required

Check your Python version with:

```bash
python --version
```

## Installation

Clone the repository:
```
git clone https://github.com/noob42-cyber/PortScope
```

Move into the project directory:
```
cd PortScope
```

No additional dependencies are required.

## Usage

Run the scanner:
```
python main.py
```
The scanner will ask for:

1. Target IPv4 address


2. Starting port


3. Ending port



Example:

Enter target IP: 192.168.1.10  
Enter start port: 1  
Enter end port: 1000  

Example output:

Port 135 is OPEN  
Port 445 is OPEN  

Only ports that successfully accept a TCP connection are displayed as open.

## How It Works

The scanner creates a TCP socket and attempts to establish a connection to each port in the selected range.

The basic process is:

Target IP  
    |  
    +---- Port 1   -> TCP connection attempt  
    |  
    +---- Port 2   -> TCP connection attempt  
    |  
    +---- Port 3   -> TCP connection attempt  
    |  
    ...  
    |  
    +---- Port 135 -> Connection succeeds -> OPEN  
    |  
    +---- Port 445 -> Connection succeeds -> OPEN  

A successful TCP connection indicates that the target accepted the connection on that port.

If the connection is refused or times out, the port is not reported as open.

### TCP Socket

The scanner uses:
```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```
Where:

`AF_INET` specifies IPv4.

`SOCK_STREAM` specifies a TCP socket.


The scanner then attempts to connect using:
```python
socket.connect((ip, port))
```
### Timeout

A connection timeout prevents the scanner from waiting indefinitely for a response.

For example:
```python
s.settimeout(0.5)
```

The timeout value can be adjusted depending on the environment.

A shorter timeout can make scanning faster, while a longer timeout can give slower networks more time to respond.




### Port Range

TCP ports range from:

`0 - 65535`

Commonly referenced ranges include:

| Range	| Description |
|       |           |
| 0–1023 |	Well-known ports |
| 1024–49151 |	Registered ports |
| 49152–65535 |	Dynamic/private ports |


The scanner can scan any port range supplied by the user.

Project Structure

tcp-scanner/  
├── main.py  
├── port_scanner.py  
├── README.md  
└── .gitignore  

## Responsible Use

Use this scanner only against:

Your own computer

Your own network

A device you have permission to test

A deliberately provided security-testing environment


Do not scan systems or networks without authorization.




