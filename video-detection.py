import cv2
import numpy as np
import os
from gtts import gTTS
import math
import random
import sys
import smtplib

net = cv2.dnn.readNet('yolov3newf.weights','yolov3newf.cfg')
classes = []

with open('newf.names','r') as f:
    classes = f.read().splitlines()

# Now for detecting from Video (mp4)
cap = cv2.VideoCapture(0)

# Now for detecting from Video (mp4)
#cap =  cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    _,img = cap.read()
    # print(classes)
    height, width, _ = img.shape
    # With this part we can open image
    blob = cv2.dnn.blobFromImage(img, 1 / 255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutPuts = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []
    for output in layerOutPuts:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Print how many object is detected
    print(len(boxes))

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    # print(indexes.flatten())
    # Now we need to show more information in a picture
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))
    # Loop for all object detected
    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            print(label)
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label + " " + confidence, (x, y + 20), font, 2, (255, 255, 255), 2)
            #TTS = gTTS(text=str(label))
            #TTS.save("voice.mp4")
            #os.system("voice.mp4")
            #os.system("so.mp4")
            import smtplib
            from email.message import EmailMessage

            SENDER_EMAIL = "crimebranchinvestigation123@gmail.com"
            APP_PASSWORD = "akvqppytvfsvnslm"


            print("Mail Start")
            msg = EmailMessage()
            msg['Subject'] = "Suspicious Object Detection"
            msg['From'] = SENDER_EMAIL
            msg['To'] = "walishrikants007@gmail.com"
            msg.set_content(label +'\t' +'object is detected')

            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(SENDER_EMAIL, APP_PASSWORD)
                    smtp.send_message(msg)
                    print("Mail send successfully")

            # color = red
            
           ## akvqppytvfsvnslm


    cv2.imshow('image', img)
    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()
