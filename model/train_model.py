import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import formatting.image as fi
import random
import pickle

class TrainModel:
    def __init__(self, exercise):
        self.exercise = exercise
        self.datadir = f"C:/Users/Josh_2/Desktop/VideoFormatter/training_images/{self.exercise}/"
        self.categories = ["good", "bad"]
        self.training_data = []

    def create_training_data(self):
        for category in self.categories:
            path = os.path.join(self.datadir, category)
            class_num = self.categories.index(category)
            for img in os.listdir(path):
                try:
                    img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                    formatter = fi.ImageFormatter(img_array)
                    new_array = formatter.getFormattedImages()
                    self.training_data.append([new_array, class_num])
                except Exception as e:
                    print(e)
    
    def format_training_data(self):
        X = []
        y = []
        for features, label in self.training_data:
            X.append(features)
            y.append(label)
        formatter = fi.ImageFormatter([])
        image_size = formatter.getImageSize()
        X = np.array(X).reshape(-1, image_size, image_size, 1)

        pickle_out = open("X.pickle", "wb")
        pickle.dump(X, pickle_out)
        pickle_out.close()

        pickle_out = open("y.pickle", "wb")
        pickle.dump(y, pickle_out)
        pickle_out.close()


    def shuffle_training_data(self):
        random.shuffle(self.training_data)

    def length_of_training(self):
        return len(self.training_data)