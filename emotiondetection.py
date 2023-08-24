import cv2
from deepface import DeepFace
from time import sleep

cap = cv2.VideoCapture("faces8s.avi")

def showResults(feed):
    output = feed[0]
    outputList = list(output.items())
    #print(type(outputList))
    #print(outputList[1])
    dominantEmotion, detectedEmotion = outputList[1]
    #print(detectedEmotion)
    #sleep(2)
    return detectedEmotion
    
    
while True:
    ret , vid = cap.read()
    
    results = DeepFace.analyze(vid,actions=("emotion"),enforce_detection=False)
    
    emotion = showResults(results)
    
    #print(emotion)
    cv2.putText(vid,emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (80, 70, 255), 2, cv2.LINE_4)
        

    cv2.imshow("video",vid)
    
    k = cv2.waitKey(1) & 0xFF
           
    if k == 27:
        break
    
cv2.destroyAllWindows()
    
    
    