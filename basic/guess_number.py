# Assignment no 2: Write a program that generates a random number and then guide you to guess it

from random import randint as r
def main():

    number = r(1,99)
    counter = 1

    while True:
        
        try:

            print(f"Guess no: {counter}! ") # printing no of try user is at
            user_guess = int(input("Enter your guess: "))
            counter +=1
            
            # Guiding user that if the number is lower of higher
            if user_guess < number: # 
                print("Your guess is lower then number ") 
            
            elif user_guess > number:
                print("Your guess is greater then number ")
            
            else:
                # A message that will tell user that he guessed the number correctly in how many tries and also displays number
                print(f"Congratulations! you guessed correctly the number was {number} in {counter} Tries")
                break
        
        except Exception as e:
            print(f"An error occured! {e}")

if __name__ == "__main__":
    main()