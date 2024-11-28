import random, time , socket
HOST='127.0.0.1'
PORT=5001
server_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
server_socket.listen()
print("Connection between server and client is established")
conn , address = server_socket.accept()
print(F"Connected by address :{address}")
while True:
    message=conn.recv(1024)
    if not message:
        break
    print(f"Recieved data : {message.decode()}")
    message_to_be_sent = random.choice(['0','1','2']) # 0-> frame milgaya , #1-> Frame lost , #2-> frame mil gaya but acknowlegement not recieved in time
    conn.sendall(message_to_be_sent.encode())

