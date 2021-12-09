import  os
from PyQt5.QtWidgets import QMenuBar, QApplication, QMainWindow, QAction, QMenu, QFileDialog


class Menubar(QMenuBar):
    def __init__(self, parent=None):
        super(Menubar, self).__init__(parent)

        # --------------------FILE--------------------
        # file = QMenu("File", self)
        file = self.addMenu("File")
        # file.addMenu("Edit")

            # --------------------Add MENU--------------------
        # mfile = file.addMenu("Add a Media File")
        openFile = QAction("Open File", file)
        openFile.triggered.connect(lambda: self.launchFileDialog())
        file.addAction(openFile)
        # plist = file.addMenu("Add a Playlist")

            # --------------------Exit MENU--------------------
        exit = QAction("Exit", self)

        exit.setShortcut("Ctrl+Q")
        exit.triggered.connect(lambda : QApplication.quit())
        file.addAction(exit)
        self.addMenu(file)

        # --------------------OPEN--------------------
        # open = QMenu("Open", self)
        open = self.addMenu("Open")
        self.addMenu(open)

        # --------------------SAVE--------------------
        save = self.addMenu("Save")
        self.addMenu(save)

    def launchFileDialog(self):
        print("open file")
        file_filter = 'Data File(*.mp3, *.ogg, *.flac, *.wav)'
        response = QFileDialog.getOpenFileNames(
            caption="Select a Media File",
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Data File(*.mp3, *.ogg, *.flac, *.wav)'
        )
        print(response)
        print("Close open")
        return response