"""
    
"""
import cv2, os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd


def getImagesAndLabels(path):
   
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

  
    faces = []
 
    Ids = []
 
    for imagePath in imagePaths:
       
        pilImage = Image.open(imagePath).convert('L')
   
        imageNp = np.array(pilImage, 'uint8')
  
        Id = int(os.path.split(imagePath)[-1].split(".")[1])
       
        faces.append(imageNp)
        
        Ids.append(Id)
    return faces, Ids


def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces , Id= getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
   
    recognizer.save("TrainData\Trainner.yml")
    res = "Image Trained and data stored in TrainData\Trainner.yml "

    print(res)

   

TrainImages()
    
