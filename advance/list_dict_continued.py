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
