# import speech_recognition as sr
# import pyttsx3
#
# ans = sr.Recognizer()
#
# with sr.Microphone() as source:
#     try:
#         # ans.energy_threshold = 12000
#         ans.adjust_for_ambient_noise(source, duration=5)
#         ans.dynamic_energy_threshold = True
#         print("listening")
#         audio = ans.listen(source)
#         anstext = ans.recognize_google(audio)
#         print("type:- {}".format(anstext))
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))


# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo
#
# # create the root window
# root = tk.Tk()
# root.title('Tkinter File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')
#
#
# def select_files():
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )
#
#     filenames = fd.askopenfilenames(
#         title='Open files',
#         initialdir='/',
#         filetypes=filetypes)
#
#     showinfo(
#         title='Selected Files',
#         message=filenames
#     )
#
#
# # open button
# open_button = ttk.Button(
#     root,
#     text='Open Files',
#     command=select_files
# )
#
# open_button.pack(expand=True)
#
# root.mainloop()
# # root.destroy()


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
# from PyQt5.QtGui import QIcon
#
#
# class App(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.title = 'PyQt5 file dialogs - pythonspot.com'
#         self.left = 10
#         self.top = 10
#         self.width = 640
#         self.height = 480
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         # self.openFileNameDialog()
#         self.openFileNamesDialog()
#         # self.saveFileDialog()
#
#         self.show()
#
#     def openFileNameDialog(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
#                                                   "All Files (*);;Python Files (*.py)", options=options)
#         if fileName:
#             print(fileName)
#
#     def openFileNamesDialog(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
#                                                 "All Files (*);;Python Files (*.py)", options=options)
#         if files:
#             print(files)
#
#     def saveFileDialog(self):
#         options = QFileDialog.Options()
#         options |= QFileDialog.DontUseNativeDialog
#         fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
#                                                   "All Files (*);;Text Files (*.txt)", options=options)
#         if fileName:
#             print(fileName)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())

# for i in range(4, 33, 1):
#     j=int(random.uniform(6, 12))
#     print('"email" : "{}.{}{}@gmail.com"'.format(''.join(random.choices(string.ascii_lowercase, k = int(random.uniform(6, 12)))),
#                                                ''.join(random.choices(string.ascii_letters, k = int(random.uniform(6, 12)))),
#                                                  int(random.uniform(1, 32))))
#
#     dict["id"]=i
# print('"id" : "{}"'.format(i))
# print('"rollno" : "{}"'.format(int(random.uniform(4, 60))))
# print('"mobile" : "{}"'.format(int(random.random() * 10000000000)))
# print('"std" : "{}"'.format(int(random.uniform(11, 13))))
# print('"physics" : "{}"'.format(int(random.random() * 100)))
# print('"chemistry" : "{}"'.format(int(random.random() * 100)))
# print('"maths" : "{}"'.format(int(random.random() * 100)))
# print('"biology" : "{}"'.format(int(random.random() * 100)))
# print('"computer" : "{}"'.format(int(random.random() * 100)))
# print("\n")
# print('"email" : "{}"'.format(chr(int(random.uniform(65, 91)))))
# print('"email" : "{}"'.format(chr(int(random.uniform(97, 123)))))
import json
import random
import string


i = 4
dict = {
    "id": "{}".format(i),
    "rollno": "{}".format(int(random.uniform(4,60))),
    "username": "{}".format(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k = 12))),
    "password": "{}".format(''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = int(random.uniform(8, 16))))),
    "email": "{}.{}{}@gmail.com".format(''.join(random.choices(string.ascii_lowercase, k = int(random.uniform(6, 12)))),
                                               ''.join(random.choices(string.ascii_letters, k = int(random.uniform(6, 12)))),
                                                 int(random.uniform(1, 32))),
    "name": "{} {}".format(''.join(random.choices(string.ascii_letters, k = int(random.uniform(3, 12)))),
                           ''.join(random.choices(string.ascii_letters, k = int(random.uniform(5, 12))))),
    "mobile": "{}".format(int(random.random() * 10000000000)),
    "std": "{}".format(int(random.uniform(11, 13))),
    "physics": "{}".format(int(random.random() * 100)),
    "chemistry": "{}".format(int(random.random() * 100)),
    "computer": "{}".format(int(random.random() * 100)),
    "biology": "{}".format(int(random.random() * 100)),
    "maths": "{}".format(int(random.random() * 100))
}

lst =[]

for l in range(0, 27, 1):
    random.seed(l*10)

    dict = {
        "id": "{}".format(i),
        "rollno": "{}".format(int(random.uniform(4, 60))),
        "username": "{}".format(
            ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))),
        "password": "{}".format(''.join(
            random.choices(string.ascii_letters + string.punctuation + string.digits, k=int(random.uniform(8, 16))))),
        "email": "{}.{}{}@gmail.com".format(
            ''.join(random.choices(string.ascii_lowercase, k=int(random.uniform(6, 12)))),
            ''.join(random.choices(string.ascii_letters, k=int(random.uniform(6, 12)))),
            int(random.uniform(1, 32))),
        "name": "{} {}".format(''.join(random.choices(string.ascii_letters, k=int(random.uniform(3, 12)))),
                               ''.join(random.choices(string.ascii_letters, k=int(random.uniform(5, 12))))),
        "mobile": "{}".format(int(random.random() * 10000000000)),
        "std": "{}".format(int(random.uniform(11, 13))),
        "physics": "{}".format(int(random.random() * 100)),
        "chemistry": "{}".format(int(random.random() * 100)),
        "computer": "{}".format(int(random.random() * 100)),
        "biology": "{}".format(int(random.random() * 100)),
        "maths": "{}".format(int(random.random() * 100))
    }
    i += 1
    lst.append(dict)

for i in lst:
    print(json.dumps(i, indent=4),",")