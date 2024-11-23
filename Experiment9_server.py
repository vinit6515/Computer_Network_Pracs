import socket
import random
import time

# Receiver (Server) Function for Stop-and-Wait Protocol
def receiver():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind to an address and port
    server_socket.bind(('localhost', 12345))
    
    expected_frame = 0

    print("Receiver is ready and waiting for frames...")

    while True:
        # Receive a frame
        frame, client_address = server_socket.recvfrom(1024)
        frame = frame.decode()

        print(f"Received Frame {frame}")

        # Simulate acknowledgment loss or delay
        if random.random() > 0.2:  # 80% chance to send acknowledgment
            if int(frame) == expected_frame:
                time.sleep(1)  # Simulate processing delay
                server_socket.sendto(frame.encode(), client_address)
                print(f"Sent Acknowledgment for Frame {frame}")
                expected_frame += 1
        else:
            print(f"Lost Acknowledgment for Frame {frame}")

        if expected_frame >= 5:
            break

    # Close the socket connection
    server_socket.close()

# Run the receiver
if __name__ == "__main__":
    receiver()
