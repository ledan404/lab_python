from models.Video import Video
from models.Clip import Clip
from models.Film import Film
from mangers.VideoManger import videos, add_video;

add_video(Clip("Never Gonna Give Ypu Up", "David Hrincker", 1999, "Rick ALstay", 2400404, 130000000))
add_video(Clip("See you Again", "Yana Cust", 2015, "Wiz Khalifa", 23232232, 232032030))
add_video(Film("Silicon Valley", "Duk Colin", 2013, 9))
add_video(Film("Braking Bad", "Walter Black", 2009, 10))

for video in videos:
    print(video)