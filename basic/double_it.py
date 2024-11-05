# Assignment no 1: Write a program that doubles a number until the value get bigger then hundred

def double():
    num = int(input("Enter your number: "))

    curr_value = num

    while curr_value <= 100:
       
        curr_value = curr_value * 2  
        print(curr_value*2)
        
if __name__ == '__main__':
    double()