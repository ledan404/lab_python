from models.Video import Video

class Clip(Video):
    def __init__(self, title, director, year, artist, like, viems):
        super().__init__(title, director, year)
        self.artist = artist
        self.like = like
        self.viems = viems
    
    def get_current_rating(self):
        return self.like / self.viems
    
    def __str__(self):
        return f"Clip({self.title},{self.director}, {self.year}, {self.artist}, {self.like}, {self.viems}" 