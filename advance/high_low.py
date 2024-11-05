# Assignment no 1: Create a game name high low.

from random import randint

def main():

    rounds = int(input("Enter No of rounds you want to play: "))    
    
    round = 1

    user_score = 0
    computer_score = 0 
    
    print("Welcome To The Game High Low!")
    print("--------------------------------")

    while round <= rounds: 
        computer_num = randint(1,100) # Generating random numbers for both user and computer
        user_num = randint(1,100)
                             
        print(f"\nRound no {round} starts \nHigh \nLow") # printing round no

        print(f"Your number is: {user_num}" )

        user_guess = input("Do you think your number is higher or lower then computer's number: ").lower() # Taking input from user

        # Handling expected error in user's input
    
        if (user_guess != "higher") and (user_guess != "lower"):
            print("You entered an invalid option, please enter \"higher\" or \"lower\" only")
            continue
            
        # Defining winning conditions of round

        if user_guess == 'higher' and user_num > computer_num:
            print(f"You guessed correctly, Computer's number was {computer_num}")
            user_score += 1
            print(f"Your score is {user_score} and Computer's score is {computer_score}.")
        
        elif user_guess == "lower" and user_num < computer_num:
            print(f"You guessed correctly, Computer's number was {computer_num}")
            user_score += 1
            print(f"Your score is {user_score} and Computer's score is {computer_score}.")
        
        elif user_guess == "higher" and user_num < computer_num:
            print(f"That is incorrect, Computer's number was {computer_num}")
            computer_score += 1
            print(f"Computer's score is {computer_score} and User's score is {user_score}")
        
        elif user_guess == "lower" and user_num > computer_num:
            print(f"That is incorrect, Computer's number was {computer_num}")
            computer_score += 1
            print(f"Computer's score is {computer_score} and User's score is {user_score}")

        round +=1 # Incrementing round by 1 in each iteration
   
    # Defining condition for overall winner of game
    
    if user_score > computer_score:
        print("\nCongratulations! You Have Won the Game")
        print(f"\nYou won {user_score} rounds and Computer won {computer_score} Rounds")
    else:
        print("Hard Luck! Computer Won")

if __name__ == "__main__":
    main()