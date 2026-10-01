import socket

def port_scanner_tcp(ip,start_port,end_port):
    for i in range(start_port,end_port+1):
        print(f"\rTrying Port {i}...",end="\r",flush=True)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.2)
        try:
            s.connect((ip,i))
            print(f"Port {i} is open")
        except (ConnectionRefusedError,TimeoutError,OSError):
            pass
        finally:
            s.close()



        
