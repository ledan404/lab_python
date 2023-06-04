"""Video class"""
from abc import ABC, abstractmethod


class Video(ABC):
    """Abstract class"""

    def get_attributes_by_type(self, data_type):
        """Get attributes by type"""
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    @abstractmethod
    def get_current_rating(self, rating):
        """Abstract method"""
