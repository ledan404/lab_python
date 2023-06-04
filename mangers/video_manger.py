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
        all_any = {"any": any(video for video in self.__videos if video.director == director),
                   "all": all(video for video in self.__videos if video.director == director),}
        return all_any

    def __len__(self):
        return len(self.__videos)

    def __getitem__(self, index):
        return self.__videos[index]

    def __iter__(self):
        return iter(self.__videos)

    def result_rating_method(self, reting):
        """Return rating"""
        return [video.get_current_rating(reting) for video in self.__videos]

    def enumerate(self):
        """Return enumerate"""
        return enumerate(self.videos)

    def __repr__(self):
        return f"VideoManger({self.__videos})"
