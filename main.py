import os
from PyQt6 import QtCore, QtGui, QtWidgets
from pytubefix import YouTube

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(676, 483)
        MainWindow.setStyleSheet("QMainWindow{background-color:black}")

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create label for header project
        self.header_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.header_label.setGeometry(QtCore.QRect(210, 5, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Script")
        font.setBold(True)
        font.setItalic(True)
        self.header_label.setFont(font)
        self.header_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.header_label.setStyleSheet("color: orange")
        self.header_label.setIndent(35)
        self.header_label.setObjectName("header_label")
        self.header_label_1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.header_label_1.setGeometry(QtCore.QRect(310, 30, 161, 41))
        self.header_label_1.setFont(font)
        self.header_label_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.header_label_1.setStyleSheet("color: orange")
        self.header_label_1.setObjectName("header_label_1")

        # create a label and line edit for get YouTube video url for download
        # create line edit
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 110, 440, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setStyleSheet("background-color: white;color:black")
        # create label
        self.url_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.url_label.setGeometry(QtCore.QRect(70, 110, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.url_label.setFont(font)
        self.url_label.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ForbiddenCursor))
        self.url_label.setStyleSheet("color: white;")
        self.url_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.url_label.setObjectName("url_label")

        # create download button for download audio
        self.download_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(280, 400, 100, 35))
        self.download_button.setFont(font)
        self.download_button.setStyleSheet("background-color: red;color:black")
        self.download_button.setObjectName("download_button")
        self.download_button.clicked.connect(self.download_audio)

        # create text browser for show Message and Error
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(140, 200, 400, 160))
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Audio Downloader"))
        self.header_label.setText(_translate("MainWindow", "Audio"))
        self.header_label_1.setText(_translate("MainWindow", "Downloader"))
        self.url_label.setText(_translate("MainWindow", "URL :"))
        self.download_button.setText(_translate("MainWindow", "Download"))

    def download_audio(self):
        try:
            yt = YouTube(url=self.lineEdit.text())
            audio_query = yt.streams.filter(only_audio=True)[1]
            audio_query.download(output_path=os.path.dirname(os.path.abspath(__name__)) + r"\Downloads")
            self.textBrowser.setText(f"Title: {yt.title}\n\nNumber of viewed: {yt.views}\n\n")
        except Exception as err:
            self.textBrowser.setText(f"{err.__class__.__name__}:\n{err}")
        else:
            self.textBrowser.append("Download Successfully")

    @staticmethod
    def check_folder_downloads():
        if "Downloads" not in os.listdir(os.path.dirname(os.path.abspath(__name__))):
            os.mkdir(os.path.dirname(os.path.abspath(__name__)) + r"\Downloads")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.check_folder_downloads()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
