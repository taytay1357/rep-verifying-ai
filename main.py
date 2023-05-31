from video import VideoFormatter
def main():
    video = VideoFormatter('C:/Users/Josh_2/Desktop/VideoFormatter/sample_videos/venice.mp4')
    video.getVideoName()
    print(video.getFramesNumber())
    video.getFrames(20)
    video.showFrames()

if __name__ == "__main__":
    main()