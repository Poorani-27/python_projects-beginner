import random 
print("\n\t\tWelcome ! To Play STONE-PAPER-SCISSORS")

def play():
    print("\nRules : \n1.Stone covers paper\n2.Scissors cuts the paper\n3stone breaks the scissors")
    print("\nAre you ready to play")
    answer = input("Enter Yes or No :").lower()
    answer = answer.strip(" ")
    if answer == "yes" :
        print("Let's begin")
    else :
        print ("Exiting Game ")
        return 
    user_count=0
    machine_count = 0
    while True :
        a=["stone", "paper","scissors"]
        user_input = input("Enter(Stone--paper--scissor--q to quit) : ").lower()
        user_input=user_input.strip(" ")
        machine_input = random.choice(a)
       
        if user_input not in ["stone" ,"paper", "scissors", "q"]:
            print("Invalid input -- stone or paper or scissors --")
            continue
        if user_input == "q":
            print("Exiting Game")
            break
        print("machine input : {}".format(machine_input))
        if machine_input==user_input :
                print("No Points ! It's a tie")
        elif (user_input == "stone" and machine_input == a[2]) or (user_input == "paper" and machine_input == a[0]) or ( user_input == "scissors" and machine_input == a[1]):
                print ("You Win This round ")
                user_count +=1
        else :
                print("you lose this round")
                machine_count+=1
        print("machine scored : {}\t  you scored : {} ".format(machine_count,user_count))
        
        
        

if __name__ =="__main__":
    try :
        game =play()
    except Exception as e :
        print("Something went Wrong {}".format(e))
        