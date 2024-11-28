import socket , random , time 
HOST='127.0.0.1'
PORT=5001
socket_server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_server.bind((HOST,PORT))
socket_server.listen()
print('Connection is successfully established.')
conn, addr = socket_server.accept()
print(f"Connected by address : {addr}")
while True:
    message= conn.recv(1024)
    if not message:
        break
    print(f"Recieved Data : {message.decode()}")
    choice = random.choice(['0','1','2']) # 0 -> for Frame Not sent successfully , 1 -> Frame Recieved , 2-> Timeout occured
    conn.sendall(choice.encode())