from pytube import YouTube
from sys import argv

uLink =input("Enter Youtube link : ")
# link = argv[1]

yt = YouTube(uLink)

print("Title : ",yt.title)
print("View : ",yt.views)
print("Len :",yt.length)

yd = yt.streams.get_highest_resolution()
path_r = "C:\\Users\\Dell\\Pictures\\Pratap_\\movies"
# C:\Users\Dell\Pictures\Pratap_\movies\ExecersiseRoberta\study\cSharpVideos
yd.download(path_r)
print("Done.............!")