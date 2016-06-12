from xml.etree import ElementTree
import http.client
import urllib

KOFAkey = '65BE74E17BF7E79BEF4B22625C3AEF67482F3889418423FCF73EEEF93E8E'
listCount = 10

movieList = []
totalCount = 0

class Movie:
    def __init__(self, dic):
        self.dicData = dic

def searchMovieWithTitle(title, page):
    global KOFAkey, listCount, movieList, totalCount
    startCount = page * listCount
    utf8title = urllib.parse.quote(title)
    conn = http.client.HTTPConnection("api.koreafilm.or.kr")
    conn.request("GET", "/openapi-data2/wisenut/search_api/search_xml.jsp?"
                 + "ServiceKey=" + KOFAkey
                 + "&startCount=" + str(startCount) + "&listCoun=" + str(listCount)
                 + "&collection=kmdb_new&detail=Y"
                 + "&title=" + utf8title)
    req = conn.getresponse()
    if req.status != 200: return
    CLen = req.getheader("Content-Length")
    strXML = req.read(CLen).decode('utf-8')
    movieTree = ElementTree.fromstring(strXML)
    
    movieList.clear()
    for child in movieTree.getchildren():
        if child.tag == "Result":
           totalCount = child.get('TotalCount')
           resultList = child.getchildren()
           for movie in resultList:
               dic = dict()
               for e in movie:
                   if e.tag == "DOCID": dic[e.tag] = e.text
                   elif e.tag == "title" : 
                       s = e.text
                       s = s.replace('<!HS>','')
                       s = s.replace('<!HE>',' ')
                       dic[e.tag] = s
                   elif e.tag == "titleEng" : dic[e.tag] = e.text
                   elif e.tag == "prodYear" : dic[e.tag] = e.text
                   elif e.tag == "runtime" : dic[e.tag] = e.text + '분'
                   elif e.tag == "company" : dic[e.tag] = e.text
                   elif e.tag == "plot" : dic[e.tag] = e.text
                   elif e.tag == "rating" : dic[e.tag] = e.text
                   elif e.tag == "nation" : dic[e.tag] = e.text
                   elif e.tag == "posters" :
                       s = e.text
                       s = s.replace('|', '\n')
                       posters = s.splitlines()
                       dic[e.tag] = posters
                   elif e.tag == "Awards1":
                       s = e.text
                       s = s.replace('|', '\n')
                       awards = s.splitlines()
                       dic['awards'] = awards
                   elif e.tag == "keywords":
                       s = e.text
                       s = s.replace(',', '\n')
                       keywords = s.splitlines()
                       dic[e.tag] = keywords
                   elif e.tag == "directors":
                       sub = e.getchildren()
                       directors = []
                       for d in sub:
                           s = d.find("directorNm").text
                           s = s.replace('<!HS>','')
                           s = s.replace('<!HE>',' ')
                           directors.append(s)
                       dic[e.tag] = directors
                   elif e.tag == "vods":
                       sub = e.getchildren()
                       if len(sub) > 0:
                            dic['vod'] = sub[0].find("vodUrl").text
                   elif e.tag == "actors":
                       sub = e.getchildren()
                       n = 0
                       actors = []
                       if len(sub) >= 4: n =4
                       else: n = len(sub)
                       for i in range(0, n):
                           s = sub[i].find("actorNm").text
                           s = s.replace('<!HS>','')
                           s = s.replace('<!HE>','')
                           actors.append(s)
                       dic[e.tag] = actors
               movieList.append(Movie(dic))
    for m in movieList:
        print(m.dicData['title'])
    movieTree.clear()


