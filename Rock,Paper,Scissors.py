#4. The Rock Paper Scissors
from pyexpat import model
import cv2
import Visions
import random
import numpy as np
import keras.models
import threading

def _in_main():
    with open('gesture.names', 'r') as f:
        classNames = f.read().split('\n')
        f.close()
    
    #open("testoutput", "w").close() #debug

    model = keras.models.load_model('mp_hand_gesture') 
        
    windowthread = threading.Thread(target=Visions.main) 
    windowthread.start()
        
    while True:
    #read frame
    
        if not Visions.landmarks:
            continue
    
        prediction = model.predict([Visions.landmarks])
        # print(prediction)
        classID = np.argmax(prediction)
        Userinput = classNames[classID] #get name Rock, Paper, or Scissors

    ##Computers choice
        PossibleActions = "rock", "paper", "scissors"
        ComputerActions = random.choice(PossibleActions)

    
    #Output
        with open("testoutput.txt", "a") as f: #debug
            print(f"\nYou choose {Userinput}, computer choose {ComputerActions}.\n", file=f)

    #Determine the Winner
            #Rock
            if Userinput == 'Rock' and Userinput != 'Scissors' and Userinput !=  'Paper':
                #Tie
                if ComputerActions == "rock" and ComputerActions != "scissors" and Userinput !=  "paper":
                    print(f"\nRock vs Rock. Imagin tying with a robot though. I bet you've lost to it too. LOSER!\n", file=f)  
                #Win
                if ComputerActions == "scissors" and ComputerActions != "rock" and Userinput !=  "paper":
                    print(f"\nRock Smashes Scissors. You Win!\n", file=f)    
            #Paper 
            if Userinput == 'Paper' and Userinput != 'Scissors' and Userinput !=  'Rock':
                if ComputerActions == "paper" and ComputerActions != "rock" and Userinput !=  "scissors":
                    print(f"\nPaper vs Paper. Imagin tying with a robot though. I bet you've lost to it too. LOSER!\n", file=f)
            #Scissors 
            if Userinput == 'Scissors' and Userinput != 'Rock' and Userinput !=  'Paper':
                if ComputerActions == "scissors" and ComputerActions != "paper" and Userinput !=  "rock":
                    print(f"\nScissors vs Scissors. Imagin tying with a robot though. I bet you've lost to it too. LOSER!\n", file=f)  
        #Win
            #Paper
            if Userinput == 'Paper' and Userinput != 'Scissors' and Userinput !=  'Rock':
                if ComputerActions == "rock" and ComputerActions != "paper" and Userinput !=  "scissors":
                    print(f"\nPaper Covers Rock. You Win!\n", file=f)
            #Scissors
            if Userinput == 'Scissors' and Userinput != 'Rock' and Userinput !=  'Paper':
                if ComputerActions == "paper" and ComputerActions != "scissors" and Userinput !=  "rock":
                    print(f"\nScissors Cuts Paper. You Win!\n", file=f) 
                 
            #Lose
                    if ComputerActions == "paper" and ComputerActions != "rock" and Userinput !=  "scissors":
                        print(f"\nPaper Covers Rock. You Lose.\n", file=f)
                #Paper 
                if Userinput == 'Paper' and Userinput != 'Scissors' and Userinput !=  'Rock':
                    if ComputerActions == "scissors" and ComputerActions != "paper" and Userinput !=  "rock":
                        print(f"\nScissors Cuts Paper. You Lose.\n", file=f)  
                #Scissors
                if Userinput == 'Scissors' and Userinput != 'Rock' and Userinput !=  'Paper':
                    if ComputerActions == "rock" and ComputerActions != "scissors" and Userinput !=  "paper":
                        print(f"\nRock breaks Scissors. You Lose.\n", file=f)
                    else:
                        print(f"\nCouldn't read hand sign, try again\n", file=f)    
        
        playAgain = input(f"\nPlay agin? (y/n):\n", file=f)
        if playAgain.input() != "y":
            break
        else:
            main()

def main():
    try:
        while True:
            _in_main()
    except StopIteration:
        pass
    