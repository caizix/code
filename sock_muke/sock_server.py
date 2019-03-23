# -*- coding:UTF-8 -*-
import random
import socket

sk = socket.socket()

ip_port = ("127.0.0.1", 8888)

sk.bind(ip_port)

sk.listen(5)

while True:

    print("zhengzaijieshou>>>>")

    conn, address = sk.accept()

    msg = "连接成功！"

    conn.send(msg.encode())
    while True:
        data = conn.recv(1024)
        print(data.decode())
        if data == b'exit':
            break
        conn.send(data)
        conn.send(str(random.randint(1, 1000)).encode())
    conn.close()
