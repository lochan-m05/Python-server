import socket
import threading

HEADER=64
PORT=8080
SERVER=socket.gethostbyname(socket.gethostname())
ADDR= (SERVER,PORT)
FORMAT="utf-8"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


def handel_client (conn, addr) :
   print(f"[New Connection] {addr} Connected")
   connected = True
   while connected :
       msg_len=conn.recv(HEADER).decode(FORMAT)
       msg_len=int(msg_len)
       msg=conn.recv(msg_len).decode(FORMAT)
       print(f"[{addr}]  {msg}")
       
   

   
def start() :

    server.listen() 
    while True :
        print("[Listening] Server is listening ")
        conn , addr = server.accept()
        thread = threading.Thread(target=handel_client,args=(conn,addr))
        thread.start()
        print(f"[Active Connection] {threading.active_Count()} -1")

        



print("[STARTING] Server is Sarting...")
start()
