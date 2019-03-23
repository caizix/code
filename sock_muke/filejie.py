import socket

# 实例化
sk = socket.socket()
# 定义连接ip和port
ip_port = ("127.0.0.1", 9999)
sk.bind(ip_port)
sk.listen(5)
while True:
    conn, address = sk.accept()
    while True:
        with open("file", "ab") as f:
            data = conn.recv(1024)
            if data == b'quit':
                break
            f.write(data)
        conn.send('success'.encode())
    print('文件接受完成')
sk.close()
