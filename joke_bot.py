# Assignment no 1 create a joke bot that only tells jokes

def joke():
    prompt = input("Hello user, what do you want from me: ").strip().lower()
    
    joke = """Here is a joke for you!\n    Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her:
    get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of
    milk. The programmer asks why and Sophia replies: 'because they had eggs'"""

    if prompt == "joke":
        print(joke)
    else:
        print("Sorry! I only tell jokes. ")

joke()
