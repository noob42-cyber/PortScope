lazy import socket
lazy import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
lazy import time

log_file = Path(__file__).parent/"scan.log"

# Set up logging

logging.basicConfig(level = logging.DEBUG,filename=log_file,format='%(asctime)s -%(levelname)s - %(message)s',filemode= 'a')

# Port Scanner Logic to try to connect through sockets
print("Port   Service  status")
def port_scan(ip_adress,port,timeout):
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip_adress,port))
            try:
                service = socket.getservbyport(port)
            except OSError:
                 service = "Unknown"
        print(f"{port}   {service}  open")
        logging.info (f"Port {port} is open")
    except ConnectionRefusedError:
        logging.warning(f"Port{port}:Connection refused")
    except TimeoutError:
        logging.debug(f"Port {port} : Connection time timeout")
    except OSError as e:
            logging.error(f"Port{port}:OS Error - {e}")
    finally:
        s.close()

# ThreadPollExecutor for concurrent trail of connecting to ports

def tcp_scanner_port(ip_address,starting_port,ending_port,workers,timeout):
    start = time.time()
    with ThreadPoolExecutor(max_workers = workers) as executor:
            futures = [
               executor.submit(port_scan,ip_address,port,timeout)
               for port in range(starting_port,ending_port+1)
           ]
    elapsed = time.time()-start
    logging.info("Scanning Completed")
    return {"elapsed":elapsed}
    

        
