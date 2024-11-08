# Assignment no 5: Write a program to print 10 random numbers between 1 to 10

from random import randint

rand_num = []

def random_num():
    
    i = 0

    while i != 10:
        
        # Generating random number until value of i is less then 10
        value = randint(1,100)

        i += 1 # Increasing value of i by 1 in each iteration
        
        rand_num.append(value)

        
    print(*rand_num,end=" " )


if __name__ == "__main__":
    random_num()