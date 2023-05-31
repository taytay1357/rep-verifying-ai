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
        self.cap = cv2.VideoCapture(self.video_path)

    def getVideoName(self):
        file_name = os.path.basename(self.video_path)
        return os.path.split(file_name)[0]

    def getFramesNumber(self):
        return self.cap.get(cv2.cv2.CAP_PROP_FRAME_COUNT)
        self.cap.release()
    
    def getHeightAndWidth(self):
        return self.cap.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT), self.cap.get(cv2.cv2.CAP_PROP_FRAME_WIDTH)
        self.cap.release()
    
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
        return self.cap.get(cv2.CAP_PROP_FPS)
    
    def getFrames(self, frames):
        number_of_frames = self.getFramesNumber()
        jump = number_of_frames // frames
        position = 0
        for frame in range(frames):
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, position)
            ret, img = self.cap.read()
            position += jump
            if ret == False:
                break
            self.image_data.append(img)
        return self.image_data

    def convertVideoFormat(self):
        subprocess.run(['ffmpeg', '-i', self.video_path, 'qscale', '0', f'{self.video_name}.mp4'])
        self.video_path = self.video_path.replace('.*', '.mp4')

    def showVideo(self):
        ipd.Video(self.video_path, width=700)
    
    def showFrames(self):
        fig, axs = plt.subplots(5, 5, figsize=(30,20))
        axs = axs.flatten()
        plt.show()
        for frame in range(len(self.image_data)):
            axs[frame].imshow(cv2.cvtColor(self.image_data[frame], cv2.COLOR_BGR2RGB))
        plt.tight_layout()
        plt.show()

