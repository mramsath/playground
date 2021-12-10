import socket
import sys, getopt
import time

ip=''
port=2200
traceFilePath='OrthoVision.txt'
BUFFER_SIZE = 2048

argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv,"h:i:p:f", ["ip=","port=", "file="])
except getopt.GetoptError:
    print ("TCPClient.py -i <ip> -p <port> -f file")
    sys.exit(2)

for opt, arg in opts:
    if opt == '-h':
        print ('TCPClient.py -i <ip> -p <port> -f file')
        sys.exit()
    elif opt in ("-i", "--ip"):
        ip = arg
    elif opt in ("-o", "--port"):
        port = arg
    elif opt in ("-f", "--file"):
        traceFilePath ='OrthoVision.txt'    
print ("IP : "+ ip)
print ("Port : "+ str(port))
print ("Trace File : "+ traceFilePath)

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (ip, port)
print('connecting to  %s port %s' % server_address)
s.connect(server_address)
#s.send("Hello server!".encode('utf-8'))

with open(traceFilePath, 'r') as file:
    print ('file opened and reading...')
    for line in file:
        line=line.strip();
        print('-> ' + line.rstrip())
        line=line.encode('utf-8').hex();
        #print(line)
        if line not in ['05', '04']:
            #data ='02'+line+'0D03'+'CC'.encode('utf-8').hex()+'0D0A';
            data =line+'0A';
        else:
            data=line;
        #print(bytes.fromhex(data))
        #print('sending data...')
        s.send(bytes.fromhex(data))
        
        #data = s.recv(BUFFER_SIZE)
        #print('<- ', repr(data))
        time.sleep(0.2);

file.close()
 