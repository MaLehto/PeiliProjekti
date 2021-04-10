
from cv2 import cv2
from threading import Thread
import playsound
import Apu

def avaaKamera():
    #Hymyn ja kasvojen mallit
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

    cap = cv2.VideoCapture(0)

    while (True):
        ret, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 2.1, 4)
        smiles = smile_cascade.detectMultiScale(gray, 3.5, 20)

        #Hoitaa hymyn käsittelyn
        Apu.hoidaIlo(smiles)
         
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        for (x, y, w, h) in smiles:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('kuva', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    avaaKamera()
    