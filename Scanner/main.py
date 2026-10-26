lazy import argparse
lazy from port_scanner import tcp_scanner_port
lazy from validator import ip_validator,port_validator,time_validator,worker_validator
# Adding of arguments by argparse

parser = argparse.ArgumentParser(prog="main",description="Main program of port scanner")
parser.add_argument('-i',"--ip",help="IP adress to scan",default="127.0.0.1")
parser.add_argument('-s',"--start",help="Starting Port",type=int,default = 1)
parser.add_argument('-e',"--end",help="Ending Port",type=int,default=65535)
parser.add_argument('-c',"--count",help="Thread Count",type=int,default=20)
parser.add_argument('-t',"--time",help = "Timeout for thread",type = float,default=1.0)

args = parser.parse_args()

# Main Function of Scanner

def main():
    validate_ip = ip_validator(args.ip)
    validate_port = port_validator(args.start , args.end)
    validate_worker = worker_validator(args.count)
    validate_timeout = time_validator(args.time)
    if validate_ip != True:
        print(validate_ip)
    elif validate_port != True:
        print(validate_port)
    elif validate_timeout != True:
        print(validate_timeout)
    elif validate_worker != True:
        print(validate_worker)
    else:
        result = tcp_scanner_port( args.ip , args.start , args.end , args.count,args.time)
        elapse = int(result["elapsed"])*1000
        print(f" Target: {args.ip} \n Range : {args.start}-{args.end} \n Time taken : {elapse}ms ")
            

if __name__ == "__main__":
    main()