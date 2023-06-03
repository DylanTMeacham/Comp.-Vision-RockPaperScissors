
import cv2

# Initialize the webcam
cap = cv2.VideoCapture(0)

def _in_Visions():
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