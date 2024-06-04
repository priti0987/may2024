# # #
# #
# # #print name , class , fav col
# # #fav game
# #
# # #cal len all
# name = "priti"
# # print(name)
# # print(f"length of {name} is {len(name)}")
# # print("lenght is ")

from pytube import YouTube
from sys import argv

# uLink =input("Enter Youtube link : ")
# link = argv[1]

yt = YouTube("https://www.youtube.com/watch?v=TQWZXBYvhck")

print("Title : ",yt.title)
print("View : ",yt.views)
print("Len :",yt.length)

yd = yt.streams.get_highest_resolution()
path_r = "C:\\Users\\Dell\\Pictures\\Pratap_\\movies"
# C:\Users\Dell\Pictures\Pratap_\movies\ExecersiseRoberta\study\cSharpVideos
yd.download(path_r)
print("Done.............!")