from xml.etree import ElementTree
import http.client
import datetime
from movieSearch import getMovieData

BOmovieList = []
KOBISkey = '6e4d4f33a080727cbdcb4dad0eb05ee7'

class BOmovie:
    def __init__(self, movieNm, movieCd, audiCnt, audiAcc, movieData):
        self.movieNm = movieNm
        self.movieCd = movieCd
        self.audiCnt = audiCnt
        self.audiAcc = audiAcc
        self.movieData = movieData

def getYesterdayBoxOffice():
    global KOBISkey, BOmovieList
    yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
    strYesterday = yesterday.strftime('%y%m%d')
    conn = http.client.HTTPConnection("kobis.or.kr")
    conn.request("GET","/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?"
                 + "key="+ KOBISkey +"&targetDt=20" + strYesterday +"&multiMovieYn=Y")
    req = conn.getresponse()
    print(req.status)
    CLen = req.getheader("Content-Length")
    if CLen != None: CLen=int(CLen)
    s = req.read(CLen).decode('utf-8')
    boxOffice = None
    try:
        boxOffice = ElementTree.fromstring(s)
    except Exception:
        pirnt("Error")
    openDt = None
    for child in boxOffice.getchildren():
        if child.tag == "dailyBoxOfficeList":
            boxOfficeList = child.getchildren()
            for movie in boxOfficeList:
                movieNm, movieCd, audiCnt, audiAcc = None, None, None, None
                for e in movie.getchildren():
                    if e.tag == "movieNm": movieNm = e.text
                    elif e.tag == "movieCd": movieCd = e.text
                    elif e.tag == "audiCnt": audiCnt = e.text
                    elif e.tag == "audiAcc" : audiAcc = e.text
                    elif e.tag == "openDt" : openDt = e.text
                openDt = openDt.replace('-', '')
                print(movieNm)
                movieData = getMovieData(movieNm.replace(' ', ''), openDt)
                BOmovieList.append(BOmovie(movieNm, movieCd, audiCnt, audiAcc, movieData))
    for d in BOmovieList:
        if d.movieData != None:
            print(d.movieData.dicData['title'])