import socket

HEARDSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),1234))

while True:

    full_msg = ''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"New Message length: {msg[:HEARDSIZE]}")
            msglen = int(msg[:HEARDSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg)-HEARDSIZE == msglen:
            print("Full msg recvd")
            print(full_msg[HEARDSIZE:])
            new_msg = True
            full_msg = ''

    print(full_msg) 