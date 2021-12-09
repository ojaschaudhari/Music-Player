from PyQt5.QtWidgets import QGroupBox, QPushButton, QVBoxLayout
from PyQt5 import QtGui
from PyQt5 import QtCore
from Component.filemenu import Filemenu
import design


class NewMenu(Filemenu):
    def __init__(self):
        super(NewMenu, self).__init__()
        self.savebtn = QPushButton("Save")
        self.filebtn = QPushButton()
        self.searchbtn = QPushButton()
        self.playlistbtn = QPushButton()
        self.groupBox = QGroupBox()
        self.gridLayout = QVBoxLayout()
        self.menus()

    def menus(self):
        self.groupBox.setFixedHeight(400)

        self.filebtn.setIcon(QtGui.QIcon('file1.png'))
        self.filebtn.setMenu(self.filemenu)
        # print("before press")
        self.songs = self.openFile.triggered.connect(lambda: self.launch_file_dialog())
        # print("after press")
        # self.openFile.triggered
        self.gridLayout.addWidget(self.filebtn)

        self.searchbtn.setIcon(QtGui.QIcon('search1.png'))
        self.gridLayout.addWidget(self.searchbtn)

        self.playlistbtn.setIcon(QtGui.QIcon('playlist1.png'))
        self.gridLayout.addWidget(self.playlistbtn)

        self.set_btn()
        self.groupBox.setLayout(self.gridLayout)

    def set_btn(self):
        btnlst = [self.filebtn, self.searchbtn, self.playlistbtn]

        for btn in btnlst:
            btn.setIconSize(QtCore.QSize(80, 80))
            btn.setObjectName("btn2")
            btn.setStyleSheet(design.stylesheet)
