lazy import socket
lazy import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed

log_file = Path(__file__).parent/"scan.log"

# Set up logging

logging.basicConfig(level = logging.DEBUG,filename=log_file,format='%(asctime)s -%(levelname)s - %(message)s',filemode= 'a')

# Port Scanner Logic to try to connect through sockets

def port_scan(ip_adress,port):
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.settimeout(3.0)
            s.connect((ip_adress,port))
            print(f"Port Open:{port}:{socket.getservbyport(port)}")
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

def tcp_scanner_port(ip_address,starting_port,ending_port,workers):

    with ThreadPoolExecutor(max_workers = workers) as executor:
            futures = [
               executor.submit(port_scan,ip_address,port)
               for port in range(starting_port,ending_port+1)
           ]
            for future in as_completed(futures):
                result = future.result()
    logging.info("Scanning Completed")
    

        
