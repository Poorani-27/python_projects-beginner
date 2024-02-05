import random

def play():
    user_input = input("\nAre You Ready To Play? ").lower()
    if user_input == "yes" or user_input == "y":
        print("\nWelcome TO Number Guessing Game")
        number = random.randint(1, 100)
        user_count = 0
        machine_count = 0
        while True:
            guess = random.randint(1, 100)
            user_guess = input("Enter The Number you Guessed Between 1 TO 100 (or 'q' to stop): ")
            
            if user_guess.lower() == "q" or user_guess.lower() == "quit":
                print("Exiting game")
                break

            if user_guess.isdigit():
                user_guess = int(user_guess)
                if 1 <= user_guess <= 100:
                    if user_guess == guess:
                        user_count += 1
                        print("Correct! You scored a point.")
                    else:
                        machine_count += 1
                        print(f"Wrong! Machine scored a point. Machine's guess was {guess}.")
                else:
                    print("Please enter a valid number between 1 and 100.")
            else:
                print("Please enter a valid number.")
        
        print(f"My Score: {machine_count}\tYour Score: {user_count}")

if __name__ == "__main__":
    try:
        game = play()
    except Exception as e:
        print(f"\nSomething went wrong! Try Again\nERROR: {e}\n\n")
