"""Film class"""
from models.video import Video


class Film(Video):
    """Film class"""
    __instance = None

    def __init__(self, title, director, year, marks):
        super().__init__(title, director, year)
        self.marks = marks

    @staticmethod
    def get_instance():
        """Retunr intctace"""
        if Film.__instance is None:
            Film.__instance = Film("", "", 0, 0)
        return Film.__instance

    def rate(self, rating):
        """Rate mehthod"""
        if rating < 1:
            rating = 1
        elif rating > 10:
            rating = 10
        self.marks += 1
        return rating

    def get_current_rating(self, rating):
        """Return rating"""
        return float(rating) / self.marks

    def __str__(self):
        return f"Film({self.title},{self.director},{self.year},{self.marks})"

    def __repr__(self):
        return f"Film({self.title},{self.director},{self.year},{self.marks})"
