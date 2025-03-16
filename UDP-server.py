from socket import *
import sys
import signal
import datetime
def main():
    if(len(sys.argv)>2):
        print("Only one argument is accepted.")
        exit(0)

    signal.signal(signal.SIGINT,killhandle)
    serverPort = int(sys.argv[1])

    serverSocket = socket(AF_INET,SOCK_DGRAM)
    serverSocket.bind(('',serverPort))
    print("UDP server is ready to receive! Listening on port:",serverPort)
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        if(message):
            print("Received UDP packet from client!")
        currentTime = datetime.datetime.now()
        curTimeStamp = currentTime.timestamp() * 1000
        currentTime = str(currentTime).replace(' ',"T")
        currentTime+="Z"
        currentTime+=str(curTimeStamp)
        serverSocket.sendto(currentTime.encode(),clientAddress)
        print("Sending timestamp back to client!")
        serverSocket.close()
        
    

def killhandle(sig,frame):
    print("\nClosing server....")
    exit(0)

if __name__ == "__main__":
    main()
