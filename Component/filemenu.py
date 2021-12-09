from PyQt5.QtWidgets import QAction, QMenu, QWidget, QFileDialog


class Filemenu(QWidget):

    def __init__(self):
        super(Filemenu, self).__init__()
        self.filemenu = QMenu()

        self.songs=""
        self.openFile = QAction("Open File", self.filemenu)

        self.filemenu.addAction(self.openFile)

        self.openFolder = QAction("Open Folder", self.filemenu)
        self.filemenu.addAction(self.openFolder)

    def launch_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Select Music Files", "",
                                                    "*.mp3;;*.ogg;;*.wav", options=options)
        if files:
            print("files1", type(files))

            index = str(files[0]).rfind("/")
            path = str(files[0])[0:index]
            for file in files:
                print(path,"-",str(file)[index+1:])

    def add_files(self):
        pass