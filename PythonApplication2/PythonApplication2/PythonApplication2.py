import movieSearch
import getBoxOffice
import sendMail
import BookMarkModule

getBoxOffice.getYesterdayBoxOffice()
movieSearch.searchMovieWithActor('필립 세이모어', 0)
#BookMarkModule.insert(movieSearch.movieList[i].dicData)
BookMarkModule.Init()