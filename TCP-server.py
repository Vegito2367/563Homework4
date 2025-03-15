import sys
import socket as s
import signal
import datetime
def main():
    if(len(sys.argv) > 2):
        print("Only one argument is allowed")
        return
    
    args = sys.argv[1:]
    port = int(args[0])
    welcomeSocket = s.socket(s.AF_INET,s.SOCK_STREAM)
    welcomeSocket.bind(('',port))
    welcomeSocket.listen(1)
    print("TCP Server is ready to receive! Listening on port:",port)
    signal.signal(signal.SIGINT,killhandle)
    while True:
        clientSocket, clientAddress = welcomeSocket.accept()
        payload = clientSocket.recv(1024).decode()
        if(payload):
            print("Received TCP packet from client!")
        currentTime = datetime.datetime.now()
        curTimeStamp = currentTime.timestamp() * 1000
        currentTime = str(currentTime).replace(' ',"T")
        currentTime+="Z"
        currentTime+=str(curTimeStamp)
        print("Sending timestamp back to client!")
        clientSocket.send(currentTime.encode())

        clientSocket.close()

def killhandle(sig,frame):
    print("\nClosing server....")
    exit(0)




if __name__ == "__main__":
    main()