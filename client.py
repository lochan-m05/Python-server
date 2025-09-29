import socket
import threading


HEADER=64
PORT=8080
FORMAT="utf-8"
DISCONNECT_MESSAGE = "!Disconnect"
SERVER='192.168.1.36'
ADDR= (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