def searchMovieWithDirector(director, page):
    global KOFAkey, listCount, movieList, totalCount
    startCount = page * listCount
    utf8director = urllib.parse.quote(director)
    conn = http.client.HTTPConnection("api.koreafilm.or.kr")
    conn.request("GET", "/openapi-data2/wisenut/search_api/search_xml.jsp?"
                 + "ServiceKey=" + KOFAkey
                 + "&startCount=" + str(startCount) + "&listCoun=" + str(listCount)
                 + "&collection=kmdb_new&detail=Y"
                 + "&director=" + utf8director)
    req = conn.getresponse()
    if req.status != 200: return
    CLen = req.getheader("Content-Length")
    strXML = req.read(CLen).decode('utf-8')
    movieTree = ElementTree.fromstring(strXML)
    
    movieList.clear()
    for child in movieTree.getchildren():
        if child.tag == "Result":
           totalCount = child.get('TotalCount')
           resultList = child.getchildren()
           for movie in resultList:
               dic = dict()
               for e in movie:
                   if e.tag == "DOCID": dic[e.tag] = e.text
                   elif e.tag == "title" : 
                       s = e.text
                       s = s.replace('<!HS>','')
                       s = s.replace('<!HE>',' ')
                       dic[e.tag] = s
                   elif e.tag == "titleEng" : dic[e.tag] = e.text
                   elif e.tag == "prodYear" : dic[e.tag] = e.text
                   elif e.tag == "runtime" : dic[e.tag] = e.text + '분'
                   elif e.tag == "company" : dic[e.tag] = e.text
                   elif e.tag == "plot" : dic[e.tag] = e.text
                   elif e.tag == "rating" : dic[e.tag] = e.text
                   elif e.tag == "nation" : dic[e.tag] = e.text
                   elif e.tag == "posters" :
                       s = e.text
                       s = s.replace('|', '\n')
                       posters = s.splitlines()
                       dic[e.tag] = posters
                   elif e.tag == "Awards1":
                       s = e.text
                       s = s.replace('|', '\n')
                       awards = s.splitlines()
                       dic['awards'] = awards
                   elif e.tag == "keywords":
                       s = e.text
                       s = s.replace(',', '\n')
                       keywords = s.splitlines()
                       dic[e.tag] = keywords
                   elif e.tag == "directors":
                       sub = e.getchildren()
                       directors = []
                       for d in sub:
                           s = d.find("directorNm").text
                           s = s.replace('<!HS>','')
                           s = s.replace('<!HE>',' ')
                           directors.append(s)
                       dic[e.tag] = directors
                   elif e.tag == "vods":
                       sub = e.getchildren()
                       if len(sub) > 0:
                            dic['vod'] = sub[0].find("vodUrl").text
                   elif e.tag == "actors":
                       sub = e.getchildren()
                       n = 0
                       actors = []
                       if len(sub) >= 4: n =4
                       else: n = len(sub)
                       for i in range(0, n):
                           s = sub[i].find("actorNm").text
                           s = s.replace('<!HS>','')
                           s = s.replace('<!HE>','')
                           actors.append(s)
                       dic[e.tag] = actors
               movieList.append(Movie(dic))
    for m in movieList:
        print(m.dicData['title'])
    movieTree.clear()


