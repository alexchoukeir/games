import time
import signal

running = True

def signal_handler(sig, frame):
    global running
    print("Received signal.")
    running = False

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    print("Worker started. Waiting for tasks...")
    while running:
        time.sleep(1)
    print("Worker stopped.")
