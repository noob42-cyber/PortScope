lazy import ipaddress

def ip_validator(ip_address):
    try:
        if ipaddress.ip_address(ip_address):
            return True
    except ValueError:
        return "Invalid IP"

def port_validator(starting_port,ending_port):
    try:
        if (starting_port < 0) or (ending_port < 0 ) or starting_port > ending_port :
            return "Invalid Ports"
        else:
            return True
    except TypeError:
        return "Invalid Ports"

def time_validator(timeout):
    try:
        if timeout < 0.0:
            return "Invalid Timeout"
        else:
            return True
    except TypeError:
        return "Invalid timeout"

def worker_validator(workers):
    try:
        if workers < 0:
            return "Invalid no.of workers"
        else:
            return True
    except TypeError:
        return "Invalid no.of workers"


