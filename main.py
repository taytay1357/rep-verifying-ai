from formatting.video import VideoFormatter
from model.train_model import TrainModel
def main():
    model = TrainModel("squat")
    model.create_training_data()
    print(model.length_of_training())

if __name__ == "__main__":
    main()