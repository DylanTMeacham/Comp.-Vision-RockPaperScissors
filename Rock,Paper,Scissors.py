import random

def _in_Rock_Paper_Scissors ():
    while True:

        #User input choice for the game
        UserInput = input("Enter one of the 3(rock, papper, scissors): ")

        #Randomly Generated Comp. Choice for the game
        PossibleActions = ["rock", "paper", "scissors"]
        CompActions = random.choice(PossibleActions)

        print(f"\nYou chose {UserInput}, computer chose {CompActions}.\n")

        #Tie
        if UserInput == CompActions:
            print(f"Both you and the comp. choose {UserInput}")
        #Rock
        elif UserInput == "rock":
            #Lose
            if CompActions == "paper":
                print("You Lose")
            #Win
            else:
                print("You Win")
        #Paper
        elif UserInput == "paper":
            #Lose
            if CompActions == "scissors":
                print("You Lose")
            #Win
            else:
                print("You Win")
        #Scissors
        elif UserInput == "scissors":
            #Lose
            if CompActions == "rock":
                print("You Lose")
            #Win
            else:
                print("You Win")
        
        playAgain = input(f"\nPlay agin? (y/n):\n")
        if playAgain.input() != "y":
            break
        else:
            Rock_Paper_Scissors()

def Rock_Paper_Scissors():
    try:
        while True:
            _in_Rock_Paper_Scissors()
    except StopIteration:
        pass
    