import socket
import threading

PORT=8080
SERVER=socket.gethostbyname(socket.gethostname())
ADDR= (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


def handel_client() :
    pass


def start() :
    pass 


print("[STARTING] Server is Sarting...")
start()
