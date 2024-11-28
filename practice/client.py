import socket , random , time
HOST='127.0.0.1'
PORT=5001
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
while True:
    message= input("Enter your message: ")
    if message== "end":
        break
    ack_recieved= False
    while not ack_recieved :
        client_socket.sendall(message.encode())
        time.sleep(2)
        data = client_socket.recv(1024)
        print(data.decode())
        if data.decode()== '2':
            print(f"ACK not recieved retransmitting the frame.")
            continue
        elif data.decode()=='1':
            print(f"Frame lost")
            ack_recieved=False
        else:
            print("ACK recieved")
            ack_recieved=True
print("Connection Ended")
client_socket.close()