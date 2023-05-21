from models.Video import Video

class Film(Video):
    instance = None

    def __init__(self, title, director, year, marks):
        super().__init__(title, director, year)
        self.marks = marks

    @staticmethod
    def get_instance():
        if Film.instance is None:
            Film.instance = Film("", "", 0, 0)
        return Film.instance

    def rate(self, rating):
        if rating < 1:
            rating = 1
        elif rating > 10:
            rating = 10
        self.marks += 1

    def get_current_rating(self, rating):
        return float(rating) / self.marks
    
    def __str__(self):
        return f"Film({self.title},{self.director},{self.year},{self.marks})"