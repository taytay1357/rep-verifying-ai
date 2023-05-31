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
        self.video_name = self.getVideoName()
        self.convertVideoFormat()

    def getVideoName(self):
        file_name = os.path.basename(self.video_path)
        return os.path.splittext(file_name)[0]

    def getFramesNumber(self):
        #will get number of frames in the video
        pass

    def getVideoLength(self):
        #gets length of the video
        pass

    def getFrames(self, frames):
        #gets 'frames' number of frames from the video and returns them
        pass

    def convertVideoFormat(self):
        subprocess.run(['ffmpeg', '-i', self.video_path, 'qscale', '0', f'{self.video_name}.mp4'])
        self.video_path = self.video_path.replace('.*', '.mp4')

    def showVideo(self):
        ipd.Video(self.video_path, width=700)