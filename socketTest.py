import socket 
import time

HEARDSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),1234))
s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address} has beem established")
    
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEARDSIZE}}'+msg
    
    clientSocket.send(bytes(msg,"utf-8"))
    while True:
        time.sleep(3)
        msg = f"The time is: {time.time()}"
        msg = f'{len(msg):<{HEARDSIZE}}'+msg 
        clientSocket.send(bytes(msg, "utf-8"))