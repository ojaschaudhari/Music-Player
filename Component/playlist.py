import os
import vlc
import design
import fnmatch
from PyQt5.QtWidgets import QFrame, QListWidget, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont
from Component.buttons import Buttons
from Component.filemenu import Filemenu


class Playlist(QFrame, Buttons, Filemenu):
    old_media = ""
    rootpath = "/home/ok/Music"
    patterns = ["*.mp3", "*.ogg", "*.flac", "*.wav"]

    def __init__(self, parent=None):
        super(Playlist, self).__init__()
        self.playlist = QListWidget(parent)
        self.createplaylist()
        self.player = vlc.MediaPlayer()
        self.setactions()


    def createplaylist(self):
        self.playlist.setFixedSize(QDesktopWidget().width(), QDesktopWidget().height())
        self.playlist.setFont(QFont("ds-digital", 12))
        self.playlist.setStyleSheet(design.stylesheet)
        self.playlist.setObjectName("list")

        for root, dirs, files in os.walk(self.rootpath):
            i = 0
            for pattern in self.patterns:
                for filename in fnmatch.filter(files, pattern):
                    self.playlist.insertItem(i, filename)
                    i += 1

    def setactions(self):
        self.play.clicked.connect(lambda: self.player_play())
        self.forward.clicked.connect(lambda: self.play_next())
        self.backward.clicked.connect(lambda: self.play_back())
        self.repeat.clicked.connect(lambda: self.play_back())
        self.volume.clicked.connect(lambda: self.play_back())

    def player_play(self):
        if self.playlist.currentItem() is None:
            self.playlist.setCurrentRow(0)
            self.media_play()

        else:
            value = self.playlist.currentItem().text()

            if self.old_media != value:
                # self.player.set_media(media)
                self.media_play()
                self.pause_state = False

            else:
                if self.pause_state:
                    self.player.play()
                    self.play.setIcon(QIcon('pause.png'))
                    self.pause_state = False

                else:
                    self.player.pause()
                    self.play.setIcon(QIcon('play.png'))
                    self.pause_state = True

            self.old_media = value

    def play_next(self):
        if self.playlist.currentRow() + 1 == self.playlist.count():
            self.playlist.setCurrentRow(0)
            self.media_play()

        else:
            self.playlist.setCurrentRow(self.playlist.currentRow() + 1)
            self.media_play()

    def play_back(self):
        if self.playlist.currentRow() <= 0:
            self.playlist.setCurrentRow(0)
            self.media_play()

        else:
            self.playlist.setCurrentRow(self.playlist.currentRow() - 1)
            self.media_play()

    def media_play(self):
        media = vlc.Media(self.rootpath + "/" + self.playlist.currentItem().text())
        self.player.set_media(media)
        self.player.play()
        self.play.setIcon(QIcon('pause.png'))
