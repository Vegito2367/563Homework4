import sys
from socket import *
import datetime
def main():
    if(len(sys.argv)>3):
        print("Only 2 arguments allowed")
    
    serverIP= sys.argv[1]
    serverPort = int(sys.argv[2])
    serverAddress = (serverIP,serverPort)
    clientSocket = socket(AF_INET,SOCK_DGRAM)
    clientSocket.sendto("test".encode(),serverAddress)
    sentTimestamp = datetime.datetime.now()
    print("Requested a timestamp from client!")
    receivepayload,serverAddress = clientSocket.recvfrom(2048)
    receiveTime = datetime.datetime.now()
    receivePayload = receivepayload.decode()
    serverUTCTime,servermsTime = receivePayload.split("Z")
    clientTime = datetime.datetime.now()
    clientTimeStamp = clientTime.timestamp()*1000
    clientUTC = str(clientTime).replace(" ","T")

    print("Received Time Stamp:",serverUTCTime)
    print("Local client time:",clientUTC)
    print("Latency:", clientTimeStamp - float(servermsTime))
    print("RTT:",(receiveTime.timestamp()-sentTimestamp.timestamp())*1000)
    clientSocket.close()

if __name__ == "__main__":
    main()