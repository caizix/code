import socket

# 实例的初始化
client = socket.socket()
# 定义绑定ip和port
ip_port = ("127.0.0.1", 8888)
# 连接主机
client.connect(ip_port)
# 接收主机的信息
data = client.recv(1024)
# 打印数据
print(data.decode())
