import socket, random ,time
HOST='127.0.0.1'
PORT=5001
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen()
print("Server is reaady ..........")
conn , addr = server_socket.accept()
print(f"Server is connected with address : {addr}")
while True:
    recieved_data = conn.recv(1024)
    if recieved_data is None:
        break
    print(f"Recieved Data : {recieved_data.decode()}")
    choice = random.choice(['0','1','2'])
    conn.sendall(choice.encode())
