# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from urllib.request import urlopen
import BoxOffice
import Dialog
import NumItem
import webbrowser
import movieSearch

text = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Gulim'; font-size:9pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:large; font-weight:600;">%영화제목</span>(%연도)</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">%국가 | %상영시간</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">%감독</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">배우</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">%배우들</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">키워드</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">%키워드들</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">%줄거리요약</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><a href="줄거리"><span style=" font-family:'굴림'; text-decoration: underline; color:#0000ff;">전체 줄거리</span></a></p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">수상내역</p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">%수상내역</p>
<p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p>
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><a href="%vodlink"><span style=" font-family:'굴림'; text-decoration: underline; color:#0000ff;">VOD Link</span></a></p></body></html>"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(700, 370))
        MainWindow.setMaximumSize(QtCore.QSize(700, 370))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAnimated(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-4, -2, 711, 371))
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.table_boxoffice = QtWidgets.QTableWidget(self.tab)
        self.table_boxoffice.setGeometry(QtCore.QRect(20, 20, 491, 311))
        self.table_boxoffice.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_boxoffice.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_boxoffice.setShowGrid(True)
        self.table_boxoffice.setObjectName("table_boxoffice")
        self.table_boxoffice.setColumnCount(3)
        self.table_boxoffice.setRowCount(0)
        self.table_boxoffice.setColumnWidth(0,300)
        self.table_boxoffice.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_boxoffice.setSortingEnabled(True)
        item = QtWidgets.QTableWidgetItem()
        self.table_boxoffice.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_boxoffice.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_boxoffice.setHorizontalHeaderItem(2, item)
        self.btn_boxoffice = QtWidgets.QPushButton(self.tab)
        self.btn_boxoffice.setGeometry(QtCore.QRect(570, 230, 75, 61))
        self.btn_boxoffice.setObjectName("btn_boxoffice")
        self.img_boxoffice = QtWidgets.QLabel(self.tab)
        self.img_boxoffice.setGeometry(QtCore.QRect(540, 30, 128, 180))
        self.img_boxoffice.setScaledContents(True)
        self.img_boxoffice.setAlignment(QtCore.Qt.AlignCenter)
        self.img_boxoffice.setObjectName("img_boxoffice")
        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(40, 10, 471, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.img_movie = QtWidgets.QLabel(self.tab_2)
        self.img_movie.setGeometry(QtCore.QRect(540, 60, 128, 160))
        self.img_movie.setScaledContents(True)
        self.img_movie.setAlignment(QtCore.Qt.AlignCenter)
        self.img_movie.setObjectName("img_movie")
        self.btn_movieSearch = QtWidgets.QPushButton(self.tab_2)
        self.btn_movieSearch.setGeometry(QtCore.QRect(520, 10, 51, 23))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("돋보기.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_movieSearch.setIcon(icon)
        self.btn_movieSearch.setObjectName("btn_movieSearch")
        self.btn_movie = QtWidgets.QPushButton(self.tab_2)
        self.btn_movie.setGeometry(QtCore.QRect(570, 230, 75, 61))
        self.btn_movie.setObjectName("btn_movie")
        self.radio_name = QtWidgets.QRadioButton(self.tab_2)
        self.radio_name.setGeometry(QtCore.QRect(70, 40, 90, 16))
        self.radio_name.setChecked(True)
        self.radio_name.setObjectName("radio_name")
        self.radio_director = QtWidgets.QRadioButton(self.tab_2)
        self.radio_director.setGeometry(QtCore.QRect(180, 40, 90, 16))
        self.radio_director.setObjectName("radio_director")
        self.radio_actor = QtWidgets.QRadioButton(self.tab_2)
        self.radio_actor.setGeometry(QtCore.QRect(290, 40, 90, 16))
        self.radio_actor.setObjectName("radio_actor")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(230, 310, 31, 31))
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 310, 31, 31))
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setGeometry(QtCore.QRect(40, 60, 471, 251))
        self.listWidget.setObjectName("listWidget")
        self.radio_keyword = QtWidgets.QRadioButton(self.tab_2)
        self.radio_keyword.setGeometry(QtCore.QRect(390, 40, 90, 16))
        self.radio_keyword.setObjectName("radio_keyword")
        self.tabWidget.addTab(self.tab_2, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.poster = QtWidgets.QLabel(self.tab_4)
        self.poster.setGeometry(QtCore.QRect(10, 10, 321, 331))
        self.poster.setAlignment(QtCore.Qt.AlignCenter)
        self.poster.setObjectName("poster")
        self.movieName = QtWidgets.QLabel(self.tab_4)
        self.movieName.setGeometry(QtCore.QRect(10, 270, 311, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.movieName.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.movieName.setFont(font)
        self.movieName.setAlignment(QtCore.Qt.AlignCenter)
        self.movieName.setObjectName("movieName")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser.setGeometry(QtCore.QRect(330, 10, 371, 331))
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.textBrowser.anchorClicked['QUrl'].connect(self.RedirectionURL)
        self.btn_movieSearch.clicked['bool'].connect(self.PressSearchButton)
        self.pushButton.clicked['bool'].connect(self.DecreasePage)
        self.pushButton_2.clicked['bool'].connect(self.IncreasePage)
        self.listWidget.currentRowChanged['int'].connect(self.ClickMovieList)
        self.btn_movie.clicked['bool'].connect(self.MovieDetail)
        self.btn_boxoffice.clicked['bool'].connect(self.BoxOfficeDetail)
        self.table_boxoffice.currentCellChanged['int','int','int','int'].connect(self.ClickBoxOffice)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.dui = Dialog.Ui_Dialog()
        self.dialog = QtWidgets.QDialog(self.centralwidget)
        self.dui.setupUi(self.dialog)

        self.searchPage = 0
        self.fullPlot = ''

    def RedirectionURL(self, url):
        if url.url() == "줄거리":
            self.dui.plainTextEdit.setPlainText(self.fullPlot)
            self.dialog.exec_()
        else:
            webbrowser.open_new(url.url())

    def IncreasePage(self):
        self.searchPage += 1
        self.SearchMovie()
        totalPage = int(int(movieSearch.totalCount) / 10) + 1
        if self.searchPage == totalPage - 1: self.pushButton_2.setDisabled(True)
        self.pushButton.setEnabled(True)

    def DecreasePage(self):
        self.searchPage -= 1
        self.SearchMovie()
        if self.searchPage == 0: self.pushButton.setDisabled(True)
        self.pushButton_2.setEnabled(True)

    def PressSearchButton(self):
        self.searchPage = 0
        self.SearchMovie()
        self.pushButton.setDisabled(True)
        totalPage = int(int(movieSearch.totalCount) / 10) + 1
        if self.searchPage == totalPage - 1: self.pushButton_2.setDisabled(True)
        else: self.pushButton_2.setEnabled(True)

    def SearchMovie(self):
        self.listWidget.clear()
        if self.radio_director.isChecked():
            movieSearch.searchMovieWithDirector(self.lineEdit.text(), self.searchPage)
        elif self.radio_name.isChecked():
            movieSearch.searchMovieWithTitle(self.lineEdit.text(), self.searchPage)
        elif self.radio_keyword.isChecked():
            movieSearch.searchMovieWithKeyword(self.lineEdit.text(), self.searchPage)
        elif self.radio_actor.isChecked():
            movieSearch.searchMovieWithActor(self.lineEdit.text(), self.searchPage)

        if movieSearch.totalCount == '0': self.listWidget.addItem("검색 결과가 없습니다.")
        else:
            for movie in movieSearch.movieList:
                self.listWidget.addItem("%s(%s)  -  %s" % (movie.dicData["title"], movie.dicData["prodYear"], movie.dicData["directors"][0]))

    def ClickMovieList(self, mIndex):
        if mIndex >= 0:
            movie = movieSearch.movieList[mIndex]
            url = movie.dicData["posters"][0].strip()
            if url != '':
                u = urlopen(url)
                d = u.read()
                u.close()
                image = QtGui.QPixmap()
                image.loadFromData(d)
                self.img_movie.setPixmap(image)
            else:
                self.img_movie.setText("포스터 정보 없음")
        else:
            self.img_movie.setText("포스터 정보 없음")

    def ClickBoxOffice(self, row, column):
        boData = BoxOffice.BOmovieList
        if row >= 0 and boData[row].movieData != None:
            movie = boData[row].movieData
            url = movie.dicData["posters"][0].strip()
            if url != '':
                u = urlopen(url)
                d = u.read()
                u.close()
                image = QtGui.QPixmap()
                image.loadFromData(d)
                self.img_boxoffice.setPixmap(image)
            else:
                self.img_boxoffice.setText("포스터 정보 없음")
        else:
            self.img_boxoffice.setText("포스터 정보 없음")

    def MovieDetail(self):
        index = self.listWidget.currentIndex().row()
        if index >= 0:
            movie = movieSearch.movieList[index]
            #포스터
            url = movie.dicData["posters"][0].strip()
            if url != '':
                u = urlopen(url)
                d = u.read()
                u.close()
                image = QtGui.QPixmap()
                image.loadFromData(d)
                self.poster.setPixmap(image)
            else:
                self.poster.setText("포스터 정보 없음")

            self.movieName.setText(movie.dicData["title"])
            tmpHtml = text.replace("%영화제목", movie.dicData["titleEng"])
            tmpHtml = tmpHtml.replace("%연도", movie.dicData["prodYear"])
            tmpHtml = tmpHtml.replace("%국가", movie.dicData["nation"])
            tmpHtml = tmpHtml.replace("%상영시간", movie.dicData["runtime"])
            dir = ''
            for s in movie.dicData["directors"]:
                dir += s
                dir += ' '
            tmpHtml = tmpHtml.replace("%감독", dir)
            dir = ''
            for a in movie.dicData["actors"]:
                dir += a
                dir += ' '
            tmpHtml = tmpHtml.replace("%배우들", dir)
            dir = ''
            for a in movie.dicData["keywords"]:
                dir += a
                dir += ' '
            tmpHtml = tmpHtml.replace("%키워드들", dir)
            self.fullPlot = movie.dicData["plot"].strip()
            if self.fullPlot != '':
                str = self.fullPlot[0:50] + "..."
                tmpHtml = tmpHtml.replace("%줄거리요약", str)
            else:
                tmpHtml = tmpHtml.replace("%줄거리요약", '')
            dir = ''
            for a in movie.dicData["awards"]:
                dir += a.strip()
                dir += """ <img src="trophy.png" width=12 height=12><br>"""
            tmpHtml = tmpHtml.replace("%수상내역", dir)
            tmpHtml = tmpHtml.replace("%vodlink", movie.dicData['vod'].strip())

            self.textBrowser.setHtml(tmpHtml)

            self.tabWidget.setCurrentIndex(2)

    def BoxOfficeDetail(self):
        boData = BoxOffice.BOmovieList
        index = self.table_boxoffice.currentRow()
        if index >= 0:
            movie = boData[index].movieData
            if movie == None: return
            url = movie.dicData["posters"][0].strip()
            if url != '':
                u = urlopen(url)
                d = u.read()
                u.close()
                image = QtGui.QPixmap()
                image.loadFromData(d)
                self.poster.setPixmap(image)
            else:
                self.poster.setText("포스터 정보 없음")

            self.movieName.setText(movie.dicData["title"])
            tmpHtml = text.replace("%영화제목", movie.dicData["titleEng"])
            tmpHtml = tmpHtml.replace("%연도", movie.dicData["prodYear"])
            tmpHtml = tmpHtml.replace("%국가", movie.dicData["nation"])
            tmpHtml = tmpHtml.replace("%상영시간", movie.dicData["runtime"])
            dir = ''
            for s in movie.dicData["directors"]:
                dir += s
                dir += ' '
            tmpHtml = tmpHtml.replace("%감독", dir)
            dir = ''
            for a in movie.dicData["actors"]:
                dir += a
                dir += ' '
            tmpHtml = tmpHtml.replace("%배우들", dir)
            dir = ''
            for a in movie.dicData["keywords"]:
                dir += a
                dir += ' '
            tmpHtml = tmpHtml.replace("%키워드들", dir)
            self.fullPlot = movie.dicData["plot"].strip()
            if self.fullPlot != '':
                str = self.fullPlot[0:50] + "..."
                tmpHtml = tmpHtml.replace("%줄거리요약", str)
            else:
                tmpHtml = tmpHtml.replace("%줄거리요약", '')
            if movie.dicData["awards"][0].strip() != '':
                dir = ''
                for a in movie.dicData["awards"]:
                    dir += a.strip()
                    dir += """ <img src="trophy.png" width=12 height=12><br>"""
                tmpHtml = tmpHtml.replace("%수상내역", dir)
            else:
                tmpHtml = tmpHtml.replace("%수상내역", '')
            tmpHtml = tmpHtml.replace("%vodlink", movie.dicData['vod'].strip())

            self.textBrowser.setHtml(tmpHtml)

            self.tabWidget.setCurrentIndex(2)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.table_boxoffice.setSortingEnabled(True)
        item = self.table_boxoffice.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "제목"))
        item = self.table_boxoffice.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "현재 관객수"))
        item = self.table_boxoffice.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "총 관객수"))
        self.btn_boxoffice.setText(_translate("MainWindow", "상세 정보"))
        self.img_boxoffice.setText(_translate("MainWindow", "포스터 정보 없음"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "박스오피스"))
        self.img_movie.setText(_translate("MainWindow", "포스터 정보 없음"))
        self.btn_movieSearch.setText(_translate("MainWindow", "검색"))
        self.btn_movie.setText(_translate("MainWindow", "상세 정보"))
        self.radio_name.setText(_translate("MainWindow", "영화명"))
        self.radio_director.setText(_translate("MainWindow", "감독명"))
        self.radio_actor.setText(_translate("MainWindow", "배우"))
        self.radio_keyword.setText(_translate("MainWindow", "키워드"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "영화 검색"))
        self.poster.setText(_translate("MainWindow", "포스터 정보 없음"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "상세 정보"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    BoxOffice.getYesterdayBoxOffice()
    boData = BoxOffice.BOmovieList
    ui.table_boxoffice.setRowCount(len(boData))
    i = 0
    for data in boData:
        ui.table_boxoffice.setItem(i,0,QtWidgets.QTableWidgetItem(data.movieNm))
        ui.table_boxoffice.setItem(i,1,NumItem.NumItem(data.audiCnt))
        ui.table_boxoffice.setItem(i,2,NumItem.NumItem(data.audiAcc))
        i+=1
    sys.exit(app.exec_())

