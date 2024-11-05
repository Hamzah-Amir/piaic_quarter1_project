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
    
    accept_index = int(input("Enter index of the list: "))

    if accept_index in list:
        print(list[accept_index])
    else:
        return "Index is out if range"
    
def modify_list():
    

list_func()