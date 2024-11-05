# List Project 3 continued

# Assignment no 3 (Final Task): Create a game That prompt user to access modify or slice list 
# and prints the updated list


# Firstly defining different modification  functions to keep main game logic simple and read able

def pop_data():
     data = [2023, 6.28, True, None, "PIAIC", "Hamza", False]
     
     try: 
        index = int(input("Enter index you want to pop: "))
        data.pop(index)
        print(data)
     except IndexError:
         print("Index is out oof range!")

def append_data():
    try:    
        data = [2023, 6.28, True, None, "PIAIC", "Hamza", False]
        new_data = input("Enter data you want to append: ")

        data.append(new_data)
        print(data)
    except Exception as e:
        print(e)
    

def remove_data():

    data = [2023, 6.28, True, None, "PIAIC", "Hamza", False]
    index_data = int(input("Enter the index number you want to remove: "))

    data.remove(index_data)
    print(data)
    if index_data < len(data):
        return "Index is out of range!"

# Main logic of game

def list_game():
    
    data = [2023, 6.28, True, None, "PIAIC", "Hamza", False]

    choice = input("Enter what do you want to do with list: (access, modify, or exit): ").lower()
    
    # Giving choices to user
    
    if choice == "access":
            print(data)

    elif choice == "modify":
                
        modify_option = input("What do you want to do with list: (pop,append,remove, exit): ").lower()
                
        if modify_option == 'pop':
            pop_data()
                
        elif modify_option == "append":
            append_data()
                
        elif modify_option == "remove":
            remove_data()  

if __name__ == "__main__":
    list_game()