"""Film class"""
from models.video import Video
from exeptions.exeption_rating import ExeptionRating
from decoratos.decorator import logged


class Film(Video):
    """Film class"""
    __instance = None
    rating = 0

    def __init__(self, title, director, year, marks,):
        super().__init__(title, director, year)
        self.marks = marks

    @staticmethod
    def get_instance():
        """Retunr intctace"""
        if Film.__instance is None:
            Film.__instance = Film("", "", 0, 0)
        return Film.__instance

    @logged(ExeptionRating, "file")
    def rate(self, rating):
        """Rate mehthod"""
        self.rating += rating
        self.marks += 1
        if rating > 10 or rating < 1:
            raise ExeptionRating
        return rating

    def get_current_rating(self, rating):
        """Return rating"""
        return (float(rating) / self.marks) * 10

    def __str__(self):
        return f"Film({self.title},{self.director},{self.year},{self.marks})"

    def __repr__(self):
        return f"Film({self.title},{self.director},{self.year},{self.marks})"