def searchMovieWithKeyword(keyword, page):
    global KOFAkey, listCount, movieList, totalCount
    startCount = page * listCount
    utf8keyword = urllib.parse.quote(keyword)
    conn = http.client.HTTPConnection("api.koreafilm.or.kr")
    conn.request("GET", "/openapi-data2/wisenut/search_api/search_xml.jsp?"
                 + "ServiceKey=" + KOFAkey
                 + "&startCount=" + str(startCount) + "&listCoun=" + str(listCount)
                 + "&collection=kmdb_new&detail=Y"
                 + "&keyword=" + utf8keyword)
    req = conn.getresponse()
    if req.status != 200: return
    CLen = req.getheader("Content-Length")
    strXML = req.read(CLen).decode('utf-8')
    movieTree = ElementTree.fromstring(strXML)
    
    movieList.clear()
    for child in movieTree.getchildren():
        if child.tag == "Result":
           totalCount = child.get('TotalCount')
           resultList = child.getchildren()
           for movie in resultList:
               dic = dict()
               for e in movie:
                   if e.tag == "DOCID": dic[e.tag] = e.text
                   elif e.tag == "title" : 
                       s = e.text
                       s = s.replace('<!HS>','')
                       s = s.replace('<!HE>',' ')
                       dic[e.tag] = s
                   elif e.tag == "titleEng" : dic[e.tag] = e.text
                   elif e.tag == "prodYear" : dic[e.tag] = e.text
                   elif e.tag == "runtime" : dic[e.tag] = e.text + '분'
                   elif e.tag == "company" : dic[e.tag] = e.text
                   elif e.tag == "plot" : dic[e.tag] = e.text
                   elif e.tag == "rating" : dic[e.tag] = e.text
                   elif e.tag == "nation" : dic[e.tag] = e.text
                   elif e.tag == "posters" :
                       s = e.text
                       s = s.replace('|', '\n')
                       posters = s.splitlines()
                       dic[e.tag] = posters
                   elif e.tag == "Awards1":
                       s = e.text
                       s = s.replace('|', '\n')
                       awards = s.splitlines()
                       dic['awards'] = awards
                   elif e.tag == "keywords":
                       s = e.text
                       s = s.replace(',', '\n')
                       keywords = s.splitlines()
                       dic[e.tag] = keywords
                   elif e.tag == "directors":
                       sub = e.getchildren()
                       directors = []
                       for d in sub:
                           s = d.find("directorNm").text
                           s = s.replace('<!HS>','')
                           s = s.replace('<!HE>',' ')
                           directors.append(s)
                       dic[e.tag] = directors
                   elif e.tag == "vods":
                       sub = e.getchildren()
                       if len(sub) > 0:
                            dic['vod'] = sub[0].find("vodUrl").text
                   elif e.tag == "actors":
                       sub = e.getchildren()
                       n = 0
                       actors = []
                       if len(sub) >= 4: n =4
                       else: n = len(sub)
                       for i in range(0, n):
                           s = sub[i].find("actorNm").text
                           s = s.replace('<!HS>','')
                           s = s.replace('<!HE>','')
                           actors.append(s)
                       dic[e.tag] = actors
               movieList.append(Movie(dic))
    for m in movieList:
        print(m.dicData['title'])
    movieTree.clear()


def searchMovieWithActor(actor, page):
    global KOFAkey, listCount, movieList, totalCount
    startCount = page * listCount
    utf8actor = urllib.parse.quote(actor)
    conn = http.client.HTTPConnection("api.koreafilm.or.kr")
    conn.request("GET", "/openapi-data2/wisenut/search_api/search_xml.jsp?"
                 + "ServiceKey=" + KOFAkey
                 + "&startCount=" + str(startCount) + "&listCoun=" + str(listCount)
                 + "&collection=kmdb_new&detail=Y"
                 + "&actor=" + utf8actor)
    req = conn.getresponse()
    if req.status != 200: return
    CLen = req.getheader("Content-Length")
    strXML = req.read(CLen).decode('utf-8')
    movieTree = ElementTree.fromstring(strXML)
    
    movieList.clear()
    for child in movieTree.getchildren():
        if child.tag == "Result":
           totalCount = child.get('TotalCount')
           resultList = child.getchildren()
           for movie in resultList:
               dic = dict()
               for e in movie:
                   if e.tag == "DOCID": dic[e.tag] = e.text
                   elif e.tag == "title" : 
                       s = e.text
                       s = s.replace('<!HS>','')
                       s = s.replace('<!HE>',' ')
                       dic[e.tag] = s
                   elif e.tag == "titleEng" : dic[e.tag] = e.text
                   elif e.tag == "prodYear" : dic[e.tag] = e.text
                   elif e.tag == "runtime" : dic[e.tag] = e.text + '분'
                   elif e.tag == "company" : dic[e.tag] = e.text
                   elif e.tag == "plot" : dic[e.tag] = e.text
                   elif e.tag == "rating" : dic[e.tag] = e.text
                   elif e.tag == "nation" : dic[e.tag] = e.text
                   elif e.tag == "posters" :
                       s = e.text
                       s = s.replace('|', '\n')
                       posters = s.splitlines()
                       dic[e.tag] = posters
                   elif e.tag == "Awards1":
                       s = e.text
                       s = s.replace('|', '\n')
                       awards = s.splitlines()
                       dic['awards'] = awards
                   elif e.tag == "keywords":
                       s = e.text
                       s = s.replace(',', '\n')
                       keywords = s.splitlines()
                       dic[e.tag] = keywords
                   elif e.tag == "directors":
                       sub = e.getchildren()
                       directors = []
                       for d in sub:
                           s = d.find("directorNm").text
                           s = s.replace('<!HS>','')
                           s = s.replace('<!HE>',' ')
                           directors.append(s)
                       dic[e.tag] = directors
                   elif e.tag == "vods":
                       sub = e.getchildren()
                       if len(sub) > 0:
                            dic['vod'] = sub[0].find("vodUrl").text
                   elif e.tag == "actors":
                       sub = e.getchildren()
                       n = 0
                       actors = []
                       if len(sub) >= 4: n =4
                       else: n = len(sub)
                       for i in range(0, n):
                           s = sub[i].find("actorNm").text
                           s = s.replace('<!HS>','')
                           s = s.replace('<!HE>','')
                           actors.append(s)
                       dic[e.tag] = actors
               movieList.append(Movie(dic))
    for m in movieList:
        print(m.dicData['title'])
    movieTree.clear()


