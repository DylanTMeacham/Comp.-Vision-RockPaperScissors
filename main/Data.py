import os
import numpy as np
#Path for exported data (np arrays)
DATA_PATH = os.path.join('MP_Data')

#Actions we try to detect
actions = np.array(['rock', 'paper', 'scissors'])

#Action Detection - rather than one frame I used 30 video worth of data to predict actions 
no_sequences = 30

#Videos are going to be 30 frames in length
sequence_length = 30

#Creates a folder for each action and creates a subfolder in that folder for each sequence
for action in actions:
    for sequence in range(no_sequences):
        try:
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass