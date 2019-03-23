import random
import socketserver


# 定义一个类
class MyServer(socketserver.BaseRequestHandler):
    # 如果handle方法出现报错，
    def setup(self):
        pass

    def handle(self):
        # 定义连接变量
        conn = self.request
        # 发送消息定义
        msg = "hello world!"
        # 消息发送
        conn.send(msg.encode())
        # 进入循环，不断接受客户端的消息
        while True:
            # 接受客户端消息
            data = conn.recv(1024)
            # 打印消息
            print(data.decode())
            if data == b'exit':
                break
            conn.send(data)
            conn.send(str(random.randint(1, 1000)).encode())
        conn.close()

    def finish(self):
        pass


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8888), MyServer)
    # 开启异步多线程
    server.serve_forever()
