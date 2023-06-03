import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
from tqdm.notebook import tqdm
import subprocess

class ImageFormatter:
    def __init__(self, img_array):
        self.img_array = np.array(img_array)
        self.resize()
    
    def resize(self):
        img_size = 100
        self.img_array = cv2.resize(self.img_array, (img_size, img_size))

    def getFormattedImages(self):
        return self.img_array

    def getImageSize(self):
        return 100   
