import time 

def timer(duration):
    print(f"Timer set for {duration} seconds ")
    time.sleep(duration)
    print('''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Time's up !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!''')

if __name__ == "__main__":
    try :
        duration = int(input("Enter Seconds : "))
        timer(duration)
    except(ValueError):
        print("Invalid ! Please enter a Number")