#Printing title
print("==============================")
print("Welcome to the UMBC \nCar Customization Form!")
print("============================== \n")

#Printing directions
print("(For multiple choice problems, please enter the letter of the selection you're looking for")

#Printing header
print("~ Make & Model ~")

#First question about car model
print("1. What Model of Car are you ordering? \n"
     "  a. Lightning Speedster\n"
     "  b. Eco Leaf\n"
     "  c. Harp Chord\n"
     "  d. Chevron Jolt")

answerModel = input("Please enter 'a' - 'd' :")

#Second question about door option
print("\n2. Would you like to upgrade from the 4-door option to the 2-door option?")

answerUpgrade = input("Please enter 'yes' or 'no' :")

#Exterior header
print("\n~ Exterior ~")

#Third question about color
print("3. What color would you like your car to be?")

answerColor = input("You may enter the name of any color you'd like: ")

#Fourth question about weather package
print("\n4. Would you like the deluxe weather packet?")

answerWeather = input("Please enter 'yes' or 'no' : ")

#Interior header
print("\n~ Interior ~")

#Fifth question about Engine
print("\n5. Which Engine would you like your car to have? \n"
     "  a. I-4 Entry Engine\n"
     "  b. V-6 Performance Engine\n"
     "  c. Eco Diesel Engine")

answerEngine = input("Please enter 'a' - 'c' :")

#Sixth question about heated seats
print("\n6. Would you like heated seats?")

answerSeats = input("Please enter 'yes' or 'no' : ")

#Summary of results
print("\n==============================")
print("~ Summary ~")
print(f"Model Option: {answerModel}\n"
     f"Upgrade to 2-door: {answerUpgrade}\n"
     f"Desired Color: {answerColor}\n"
     f"Upgrade to Deluxe Weather: {answerWeather}\n"
     f"Engine Option: {answerEngine}\n"
     f"Upgrade to Heated Seats: {answerSeats}")
