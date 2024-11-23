## GO-N-BACK ARQ
import random
import time
window_size= int(input("Number of frames that can be sent before needing an ACK:"))
total_frames= int(input ("Total number of frames to send:"))
timeout= int(input("Timeout in seconds:"))
# Simulate sending a frame
def send_frame(frame_number):
    print(f"Sending frame {frame_number}")
    return random.choice([True, False])  # Simulate a frame loss (False) or success (True)

# Simulate receiving an ACK
def receive_ack(expected_frame):
    time.sleep(1)  # Simulate delay
    return random.choice([expected_frame, None])  # Simulate ACK loss (None) or success (expected_frame)

# Go-Back-N ARQ simulation
def go_back_n_arq():
    base = 0  # First frame in the window
    next_frame_to_send = 0  # Next frame to send
    ack_received = -1  # Last acknowledged frame

    while base < total_frames:
        while next_frame_to_send < base + window_size and next_frame_to_send < total_frames:
            if send_frame(next_frame_to_send):
                print(f"Frame {next_frame_to_send} sent successfully.")
            else:
                print(f"Frame {next_frame_to_send} lost.")
            next_frame_to_send += 1

        ack = receive_ack(base)
        if ack is not None:
            print(f"Received ACK for frame {ack}")
            base = ack + 1
        else:
            print("ACK lost or timeout occurred, resending from base frame")
            next_frame_to_send = base  # Go back to the base frame and resend
if __name__ == "__main__":
    go_back_n_arq()
