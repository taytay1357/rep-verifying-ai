import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, MaxPooling2D, Flatten, Conv2D
import pickle

class CreateModel:
    def __init__(self):
        self.X, self.y = self.load_and_format_training()


    def load_and_format_training(self):
        X = pickle.load(open("X.pickle", "rb"))
        y = pickle.load(open("y.pickle", "rb"))

        return X,y

    def create_and_train(self):
        model = Sequential()
        model.add(Conv2D(64), (3,3), input_shape= self.X.shape[1:])
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2)))

        model.add(Conv2D(64), (3,3), input_shape= self.X.shape[1:])
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2,2)))

        model.add(Flatten())
        model.add(Dense(64))

        model.add(Dense(1))
        model.add(Activation('sigmoid'))

        model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

        model.fit(self.X, self.y, batch_size=32, validation_split=0.1)




