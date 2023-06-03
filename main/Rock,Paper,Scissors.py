
import random

Playing = True

def _in_Rock_Paper_Scissors ():

    while True:

        options = ("rock", "paper", "scissors")
        comp = random.choice(options)
        
        player = None
        while player not in options:
            player = input("Choose your pick (rock, paper, scissors)")

        print(f"Player: {player} | Comp: {comp}")

        #Tie
        if player == comp:
            print("Wow tying with a comp thats embarasing")
        #Rock
        elif player == "rock":
            #Win
            if comp == "scissors":
                print("You beat a comp. Congrats")
            #Loss
            else:
                print("Image lossing to a comp")
        #Paper
        elif player == "paper":
            #Win
            if comp == "rock":
                print("You beat a comp. Congrats")
            #Loss
            else:
                print("Image lossing to a comp")
        #Scissors
        elif player == "scissors":
            #Win
            if comp == "paper":
                print("You beat a comp. Congrats")
            #Loss
            else:
                print("Image lossing to a comp")

        playAgain = input("Play agin? (y/n):").lower()
        if not playAgain.input() == "y":
            Playing = False
            print("Thanks for PLaying")

def Rock_Paper_Scissors():
    try:
        while Playing:
            _in_Rock_Paper_Scissors()
    except StopIteration:
        pass
    
if __name__ == "__main__":
    Rock_Paper_Scissors()