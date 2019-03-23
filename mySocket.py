import socket

mySocket = socket.socket()
HOST = "103.46.128.49"
PORT = 58888

mySocket.bind((HOST, PORT))
mySocket.listen(10)
while True:
    conn, address = mySocket.accept()
    print(address)
    data = conn.recv(1024)
    jsonData = eval(data)
    for key, value in jsonData.items():
        print(key)
        print(value)
