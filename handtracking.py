import cv2 #import opencv module
import mediapipe as mp # google Ai library
import time #To check the frame rate

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)  # video capture input 1 or 0 or -1 according to y
while True:
    success, img = cap.read()  # reading from capture object returns if the


    # The following three lines is to calculate the fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_ITALIC, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)  # shows the images frame by frame( making it look like a video)
    if cv2.waitKey(1) & 0xFF == ord('q'): #If q is pressed quit the application
        cap.release()
        # Closes all the frames

        cv2.destroyAllWindows()
        break



