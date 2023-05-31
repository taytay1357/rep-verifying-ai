from formatting.video import VideoFormatter
from model.train_model import TrainModel
def main():
    model = TrainModel("squat")
    model.trainCategorically()

if __name__ == "__main__":
    main()