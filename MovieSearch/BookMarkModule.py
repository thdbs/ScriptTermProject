import BookMarkIO

BookMarkedList = []
FavoriteDirectors = []
FavoriteActors = []

class MarkedMovie:
    def __init__(self, title, prodYear, directors, actors, DOCID, movieData = None):
        self.title = title
        self.prodYear = prodYear
        self.directors = directors
        self.actors = actors
        self.DOCID = DOCID
        self.movieData = movieData

def Init():
    global BookMarkedList, FavoriteDirectors, FavoriteActors
    BookMarkedList.clear()
    FavoriteActors.clear()
    FavoriteDirectors.clear()
    mvs = BookMarkIO.getBookMarkedMv()
    if len(mvs) == 0:
        return
    mvs = mvs.rsplit('|')
    for mv in mvs:
        if mv == '': break
        l = mv.rsplit('+')
        BookMarkedList.append(MarkedMovie(l[0], l[1], l[2], l[3], l[4]))
    d, a = BookMarkIO.getTopDirectorsNActors()
    FavoriteDirectors = d.rsplit('+')
    FavoriteDirectors.pop()
    FavoriteActors = a.rsplit('+')
    FavoriteActors.pop()


def insert(dicData):
    directors = dicData["directors"]
    director = ""
    for i in range(0, len(directors)):
        if( i == len(directors) - 1):
            director += directors[i]
            break;
        director += directors[i] + ","
    actors = dicData["actors"]
    actor = ""
    for i in range(0, len(actors)):
        if(i == len(actors) - 1):
            actor += actors[i]
            break;
        actor += actors[i] + ","
    BookMarkIO.insert(dicData["title"], dicData["prodYear"], director, actor, dicData["DOCID"])
    Init()

def delete(DOCID):
    BookMarkIO.delete(DOCID)
    Init()