"""Serial class"""
from models.video import Video

class Serial(Video):
    """Serial class"""
    def __init__(self, title, director, year, episods, seasons, marks):
        super().__init__(title, director, year)
        self.episods = episods
        self.seasons = seasons
        self.marks = marks

    def rate(self, rating):
        """Rate mehthod"""
        if rating < 1:
            rating = 1
        elif rating > 10:
            rating = 10
        self.marks += 1

    def get_current_rating(self, rating):
        """Return rating"""
        return float(rating) / self.marks


    def __str__(self):
        return f"Serial({self.title},{self.director}, {self.year},\
        {self.episods}, {self.seasons}, {self.marks})"