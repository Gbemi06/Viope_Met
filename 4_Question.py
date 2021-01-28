# Exercise 1
total_rounds = 5
now_lap = 0
while now_lap < total_rounds:
    print("This is lap", now_lap)
    now_lap += 1

# Exercise 2
# Create a program which, for every loop, prompts the user for input,
# and then prints it on the screen. If the user inputs the string "quit",
# the program prints "Bye bye!" and shuts down.

number = True

while number:
    user_wrote = input("write something: ")

    if user_wrote == "quit":
        number = False
        print("Bye bye!")

    else:
        print(user_wrote)



