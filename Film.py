class Film:
    instance = None

    def __init__(self, title="", director="", year=0, rating=0.0, marks=0):
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating
        self.marks = marks

    @staticmethod
    def get_instance():
        if Film.instance is None:
            Film.instance = Film()
        return Film.instance

    def rate(self, rating):
        if rating < 1:
            rating = 1
        elif rating > 10:
            rating = 10
        self.rating += rating
        self.marks += 1

    def get_current_rating(self):
        if self.marks == 0:
            return 0.0
        return self.rating / self.marks

    def __str__(self):
        return f"Film(title='{self.title}', director='{self.director}', year={self.year}, rating={self.rating}, marks={self.marks})"


if __name__ == "__main__":
    films = [Film() for _ in range(4)]
    films[1] = Film("Fight Club", "David Fincher", 1999, 8.8, 2155592)
    films[2] = Film.get_instance()
    films[3] = Film.get_instance()
    for counter in films:
        print(counter)
