from formatting.video import VideoFormatter
from model.train_model import TrainModel
from model.create_model import CreateModel
def main():
    model = CreateModel()
    model.create_and_train()

if __name__ == "__main__":
    main()