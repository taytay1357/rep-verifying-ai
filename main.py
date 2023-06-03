from formatting.video import VideoFormatter
from model.train_model import TrainModel
from model.create_model import CreateModel
def main():
    training_model = TrainModel("squat")
    training_model.create_training_data()
    training_model.format_training_data()
    training_model.shuffle_training_data()
    length_of_training_data = training_model.length_of_training()
    model = CreateModel()
    model.create_and_train()

if __name__ == "__main__":
    main()