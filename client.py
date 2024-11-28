import socket , time
HOST='127.0.0.1'
PORT=5001
client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
while True:
    message_to_be_sent= input("Enter the data you want to send: ")
    if message_to_be_sent=='end':
        break
    ack_recieved=False
    while not ack_recieved:
        client_socket.sendall(message_to_be_sent.encode())
        time.sleep(2)
        choice= client_socket.recv(1024)
        if choice.decode()=='0':
            print("Frame Sent Successfully and ACK recieved.")
            ack_recieved=True
        elif choice.decode()=='1':
            print("Frame Lost . Retransmitting Again .......")
            ack_recieved=False
        else:
            print("ACK not Recieved in Time . Retansmitting frame again.")
            continue
         
print("Connection Ended Successfully.")
client_socket.close()