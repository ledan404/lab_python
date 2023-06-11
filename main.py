"""Main method"""
from models.tutorial import Tutorial
from models.clip import Clip
from models.film import Film
from models.serial import Serial
from mangers.video_manger import VideoManger


videos = []
obj = VideoManger()

obj.add_video(Clip("Never Gonna Give Ypu Up", "David Hrincker",
              1999, "Rick ALstay", 50000, 100000))
obj.add_video(Clip("See you Again", "Yana Cust", 2015,
                   "Wiz Khalifa", 23133, 23424))
obj.add_video(Film("Silicon Valley", "Duk Colsin", 2013, 14))
obj.add_video(Film("Braking Bad", "Walters Black", 2009, 10))
obj.add_video(Tutorial("How to add aray?", "Hs", 2022, 10000, 20000))
obj.add_video(Serial("Breaking Bad", "David Hrincker", 2008, 60, 5, 10))

print("Вивід всіх елементів")
for video in obj.videos:
    print(video)

print("Вивід методу find_videos_with_year")
for film in obj.find_videos_with_year(2008):
    print(film)
    print("********")

print("Вивід методу result_rating_method")
for video in obj.result_rating_method(10):
    print(video)

print ("********")
print("Вивід методу enumerate")
for video in enumerate(obj.videos):
    print(video)

print ("Вивід методу zip")
for video in zip(obj.videos, obj.result_rating_method(0)):
    print(video)

print("Вивід методу get_attributes_by_type")
for video in obj.videos:
    print(video.get_attributes_by_type(int))

print ("Виввід методу find_videos_with_director")
for film in obj.find_videos_with_director("Hs"):
    print(film)

obj.videos[2].rate(12)
