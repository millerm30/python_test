from random import randint

# Create a list of play options
t = ["Rock", "Paper", "Scissors"]

# Assign a random play to the computer
computer = t[randint(0,2)]

# Set player to False
player = False

while player == False:
    # Set player to True
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")


# Reset the game and start again
player = False
computer = t[randint(0,2)]