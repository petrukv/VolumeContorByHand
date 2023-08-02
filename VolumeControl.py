import cv2
import mediapipe as mp
import pyautogui
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        centerPoint1 = hand1['center']
        handType1 = hand1["type"]

        fingers1 = detector.fingersUp(hand1)

        cv2.putText(img, handType1, (bbox1[0], bbox1[1] - 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"] 
            centerPoint2 = hand2['center']
            handType2 = hand2["type"]

            fingers2 = detector.fingersUp(hand2)

            length, info = detector.findDistance(lmList1[8], lmList1[4], img)  

        else:
            length, info = detector.findDistance(lmList1[8], lmList1[4], img)  
        if length > 50:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    cv2.imshow("Image", img)

    if cv2.waitKey(1) == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()