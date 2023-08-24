import socket
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


# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Specify the IP address and port number of your Raspberry Pi Pico W
# You can use the ipconfig or ifconfig command to find out the IP address of your device
ip = '192.168.0.103' # Change this to your Raspberry Pi Pico W IP address
port = 80 # Change this to your Raspberry Pi Pico W port number

# Connect to the server socket
s.connect((ip, port))

# Start a while loop
while True:
    
    ret , vid = cap.read()
    
    results = DeepFace.analyze(vid,actions=("emotion"),enforce_detection=False)
    
    emotion = showResults(results)
    
    #print(emotion)
    cv2.putText(vid,emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (80, 70, 255), 2, cv2.LINE_4)
        

    cv2.imshow("video",vid)
    
    k = cv2.waitKey(1) & 0xFF
           
    data = emotion
    # Encode the data as bytes
    data = data.encode()
    # Send the data to the server
    s.send(data)
    # Receive a response from the server
    response = s.recv(1024)
    print(response)
    # Check if the user wants to stop the loop
    
    if k == 27:
        break

# Close the socket
s.close()
cv2.destroyAllWindows()
