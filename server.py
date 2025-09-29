import socket
import threading

HEADER=64
PORT=8080
SERVER=socket.gethostbyname(socket.gethostname())
ADDR= (SERVER,PORT)
FORMAT="utf-8"
DISCONNECT_MESSAGE = "!Disconnect"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


def handel_client (conn, addr) :
   print(f"[New Connection] {addr} Connected")
   connected = True
   while connected :
       msg_len=conn.recv(HEADER).decode(FORMAT)
       msg_len=int(msg_len)
       msg=conn.recv(msg_len).decode(FORMAT)
       if msg == DISCONNECT_MESSAGE :
           connected = False
       print(f"[{addr}]  {msg}")
   conn.close()
    
   
def start() :

    server.listen() 
    while True :
        print(f"[Listening] Server is listening on {SERVER}")
        conn , addr = server.accept()
        thread = threading.Thread(target=handel_client,args=(conn,addr))
        thread.start()
        print(f"[Active Connection] {threading.active_Count()} -1")

        



print("[STARTING] Server is Sarting...")
start()
