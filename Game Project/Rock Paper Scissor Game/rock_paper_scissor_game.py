'''
Name : Rock-Paper-Scissor Game
Date : 10/31/2020
Author : Fahad
'''
# Import random module
import random
# Define a function to decide the winner


def gamewin(computer, player):

    # When the computer and player choose the same
    if computer == player:
        return None

    # When computer choose the rock
    if computer == "r":
        if player == "p":
            return True
        elif player == "s":
            return False

    # when computer choose the paper
    if computer == "p":
        if player == "s":
            return True
        elif player == "r":
            return False

    # When computer choose the scissor
    if computer == "s":
        if player == "r":
            return True
        elif player == "p":
            return False


# Generate random number
randomNo = random.randint(1, 3)
# Give the computer turn value with the random number
if randomNo == 1:
    computer = "r"
elif randomNo == 2:
    computer = "p"
elif randomNo == 3:
    computer = "s"

round = 0  # count round
player = None  # Deafult value

while player != True:
    round += 1
    print("Computer Turn : ***************")
    player = input(
        "Your Turn : ------------- \nRock(r) , Paper(p) or Scissor(s) : ")
    # Player turn : Player give a value

    if player == "r" or player == "p" or player == "s":
        # Pass the two values to gamewin function to justify
        isPlayerWin = gamewin(computer, player)

    # converts character to word
        #For : Computer
        if computer == "r":
            computer = "Rock"
        elif computer == "p":
            computer = "Paper"
        else:
            computer = "Scissor"

        #For : Player
        if player == "r":
            player = "Rock"
        elif player == "p":
            player = "Paper"
        else:
            player = "Scissor"

        # show both results
        print("-----------------------")
        print(f"Computer choose : {computer}")
        print(f"You choose : {player}\n------------------")

        # Print who is the winner
        if isPlayerWin is None:
            print("The game is Tie!\n\n")
        elif isPlayerWin:
            print("******Congrats! You are the winner.*********\n\n")
        else:
            print("****You lose! Try again.****\n\n")
    elif(player == "q"):
        exit()

    else:
        print(
            "****Invalid Keyword*****\nPlease choose from Rock(r), Paper(p) or Scissor(s) [only write : r, p, s]\n\n")
print(f"You win in {round} Try!")
