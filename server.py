from http import server
import socket
from sqlite3 import connect
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DC_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #using TCP because why not
server.bind(ADDR)

def handle_client(conn,addr):
    print("New Client: " + str(addr))
    connected = True
    while connected:
        msg = conn.recv(1024).decode(FORMAT) #1kb is way more than neccessary, can optimize but shouldn't cause problems
        if msg == DC_MSG:
            connected = False
        print(msg)
    conn.close()

def start():
    server.listen()
    print(f"Server is listening: {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("Active Connections = " + str(threading.active_count()-1)) #sub 1 because start thread counts as 1 thread

print("Server initialized...")
start()