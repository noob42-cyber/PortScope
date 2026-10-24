lazy import argparse


# Adding of arguments by argparse

parser = argparse.ArgumentParser(prog="main",description="Main program of port scanner")
parser.add_argument('-i',"--ip",help="IP adress to scan",default="127.0.0.1")
parser.add_argument('-s',"--start",help="Starting Port",type=int,default = 1)
parser.add_argument('-e',"--end",help="Ending Port",type=int,default=100)
parser.add_argument('-c',"--count",help="Thread Count",type=int,default=20)
parser.add_argument('-t',"--time",help = "Timeout for thread",type = float,default=1.0)

args = parser.parse_args()

# Main Function of Scanner

def main():
    from port_scanner import tcp_scanner_port
    ip_address = args.ip
    starting_port = args.start
    ending_port = args.end
    workers = args.count
    timeout = args.time
    result = tcp_scanner_port( ip_address , starting_port , ending_port , workers,timeout)
    elapse = int(result["elapsed"])*1000
    print(f" Target: {ip_address} \n Range : {starting_port}-{ending_port} \n Time taken : {elapse}ms ")
            

if __name__ == "__main__":
    main()


        

