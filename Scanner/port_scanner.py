import socket
import logging
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

log_file = Path(__file__).parent/"scan.log"

logging.basicConfig(level = logging.DEBUG,filename=log_file,format='%(asctime)s -%(levelname)s - %(message)s',filemode= 'a')

def port_scan(ip,port):
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip,port))
            logging.info(f"Port {port} ports open")
    except ConnectionRefusedError:
        logging.warning(f"Port{port}:Connection refused")
    except TimeoutError:
        logging.debug(f"Port {port} : Connection time timeout")
    except OSError as e:
            logging.error(f"Port{port}:OS Error - {e}")
    finally:
        s.close()


def tcp_scanner_port(ip,start_port,end_port):
    open_port = []

    with ThreadPoolExecutor(max_workers = 20) as executor:
            futures = [
               executor.submit(port_scan,ip,port)
               for port in range(start_port,end_port+1)
           ]
            for future in as_completed(futures):
                result = future.result()
    logging.info("Scanning Completed")
    

        
