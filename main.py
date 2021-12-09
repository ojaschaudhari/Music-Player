import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from Component.menubar import Menubar
from Component.playlist import Playlist
from Component.newMenu import NewMenu


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.frame4 = QWidget()
        self.frame3 = QFrame()
        self.frame2 = QFrame()
        self.frame1 = QWidget()
        self.title = "MP3 PLayer"
        self.top = 0
        self.left = 0
        self.width = round(QDesktopWidget().width())
        self.height = round(QDesktopWidget().height())
        self.setStyleSheet("background-color: #343434;"
                           "color: #fff;"
                           "margin: 0;"
                           "padding: 0;")
        self.layout()

    def layout(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        menus = Menubar(self)
        self.setMenuBar(menus)

        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)
        layout = QtWidgets.QHBoxLayout()

        self.frame1.setMaximumHeight(900)
        self.frame1.setFixedWidth(round(self.width / 16))
        self.frame1.setStyleSheet("background-color: #121212")

        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setStyleSheet("background-color: #121212")

        self.frame3.setFrameShape(QFrame.NoFrame)
        self.frame3.setMaximumWidth(round(self.width / 5))
        self.frame3.setStyleSheet("background-color: #121212")

        self.frame4.setMaximumHeight(100)
        self.frame4.setStyleSheet("background-color: #232323")

        sp1 = QSplitter(Qt.Horizontal)
        sp1.addWidget(self.frame1)
        sp1.addWidget(self.frame2)
        sp1.addWidget(self.frame3)

        sp2 = QSplitter(Qt.Vertical)
        sp2.addWidget(sp1)
        sp2.addWidget(self.frame4)
        layout.addWidget(sp2)

        widget.setLayout(layout)

        # --------------------ADDING-MENUS--------------------
        newmenu = NewMenu()
        self.vbox.addWidget (newmenu.groupBox)
        self.frame1.setLayout(self.vbox)

        # --------------------ADDING-Playlist--------------------
        playlist = Playlist(self.frame3)

        # --------------------AUDIO-CONTROL--------------------
        playlist.buttons(self.frame4)
        self.hbox.addWidget(playlist.groupbox)
        self.frame4.setLayout(self.hbox)

        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    window.setWindowOpacity(1)
    window.show()
    sys.exit(App.exec_())
