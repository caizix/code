import socket

# 定义实例
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_port = ("127.0.0.1", 8888)
# 循环输入
while True:
    # 输入发送信息
    msg_input = input("请输入发送的信息：")
    # 退出循环
    if msg_input == "exit":
        break
    # 数据发送
    sk.sendto(msg_input.encode(), ip_port)
sk.close()
