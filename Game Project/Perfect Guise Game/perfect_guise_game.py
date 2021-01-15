import random
import os
import pickle

#!THE GAME FUNCTION
def game():
    userguise = None
    scoreList = []
    guise = 0
    mul = True
    hiscore = ""
    print("**********The Perfect Guess Game***************")
    # Pick a level that user wants
    level = input(
        "Choose a level Very easy(ve), Easy(e) , medium(m), hard(h), Extreme(ex)\n------------------ : ")
    folder = "Game Project/__game_data__(Perfect Guise Game)"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Customize the game as levels
    if level == "ve":
        num = 10
        filename = "hiscore_very_easy.pkl"
        mode_desc = "in (Very easy) mode"
        todo = "Guise a number between 1 to 10."
    elif level == "e":
        num = 100
        filename = "hiscore_easy.pkl"
        mode_desc = "in (Easy) mode"
        todo = "Guise a number between 1 to 100."
    elif level == "m":
        num = 200
        filename = "hiscore_medium.pkl"
        mode_desc = "in (Medium) mode"
        todo = "Guise a number between 1 to 200."
    elif level == "h":
        num = 500
        filename = "hiscore_hard.pkl"
        mode_desc = "in (Hard) mode"
        todo = "Guise a number between 1 to 500."
    elif level == "ex":
        num = 1000
        filename = "hiscore_extreme.pkl"
        mode_desc = "in (Extreme)"
        todo = "Guise a number between 1 to 1000."
    else:
        num = 100
        filename = "hiscore_easy.pkl"
        mode_desc = "in (Easy) mode"
        todo = "Guise a number between 1 to 100."

    for i in range(int(input("Enter the player number : "))):
        randomNum = random.randint(1, num)
        print(f"Player {i+1} Turn : ")
        # Read the hiscore file to print highscores
        if os.path.isfile(f"{folder}/{filename}"):  # Check a file is present or not
            with open(f"{folder}/{filename}") as f:
                hiscore = pickle.load(f)
                define_file = True
        else:
            # If a file not present in the directory then create a file on this directory
            with open(f"{folder}/{filename}", "w") as f:
                pickle.dump("")  # Create file
                define_file = False

        print("****Type q to exit the game.****")
        print(f"Mode : {mode_desc}")
        if define_file and hiscore != "":
            print(f"High Score: {hiscore} trails\n------------------")
        print(f"TODO : {todo}")
        while userguise != randomNum:
            try:
                # Handling errors
                # Keep the input of the user
                userguise = input("Enter a guise number : ")
                if userguise == "q":
                    input("Hit Enter to exit ")
                    exit()
                userguise = int(userguise)  # convert str to int
                guise += 1  # Count the guises
                # Check the userguise is same to the random number or not
                if userguise == randomNum:
                    print(f"You guised number on {guise} trails")
                    scoreList.append(guise)
                    guise = 0
                else:
                    # manipulating some hints for helping the user to guise the number
                    if userguise > randomNum:
                        print("You guised wrong! Hint: Enter a smaller number")
                    else:
                        print("You guised wrong! Hint: Enter a larger number")
            except ValueError:
                print("Invalid Value! Make sure to enter a number.")
        
    if mul:
        winner = scoreList.index(min(scoreList))
        print(f"Player {winner+1} win!")
        score = min(scoreList)
    else:
        score = guise
        
    with open(f"{folder}/{filename}") as f:
        hiscore = pickle.load(f)
    if hiscore == "":
        with open(f"{folder}/{filename}", 'w') as f:
            pickle.dump(str(score), f)
    elif int(hiscore) > score:
        with open(f"{folder}/{filename}", 'w') as f:
            pickle.dump(str(score), f)
            print("\n")
            print(
                f"\t****Congratulations! You made a highscore of {score} guises {mode_desc}****\n")
    if userguise == randomNum:
        isRestart = input("Do you want to play again (y)/(n) : ")
        if isRestart == "y":
            game()
    else:
        print("Ok! Exiting....... the game.")
        exit()

game()

print("Thanks For Playing This Game!")
input("Tap \"Enter\" key to exit ")
