"""Video manger"""


class VideoManger:
    """Video Manger class"""

    def __init__(self):
        self.__videos = []

    @property
    def videos(self):
        """Return videos"""
        return self.__videos

    def add_video(self, video):
        """Add object to aarray"""
        self.__videos.append(video)

    def find_videos_with_year(self, year):
        """Find video in  grater then year"""
        return [video for video in self.__videos if video.year > year]

    def find_videos_with_director(self, director):
        """Find video with same director"""
        return [video for video in self.__videos if video.director == director]
