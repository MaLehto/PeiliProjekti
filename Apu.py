from cv2 import cv2
import playsound
from threading import Thread

ilonMaara = []

#Palauttaa true jos kuvassa on hymy, muuten false
def tunnistaHymy(hymyt):
    if (len(hymyt) > 0):
        return True
    return False       

#Soittaa äänenn
def laski():
    playsound.playsound("laski.mp3")

#Käsittelee hymyn
def hoidaIlo(smiles):
    
    #Jos hymy on positiivinen lisää taulukkoon 1
    if (tunnistaHymy(smiles) == True):
        ilonMaara.append(1)
    
    #Jos ilonmäärä yli 50 menee laski()
    if(len(ilonMaara) > 50):
        Thread(target = laski).start()
        ilonMaara.clear()

    