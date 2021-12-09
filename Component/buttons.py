import design
from PyQt5.QtWidgets import QPushButton, QGroupBox, QGridLayout
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon


class Buttons:
    def __init__(self, parent=None):
        super(Buttons, self).__init__()
        self.play = QPushButton(parent)
        self.forward = QPushButton(parent)
        self.backward = QPushButton(parent)
        self.volume = QPushButton(parent)
        self.repeat = QPushButton(parent)
        self.groupbox = QGroupBox()
        self.gridLayout = QGridLayout()
        self.forward = QPushButton()
        self.backward = QPushButton()
        self.volume = QPushButton()
        self.repeat = QPushButton()
        self.pause_state = True
    
    def buttons(self, parent):
        self.groupbox.setFixedWidth(500)

        self.play.setIcon(QtGui.QIcon('play.png'))
        # self.play.clicked.connect(lambda: self.player_play())
        self.gridLayout.addWidget(self.play, 0, 2)

        self.forward.setIcon(QIcon('next.png'))
        # self.forward.clicked.connect(lambda: self.play_next())
        self.gridLayout.addWidget(self.forward, 0, 3)

        self.backward.setIcon(QIcon('back.png'))
        # self.backward.clicked.connect(lambda: self.play_back())
        self.gridLayout.addWidget(self.backward, 0, 1)

        self.repeat.setIcon(QIcon('repeat.png'))
        # self.repeat.clicked.connect(lambda: self.play_back())
        self.gridLayout.addWidget(self.repeat, 0, 4)

        self.volume.setIcon(QIcon('volume.png'))
        # self.volume.clicked.connect(lambda: self.play_back())
        self.gridLayout.addWidget(self.volume, 0, 0)

        self.set_icon()
        self.groupbox.setLayout(self.gridLayout)
    
    def set_icon(self):
        btnlist = [self.repeat, self.backward, self.play, self.forward, self.volume]
        for btn in btnlist:
            btn.setObjectName("btn1")
            btn.setStyleSheet(design.stylesheet)
            btn.setFixedSize(60, 60)
            btn.setIconSize(QtCore.QSize(50, 50))
            