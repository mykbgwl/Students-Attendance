import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64

# Starting the webcam

capt = cv2.VideoCapture(0)

names = []

# Creating Attendees file

fob = open('attendees.txt', 'a+')


def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z = ''.join(str(z))
        fob.write(z+'\n')
        return names


print('Reading code...')

# Function of Data present or not


def checkData(data):
    data = str(data)
    if data in names:
        print('Already present')
    else:
        print('\n'+str(len(names)+1)+'\n'+'Attendance Marked')
        enterData(data)


while True:
    _, frame = capt.read()
    decodedObject = pyzbar.decode(frame)
    for obj in decodedObject:
        checkData(obj.data)
        time.sleep(1)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.destroyAllWindows()
        break

fob.close()
