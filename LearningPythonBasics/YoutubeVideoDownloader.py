from pytube import YouTube
from sys import argv

#link = str(argv[1])
link = "https://www.youtube.com/watch?v=WyyUPqdZQfU&ab_channel=GameIndustryConference"
yt = YouTube(link)

print("Title:", yt.title)

print("views:", yt.views)

yd = yt.streams.get_highest_resolution()

# creates a folder if it does not exist
path = './youtubevideos'
yd.download(path)

print("downloading video")