def getMovieData(title, openDate):
    global KOFAkey
    utf8title = urllib.parse.quote(title)
    conn = http.client.HTTPConnection("api.koreafilm.or.kr")
    conn.request("GET", "/openapi-data2/wisenut/search_api/search_xml.jsp?"
                 + "ServiceKey=" + KOFAkey
                 + "&collection=kmdb_new&detail=Y"
                 + "&title=" + utf8title)
    req = conn.getresponse()
    if req.status != 200: return None
    CLen = req.getheader("Content-Length")
    if CLen != None: CLen=int(CLen)
    strXML = req.read(CLen).decode('utf-8')
    movieTree = ElementTree.fromstring(strXML)
    
    rlsDate = None
    for child in movieTree.getchildren():
        retMovie = None
        if child.tag == "Result":
           resultList = child.getchildren()
           for movie in resultList:
               dic = dict()
               for e in movie:
                   if e.tag == "DOCID": dic[e.tag] = e.text
                   elif e.tag == "title" : 
                       s = e.text
                       s = s.replace('<!HS>','')
                       s = s.replace('<!HE>',' ')
                       dic[e.tag] = s
                   elif e.tag == "titleEng" : dic[e.tag] = e.text
                   elif e.tag == "prodYear" : dic[e.tag] = e.text
                   elif e.tag == "runtime" : dic[e.tag] = e.text + '분'
                   elif e.tag == "company" : dic[e.tag] = e.text
                   elif e.tag == "plot" : dic[e.tag] = e.text
                   elif e.tag == "rating" : dic[e.tag] = e.text
                   elif e.tag == "nation" : dic[e.tag] = e.text
                   elif e.tag == "posters" :
                       s = e.text
                       s = s.replace('|', '\n')
                       posters = s.splitlines()
                       dic[e.tag] = posters
                   elif e.tag == "Awards1":
                       s = e.text
                       s = s.replace('|', '\n')
                       awards = s.splitlines()
                       dic['awards'] = awards
                   elif e.tag == "keywords":
                       s = e.text
                       s = s.replace(',', '\n')
                       keywords = s.splitlines()
                       dic[e.tag] = keywords
                   elif e.tag == "directors":
                       sub = e.getchildren()
                       directors = []
                       for d in sub:
                           s = d.find("directorNm").text
                           s = s.replace('<!HS>','')
                           s = s.replace('<!HE>',' ')
                           directors.append(s)
                       dic[e.tag] = directors
                   elif e.tag == "vods":
                       sub = e.getchildren()
                       if len(sub) > 0:
                            dic['vod'] = sub[0].find("vodUrl").text
                   elif e.tag == "actors":
                       sub = e.getchildren()
                       n = 0
                       actors = []
                       if len(sub) >= 4: n =4
                       else: n = len(sub)
                       for i in range(0, n):
                           s = sub[i].find("actorNm").text
                           s = s.replace('<!HS>','')
                           s = s.replace('<!HE>','')
                           actors.append(s)
                       dic[e.tag] = actors
                   elif e.tag == "repRlsDate": 
                       rlsDate = e.text
                       rlsDate = rlsDate.replace(' ','')
               if rlsDate == openDate:
                    return Movie(dic)
    movieTree.clear()
    return None