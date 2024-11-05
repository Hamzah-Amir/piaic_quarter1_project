# Assignment no 2: Write a program to calculate weight of object on different planets

def weight():

    try:
        
        weight_earth = float(input("Enter your weight on earth: "))
        other_planet_weight = input("Enter name of planet you want to check your weight on: ").title()

        if other_planet_weight == "Mars":
            print(f"According to NASA calculation your weight on Mars will be: {round(weight_earth*0.38, 2)}")
        
        elif other_planet_weight == "Mercury":
            print(f"According to NASA calculation your weight on Mars will be: {round(weight_earth*0.378,2)}")
        
        elif other_planet_weight == "Venus":
            print(f"According to NASA calculation your weight on Mars will be: {round(weight_earth*0.889,2)}")
        
        elif other_planet_weight == "Jupiter":
            print(f"According to NASA calculation your weight on Mars will be: {round(weight_earth*2.36,2)}")
        
        elif other_planet_weight == "Saturn":
            print(f"According to NASA calculation your weight on Mars will be: {round(weight_earth*1.081,2)}")
        
        elif other_planet_weight == "Uranus":
            print(f"According to NASA calculation your weight on Mars will be: {round(weight_earth*0.815,2)}")
        
        elif other_planet_weight == "Neptune":
            print(f"According to NASA calculation your weight on Mars will be: {round(weight_earth*1.14,2)}")
        
        else:
            print("You Entered invalid name of planet: ")
   
    except Exception as e:
        print(e)

if __name__ == "__main__":
    weight()
        