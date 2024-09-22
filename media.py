class Media:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def to_dict(self):
        return {
            "title": self.title,
            "director": self.director,
            "year": self.year
        }

    def __str__(self):
        return f"Название: {self.title}, режиссер: {self.director}, год: {self.year}"



class Movie(Media):
    def __init__(self, title, director, year, duration):
        super().__init__(title, director, year)  
        self.duration = duration
# ААА
    def to_dict(self):
        movie_dict = super().to_dict() 
        movie_dict.update({
            "duration": self.duration
        })
        return movie_dict

    def __str__(self):
        return f"Фильм: {self.title}, режиссер: {self.director}, год: {self.year}, длительность: {self.duration} мин."


class TVSeries(Media):
    def __init__(self, title, director, year, seasons, episodes):
        super().__init__(title, director, year)  
        self.seasons = seasons
        self.episodes = episodes

    def to_dict(self):
        series_dict = super().to_dict()  
        series_dict.update({
            "seasons": self.seasons,
            "episodes": self.episodes
        })
        return series_dict

    def __str__(self):
        return f"Сериал: {self.title}, режиссер: {self.director}, год: {self.year}, сезонов: {self.seasons}, эпизодов: {self.episodes}"
