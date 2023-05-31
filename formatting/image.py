import os
import cv2
import matplotlib.pyplot as plt
import IPython.display as ipd
from tqdm.notebook import tqdm
import subprocess

class ImageFormatter:
    def __init__(self, img_array=[]):
        self.img_array = img_array
        self.resize()
        self.recolour()
    
    def resize(self):
        img_size = 100
        self.img_array = cv2.resize(self.img_array, (img_size, img_size))
        plt.imshow(self.img_array, cmap="gray")
        plt.show()

    def recolour(self):
        for img in self.img_array:
            self.img_array[img] = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def getFormattedImages(self):
        return self.img_array   
