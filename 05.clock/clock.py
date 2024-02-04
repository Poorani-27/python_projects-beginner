import time 
print("press ctrl+c to stop ")
def clock():
    while True:
        current_time = time.localtime()
        formatted_time = time.strftime("%H Hours %M Minutes %S Seconds", current_time)
        print(formatted_time, end="\r")
        time.sleep(1)

if __name__ == "__main__":
    try:
        clock()
    except KeyboardInterrupt:
        print("\n\tClock stopped")
