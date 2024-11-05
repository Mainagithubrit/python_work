import signal
import time
import sys

def termination_handler(signum, frame):
    print("termination request")
    print("Cleanup...")
    sys.exit()

signal.signal(signal.SIGINT, termination_handler)
while True:
    print("Hey")
    time.sleep(1)
