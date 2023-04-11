from socket import *
import threading
import random

def handle_client(connectionSocket, clientAddress):
    message = connectionSocket.recv(8000).decode()
    newMessage = message.split()
    clientNumber  = int(newMessage[-1])
    if  clientNumber > 100 or  clientNumber < 1:
        connectionSocket.close()
        return
    # client jerry asd 1 [jerry,asd]
    nameOfClient = newMessage[1:3]
    print("name of client:",*nameOfClient,sep=" ")
    print("server's name:" + " " +name)
    print ("client number:" , clientNumber)
    serverNumber = random.randint(1,100)
    print ("server generated number:" ,serverNumber )
    print ("sum:" , clientNumber +serverNumber  )
    modifiedMessage = name +" "+ str(serverNumber)
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()

serverPort = 7000
name = "server of BDFJ"
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5) # Maximum number of queued connections should be 7

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Received connection from:", addr)
    clientThread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    clientThread.start()