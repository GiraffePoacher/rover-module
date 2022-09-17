import socket
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
    connection = True
    while connection:
        msg = conn.recv(128).decode(FORMAT) #128bytes is way more than neccessary, can optimize but shouldn't cause problems
        with open('readme.txt', 'a') as f:
            f.write(msg)
        if(len(msg) > 0):
            print(msg)
    conn.close()

def start():
    server.listen()
    print("Server is listening...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("ACTIVE CONNECTIONS: " + str(threading.active_count() - 1))

print("Server initialized...")
start()