"""Tutorial class"""
from models.video import Video


class Tutorial(Video):
    """Tutorial class"""

    def __init__(self, title, director, year, like, viems):
        super().__init__(title, director, year)
        self.like = like
        self.viems = viems

    def get_current_rating(self, rating):
        """Return rating"""
        return self.like / self.viems

    def __str__(self):
        return f"Tutorial({self.title},{self.director}, {self.year},\
        {self.like}, {self.viems})"

    def __repl__(self):
        return f"Tutorial({self.title},{self.director}, {self.year},\
        {self.like}, {self.viems})"
