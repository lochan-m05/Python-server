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
    server.listen() 
    while True :
        print("[Listening] Server is listenign ")
        conn , addr = server.accept()
        thread = threading.Thread(target=handel_client,args=(conn,addr))
        thread.start()
        



print("[STARTING] Server is Sarting...")
start()
