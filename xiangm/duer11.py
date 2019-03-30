import socket
# HOST = "127.0.0.1"
HOST = "47.104.248.127"
PORT = 65533
def doConnect(host, port):
    duerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        duerSocket.connect((host, port))
    except:
        pass
    return duerSocket


while True:
    try:
        duer = doConnect(HOST, PORT)
        while True:
            rev_msg = duer.recv(1024)

            if len(rev_msg) == 0:
                continue
            else:
                # Here maybe add serial communication code

                print(eval(rev_msg))
                break
    except:
        pass
        continue
