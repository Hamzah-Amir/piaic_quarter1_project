#  Assignment no 1 (Problem 1): Create a list then add mango at end and print updated list 

fruit_list = ["apple","banana","grapes","pineapple", "orange"]
print(fruit_list)

fruit_list.append("mango")
print(fruit_list)

# Assignment no 3 (problem 2): Create a Python program that helps you practice accessing and manipulating elements in a list

list = ["hamza", "55", True, 489, 524.69]

"""Task no 1: Write a function that:
Accept list and index as input
Returns element at specified index and if index is out of range returns an appropriate message"""

def list_func():
    
    lst = ["hamza", "55", True, 489, 524.69]
    accept_index = int(input("Enter index of the list: "))

    if accept_index <= len(lst):
        print(list[accept_index])
    
    else:
        return "Index is out f range"
    
def modify_list():
    
    lst = ["hamza", "55", True, 489, 524.69]
    
    index = int(input("Enter Index value: "))
    new_value = input("Enter new value you want to replace with: ")

    if index < len(lst):
        lst[index] = new_value
        print(lst)
        
    else:
        return "Index is out of range"    

if __name__ == "__main__":
    list_func()
if __name__ == "__main__":    
    modify_list()


# Assignment no 3 (Final Task): Create a game That prompt user to access modify or slice list 
# and prints the updated list

def pop():
     
     try: 
        index = int(input("Enter index you want to pop: "))
        data.pop(index)
     except IndexError:
         print("Index is out oof range!")

num = [5,6,648,13,364]

def list_slice():
    
    start_index = int(input("Enter starting index: "))
    last_index = int(input("Enter last index: "))

    if (start_index or last_index) <= len(num):
        updated_num = num[start_index:last_index]
        print(updated_num)
    else:
        print("Index is out of range! ")

