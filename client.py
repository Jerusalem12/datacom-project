from socket import *

serverName = '127.0.0.1' # replace this with the IP address of the server PC
serverPort = 7000
clientName = input("Enter your full name:")
client_string = "client" + " " + clientName
clientInteger = int(input('input an integer from 1 to 100:'))

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

requestMessage =client_string +" "+ str(clientInteger)
clientSocket.send(requestMessage.encode())

replyMessage = clientSocket.recv(8000).decode()
if replyMessage == "":
    print("the server is closed")
    clientSocket.close()
    exit()
    
newMessage = replyMessage.split()
newInteger = int(newMessage[-1])

print('From Server:', replyMessage)
print("client:", requestMessage)
print("sum:",newInteger+clientInteger)
clientSocket.close()