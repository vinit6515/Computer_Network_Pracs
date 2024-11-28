import random , time
def send_frame(frame_number):
    print(f"Sending frame {frame_number} .")
    return random.choice(['True', 'False'])
def recieve_frame(base):
    time.sleep(1)
    return  random.choice([None,base])
window_size= int(input("Enter the window size : "))
total_frames= int (input("Enter the total number of frames: "))
base = 0
next_frame = 0
ack = -1
while base < total_frames:
    while next_frame < base + window_size and next_frame<total_frames:
        if send_frame(next_frame):
            print(f"Frame {next_frame} is sent successfully.")
        else:
            print(f"Frame {next_frame} is lost.")
        next_frame +=1
    ack = recieve_frame(base)
    if ack is not None:
        print(f"ACK for frame {base} recieved.")
        base = ack + 1
    else:
        print("ACK not recieved retransmitting from the base frame.")
        next_frame = base