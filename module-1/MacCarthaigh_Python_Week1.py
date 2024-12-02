def countdown(bottle_count): #create function that manages the countdown of bottles
    for bottles in range(bottle_count, 0, -1):
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer,")
            print(f"Take one down, pass it around, {bottles -1 } bottle(s) of beer on the wall")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer,")
            print(f"Take one down, pass it around, 0 bottles of beer on the wall")

def main(): #main to handle input and trigger countdown
    try:
        bottle_count = int(input("Enter number of bottles: ")) #request input
        if bottle_count == 0:
            print ("Time to buy more beer I guess!") #error for entering 0 bottles
        else:
            countdown(bottle_count)
            print ("Time to buy more bottles of beer!") #expected countdown and end state
    except ValueError:
        print("That isn't a real number of bottles") #error for entering non-integer
        main()

main() 
