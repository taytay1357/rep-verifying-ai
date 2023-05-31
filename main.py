from video import VideoFormatter
def main():
    video = VideoFormatter('C:/Users/Josh_2/Desktop/Venice_10.mp4')
    video.getFrames()
    video.showFrames()

if __name__ == "__main__":
    main()