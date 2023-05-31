import pandas as pd
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt
from glob import glob
import IPython.display as ipd
from tqdm.notebook import tqdm
import subprocess

class VideoFormatter:
    def __init__(self, video_path):
        self.video_path = video_path
        self.image_data = []
        self.video_name = self.getVideoName()
        self.convertVideoFormat()
        

    def getVideoName(self):
        file_name = os.path.basename(self.video_path)
        return os.path.split(file_name)[0]

    def getFramesNumber(self):
        cap = cv2.VideoCapture(self.video_path)
        frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        cap.release()
        return frame_count
    
    def getHeightAndWidth(self):
        cap = cv2.VideoCapture(self.video_path)
        height,width = cap.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT), self.cap.get(cv2.cv2.CAP_PROP_FRAME_WIDTH)
        cap.release()
        return height, width
    
    def getVideoLength(self):
        fps = self.getFPS()
        numberOfFrames = self.getFramesNumber()
        return numberOfFrames // fps

    def display_cv2_img(img, figsize=(10,10)):
        img_ = cv2.cvtColor(img, cv2.COLORBGR2RGB)
        fig, ax = plt.subplots(figsize=figsize)
        ax.imshow(img_)
        ax.axis("off")
    
    def display_image(self, img):
        self.display_cv2_img(img)

    def getFPS(self):
        cap = cv2.VideoCapture(self.video_path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        cap.release()
        return fps
    
    def getFrames(self):
        cap = cv2.VideoCapture(self.video_path)
        number_of_frames = self.getFramesNumber()
        for frame in range(number_of_frames):
            ret, img = cap.read()
            if ret == False:
                break
            self.image_data.append(img)
        cap.release()
        return self.image_data

    def convertVideoFormat(self):
        self.video_path = self.video_path.replace('.*', '.mp4')

    def showVideo(self):
        ipd.Video(self.video_path, width=700)
    
    def showFrames(self):
        img_idx = 0
        fig, axs = plt.subplots(5, 4, figsize=(30,20))
        axs = axs.flatten()
        for frame in range(len(self.image_data)):
            axs[img_idx].imshow(cv2.cvtColor(self.image_data[frame], cv2.COLOR_BGR2RGB))
            axs[img_idx].set_title(f'Frame: {frame+1}')
            axs[img_idx].axis('off')
            img_idx += 1
        
        plt.tight_layout()
        plt.show()

    

