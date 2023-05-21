from abc import ABC, abstractmethod

class Video(ABC):
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year
    
    @abstractmethod
    def get_current_rating(self, rating):
        pass
