import socket as s
import sys
import datetime
def main():
    if(len(sys.argv)>3):
        print("Only 2 arguments allowed")
    
    serverIP= sys.argv[1]
    serverPort = int(sys.argv[2])
    serverAddress = (serverIP,serverPort)
    clientSocket = s.socket(s.AF_INET,s.SOCK_STREAM)
    clientSocket.connect(serverAddress)
    clientSocket.send("giveTime".encode())
    sentTimestamp = datetime.datetime.now()
    print("Requested a timestamp from client!")
    receivePayload = clientSocket.recv(1024).decode()
    receiveTime = datetime.datetime.now()
    serverUTCTime,servermsTime = receivePayload.split("Z")
    clientTime = datetime.datetime.now()
    clientTimeStamp = clientTime.timestamp()*1000
    clientUTC = str(clientTime).replace(" ","T")

    print("Received Time Stamp:",serverUTCTime)
    print("Local client time:",clientUTC)
    print("Latency:", abs(clientTimeStamp - float(servermsTime)))
    print("RTT:",(receiveTime.timestamp()-sentTimestamp.timestamp())*1000)


    clientSocket.close()


if __name__ == "__main__":
    main()
