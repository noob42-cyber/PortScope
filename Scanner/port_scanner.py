lazy import socket
lazy import logging
lazy from pathlib import Path
lazy from concurrent.futures import ThreadPoolExecutor,as_completed 
lazy from validator import service_validator

log_file = Path(__file__).parent/"scan.log"

# Set up logging

logging.basicConfig(level = logging.DEBUG,filename=log_file,format='%(asctime)s -%(levelname)s - %(message)s',filemode= 'a')

# Port Scanner Logic to try to connect through sockets
def port_scan(ip_adress,port,timeout):
    service = service_validator(port)
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip_adress,port))
        logging.info(f"Port {port} is open")
        return {"port":port,"status":"open","service": service }
    except ConnectionRefusedError:
        logging.warning(f"Port{port}:Connection refused")
        return {"port":port,"status":"closed","service": service}
    except TimeoutError:
        logging.debug(f"Port {port} : Connection time timeout")
        return {"port":port,"status":"timeout","service":service} 
    except OSError as e:
            logging.error(f"Port{port}:OS Error - {e}")
            return {"port":port,"status":"error","service":service}

# ThreadPollExecutor for concurrent trail of connecting to ports

def tcp_scanner_port(ip_address,starting_port,ending_port,workers,timeout):
    results = []
    with ThreadPoolExecutor(max_workers = workers) as executor:
            futures = [
               executor.submit(port_scan,ip_address,port,timeout)
               for port in range(starting_port,ending_port+1)
           ]
            for future in as_completed(futures):
                ports = future.result() 
                if ports['status'] == "open":
                    results.append(ports)        
    logging.info("Scanning Completed")
    return results