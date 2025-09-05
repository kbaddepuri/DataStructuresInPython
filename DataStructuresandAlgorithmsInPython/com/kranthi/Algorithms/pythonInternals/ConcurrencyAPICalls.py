from future.utils import reraise


class Show(object):
    def __init__(self, title, date, rating, synopsis):
        self.title = title
        self.date = date
        self.rating = rating
        self.synopsis = synopsis


    def getName(self):
        return self.title

class Movie(Show):
    def __init__(self, runtime, title, date, rating, synopsis):
        super().__init__(title, date, rating, synopsis)
        self.runtime = runtime



class TVShow(Show):
    def __init__(self, seasons, title, date, rating, synopsis):
        super().__init__(title, date, rating, synopsis)
        self.seasons = seasons

    def getName(self):
        return self.title



class Titanic(Movie, TVShow):
    def __init__(self, runtime, title, date, rating, synopsis):
    pass

    def test(self):
        getName()
