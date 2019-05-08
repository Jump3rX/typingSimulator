import sys,time

def typing(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.2)
typing("Hello i am a function that simulates typing...pleased to meet you.")