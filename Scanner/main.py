from port_scanner import tcp_scanner_port
import sys

print("Default IP - 127.0.0.1")
ip = input("Enter ip or url you want to scan:-")
if not ip:
    ip = "127.0.0.1"
print("Default Port:-1")
start_port = input("Enter the port no.from where you wanna start scanning:-")
if not start_port:
    start_port = 1
else:
    start_port = int(start_port)
print("Default Port- 65535")
end_port = input("Enter the port at which you wanna stop scanning:-")
if not end_port:
    end_port = 65535 
else:
    end_port = int(end_port)


def main():
    while True:
        if end_port < start_port:
            print("Invalid port order start port must be less than end port")
        else:
            print("1.Scan the IP\n2.Exit.")
            usr = input("Choose a option:-")
            if usr == "1":
                worker = input("Choose no.of workers you wanna do the scanning:-")
                tcp_scanner_port(worker,ip,start_port,end_port)
            elif usr =="2":
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid option")
            

main()
        
