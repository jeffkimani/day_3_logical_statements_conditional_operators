#Treasure island game
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure!")
direction = input("You're at a crossroad, where do you want to go? Type 'left' or 'right?': ")
select_direction = direction.lower()
if select_direction == "right":
    print("You were eaten by a dragon. Game Over.")
elif select_direction == "left":
    swim_or_wait = input("You've reached a lake. Do you want to swim or wait? Type 'swim' or 'wait': ")
    swim_or_wait_decision = swim_or_wait.lower()
    if swim_or_wait_decision == "swim":
        print("Game Over.")
    elif swim_or_wait_decision == "wait":
        which_door = input("You've reached three doors with different colors. Which door color do you choose: 'R' for red, 'B' for blue, or 'Y' for Yellow?")
        select_door = which_door.lower()
        if select_door == "r":
            print("It's a room full of fire! Game Over.")
        elif select_door == "b":
            print("It's a room full of sea beasts! Game Over.")
        elif select_door == "y":
            print("You Win! You are now wealthy!")
        else:
            print("I do not understand!")
    else:
        print("I do not understand! Use the outlined commands!")
else:
    print("Please use the specified values for the game to work!")