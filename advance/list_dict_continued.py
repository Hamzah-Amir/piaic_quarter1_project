# Part 3: Slicing List Project 3 continued

num = [5,6,648,13,364]

def list_slice():
    
    start_index = int(input("Enter starting index: "))
    last_index = int(input("Enter last index: "))

    if (start_index or last_index) <= len(num):
        updated_num = num[start_index:last_index]
        print(updated_num)
    else:
        print("Index is out of range! ")

list_slice()

# Assignment no 3 (Final Task): Create a game That prompt user to access modify or slice list 
# and prints the updated list

def pop_data():
     data = [2023, 6.28, True, None, "PIAIC", "Hamza", False]
     
     try: 
        index = int(input("Enter index you want to pop: "))
        data.pop(index)
     except IndexError:
         print("Index is out oof range!")

def list_game():
    
    data = [2023, 6.28, True, None, "PIAIC", "Hamza", False]

    choice = input("Enter what do you want to do with list: (access, modify, or slice)").lower()

    if choice == "access":
            print(data)

    elif choice == "modify":
        modify_option = input("What do you want to do with list: (pop,append,remove) ").lower()
        if modify_option == 'pop':
            pop_data()


