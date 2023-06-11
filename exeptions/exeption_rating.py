"""Class exeption for rating"""

class ExeptionRating(Exception):
    """Class exeption for rating"""
    error = "Rating must be between 1 and 10"
    def __init__(self):
        super().__init__(self.error)
