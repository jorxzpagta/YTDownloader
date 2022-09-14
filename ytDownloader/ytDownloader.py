from pytube import YouTube

# path where you want ot save your video
path = "C:/Users/jorex/Downloads/DownloadedVideo"


# downloads the video
def get_video(link):
    yt = YouTube(link)
    # gets the highest resolution of the video
    yd = yt.streams.get_highest_resolution()
    yd.download(path)


# gets the title of the video you downloaded
def get_title(link):
    return YouTube(link).title
