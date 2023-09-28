from sklearn.model_selection import train_test_split
from keras.callbacks import TensorBoard
from keras.utils import to_categorical
from matplotlib import pyplot as plt
from keras.layers import LSTM, Dense
from keras.models import Sequential
import mediapipe as mp
import numpy as np
import cv2 as cv
import time
import os

mp_holistic = mp.solutions.holistic #Holistic model
mp_drawing = mp.solutions.drawing_utils #Drawing utilities 

def mediapipe_detection(image, model):
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)#Color Conversion BGR 2 RBG
    image.flags.writeable = False#Image is no longer writable
    results = model.process(image)#Make prediction
    image.flags.writeable = True#Image is writeable
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)#Color Conversion RBG 2 BGR
    return image, results

def draw_landmarks(image, results):
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)#Draw left hand connections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)#Draw right hand connections

def extract_keypoints(results):
    right_hand = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
    left_hand = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
    return np.concatenate([right_hand, left_hand])

#Path for exported data (np arrays)
DATA_PATH = os.path.join('MP_Data')

# Actions we try to detect
actions = np.array(['rock', 'paper', 'scissors'])

# Action Detection - rather than one frame I used 30 video worth of data to predict actions 
no_sequences = 30

# Videos are going to be 30 frames in length
sequence_length = 30

# Creates a folder for each action and creates a subfolder in that folder for each sequence
for action in actions:
    for sequence in range(no_sequences):
        try:
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass

cap = cv.VideoCapture(1)
#Set mediapipe model
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    #while cap.isOpened():
    #Loop through actions
    for action in actions:
        #Loop through sequences(videos)
        for sequence in range(no_sequences):
            #Loop through video length(sequence length)
            for frame_num in range(sequence_length):

                #Read Frame
                ret, frame = cap.read()

                #Make Detections
                image, results = mediapipe_detection(frame, holistic)
                #print(results)

                #Draw landmarks
                draw_landmarks(image, results)

                #Apply Wait Logic
                if frame_num == 0:
                    cv.putText(image, 'Starting Collection', (120, 200), 
                               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 4, cv.LINE_AA)
                    cv.putText(image, 'Collecting frames for {} Video Number {}'.format(actions, sequence), (15, 12),
                               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv.LINE_AA)
                    #Show frame   
                    cv.imshow('Hand Tracking', image)
                    cv.resizeWindow('Hand Tracking', 1250, 800)
                    cv.waitKey(4000)
                else:
                    cv.putText(image, 'Collectig frames for {} Video Number {}'.format(action, sequence), (15, 12),
                               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv.LINE_AA)
                    #Show frame   
                    cv.imshow('Hand Tracking', image)
                    cv.resizeWindow('Hand Tracking', 1250, 800)

                #Export Keypoints
                keypoints = extract_keypoints(results)
                npy_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
                np.save(npy_path, keypoints)

                #If esc is pressed break
                if cv.waitKey(10) & 0xFF == ord('q'):
                    break

    cap.release()
    cv.destroyAllWindows()


label_map = {label:num for num, label in enumerate(actions)}

sequences, labels = [], []
for action in actions:
    for sequence in range(no_sequences):
        window = []
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
            window.append(res)
        sequences.append(window)
        labels.append(label_map[action])

x = np.array(sequences)
y = to_categorical(labels).astype(int)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.05)
