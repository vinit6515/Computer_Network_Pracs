import socket, random ,time
HOST='127.0.0.1'
PORT=5001
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
while True:
    message = input('Enter the message you want to send : ')
    if message == 'end':
        break
    ack_recieved = False
    while ack_recieved == False:
        client_socket.sendall(message.encode())
        time.sleep(2)
        choice = client_socket.recv(1024)
        if choice.decode()=='0':
            print("ACK recieved")
            ack_recieved=True
        elif choice.decode()=='1':
            print("ACK lost.")
            ack_recieved=False
        else:
            print("ACK lost due to timeout , Retransmitting the frame......")

