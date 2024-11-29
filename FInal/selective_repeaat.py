import random , time
def send_frame(frame):
    print(f"Sending frame {frame}")
    return random.choice([True,False])
def recieve_frame(base):
    time.sleep(2)
    return random.choice([None,base])
window_size = int(input("Enter the window size :"))
total_frame = int(input("Enter the total number of frames : "))
base = 0
next_frame =0
ack = -1
while base < total_frame:
    while next_frame < base + window_size and next_frame < total_frame:
        if send_frame(next_frame):
            print(f"Frame {next_frame} is sent successfully .")
        else:
            print(f"Frame {next_frame} is lost.")
        next_frame= next_frame+1
    ack = recieve_frame(base)
    if ack is not None:
        print(f"ACK for frame {ack} recieved .")
        base = ack + 1
    else:
        print("ACK lost due to timeout")
        