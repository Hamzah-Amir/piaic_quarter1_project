# Assignment no 4: Write a program that prints out the calls for a spaceship that is about to launch. Countdown 10 to 1 and then LIFTOFF!

def liftoff():
    
    num = []
    # using step size technique in for loop to reverse yhe countdown

    for i in range(10, 0, -1):
        
        num.append(i)
            
    print(*num,end=" ")
    print("LIFTOFF!")

if __name__ == "__main__":
    liftoff()