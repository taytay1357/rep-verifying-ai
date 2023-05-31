import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import formatting.image as fi

class TrainModel:
    def __init__(self, exercise):
        self.exercise = exercise
        self.datadir = f"C:/Users/Josh_2/Desktop/VideoFormatter/training_images/{self.exercise}"
        self.categories = ["good", "bad"]
    
    def trainCategorically(self):
        for category in self.categories:
            path = os.path.join(self.datadir, category)
            for img in os.listdir(path):
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                formatter = fi.ImageFormatter(img_array)
                img_array = formatter.getFormattedImages()
                break
            break