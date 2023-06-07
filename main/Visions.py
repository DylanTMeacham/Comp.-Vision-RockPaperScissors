
import cv2 
import mediapipe as mp 
import argparse

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=1)
    parser.add_argument('--use_static_image_mode', action='store_true')
    parser.add_argument("--min_detection_confidence",
                        help='min_detection_confidence',
                        type=float,
                        default=0.7)
    parser.add_argument("--min_tracking_confidence",
                        help='min_tracking_confidence',
                        type=int,
                        default=0.5)

    args = parser.parse_args()

    return args

def _in_Visions():
    args = get_args()

    #Initializes the Camera 
    cam = args.device
    cap = cv2.VideoCapture(cam)

    #use_static_image_mode = args.use_static_image_mode
    min_detection_confidence = args.min_detection_confidence
    #min_tracking_confidence = args.min_tracking_confidence

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        #static_image_mode=use_static_image_mode,
        max_num_hands=2,
        min_detection_confidence=min_detection_confidence,
        #min_tracking_confidence=min_tracking_confidence,
    )


    while True:

        _, frame = cap.read()
        cv2.imshow("Output", frame) 
        c =  cv2.waitKey(1) 

        if c == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

def Visions():
    try:
        while True:
            _in_Visions()
    except StopIteration:
        pass

if __name__ == "__main__":
    Visions()