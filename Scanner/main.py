from port_scanner import tcp_scanner_port
import sys
import argparse


parser = argparse.ArgumentParser(prog="main",description="Main program of port scanner")
parser.add_argument('-i',"--ip",help="IP adress to scan",default="152.58.132.106")
parser.add_argument('-s',"--start",help="Starting Port",type=int,default = 1)
parser.add_argument('-e',"--end",help="Ending Port",type=int,default=65535)
parser.add_argument('-w',"--worker",help="No.of Workers",type=int,default=20)

args = parser.parse_args()

def main():
    while True:
        print("1.Scan the IP\n2.Exit.")
        usr = input("Choose a option:-")
        if usr == "1":
            ip_address = args.ip
            starting_port = args.start
            ending_port = args.end
            workers = args.worker
            tcp_scanner_port( ip_address , starting_port , ending_port , workers)
        elif usr =="2":
            print("Exiting...")
            sys.exit()
        else:
    
            print("Invalid option")
            

main()

        
