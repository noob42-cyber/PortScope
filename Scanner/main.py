lazy import argparse
lazy from port_scanner import tcp_scanner_port
lazy from validator import ip_validator,port_validator,time_validator,worker_validator
lazy import time
# Adding of arguments by argparse

parser = argparse.ArgumentParser(prog="main",description="Main program of port scanner")
parser.add_argument('-i',"--ip",help="IP adress to scan",default="127.0.0.1")
parser.add_argument('-s',"--start",help="Starting Port",type=int,default = 1)
parser.add_argument('-e',"--end",help="Ending Port",type=int,default=65535)
parser.add_argument('-c',"--count",help="Thread Count",type=int,default=20)
parser.add_argument('-t',"--time",help = "Timeout for thread",type = float,default=3.0)
parser.add_argument('-w',"--web",help = "Scan the website url",type = str)

args = parser.parse_args()

# Main Function of Scanner

def main():
    validations = [ 
      ip_validator(args.ip),
      port_validator(args.start , args.end),
      worker_validator(args.count),
      time_validator(args.time)
      ]
    if all(result is True for result in validations):
        start = time.time()
        result = tcp_scanner_port( args.ip , args.start , args.end , args.count,args.time)
        elapse = int(time.time()-start)*1000
        print(f" Target: {args.ip} \n Range : {args.start}-{args.end} \n Time taken : {elapse}ms ")
        for i in range (len(result)):
            print(result[i])

    else:
        for result in validations:
            if result is not True:
                print(result)
                break

            

if __name__ == "__main__":
    main()