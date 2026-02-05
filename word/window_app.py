import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QLineEdit, QFrame, QHBoxLayout, QMainWindow)
from aсts import *


name_but = ['Добавить', 'Удалить', 'Создать']


class Windows_act(QMainWindow):
    def __init__(self):
        super().__init__()
        self.user = []
        self.names = []
        self.sns = []

        self.setMinimumWidth(434)

        central_widget = QWidget()
        # central_widget = QFrame(self)
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        self.frames = []
        self.line_user = QLineEdit()
        self.line_user.setPlaceholderText('ФИО')
        self.line_post = QLineEdit()
        self.line_post.setPlaceholderText('Должность')

        self.but_box = []

        self.start()

    def start(self):
        self.create_frames(3)
        self.create_but()
        self.basis()


    def create_frames(self, numb):
        for i in range(numb):
            frame = QFrame(self)
            frame.setLayout(QHBoxLayout())
            frame.layout().setContentsMargins(0, 0, 0, 0)
            self.frames.append(frame)
            self.layout.addWidget(frame)


    def create_but(self):
        for i in range(len(name_but)):
            but = QPushButton(name_but[i])
            self.but_box.append(but)


    def basis(self):
        self.frames[0].layout().addWidget(self.line_user)
        self.frames[1].layout().addWidget(self.line_post)

        for i in range(len(name_but)):
            self.frames[2].layout().addWidget(self.but_box[i])

        self.but_box[0].clicked.connect(self.new_line)
        self.but_box[1].clicked.connect(self.del_line)
        self.but_box[2].clicked.connect(self.act_start)


    def new_line(self):
        self.create_frames(1)

        line_name = QLineEdit()
        line_name.setFixedSize(200, 20)
        line_name.setPlaceholderText('Наименование')
        line_sn = QLineEdit()
        line_sn.setPlaceholderText('S/N')
        line_sn.setFixedSize(100, 20)

        last_frame = self.frames[-1]

        last_frame.layout().addWidget(line_name)
        last_frame.layout().addWidget(line_sn)

        self.names.append(line_name)
        self.sns.append(line_sn)


    def del_line(self):
        if len(self.frames) > 3:
            last_frame = self.frames.pop()
            last_frame.deleteLater()

            last_name = self.names.pop()
            last_name.deleteLater()
            last_sn = self.sns.pop()
            last_sn.deleteLater()

            self.adjustSize()

        elif len(self.frames) == 3:
            pass

    def print_data(self):
        self.user.append(self.line_user.text())
        self.user.append(self.line_post.text())

        name_technic = []
        sn_technic = []

        for i in range(len(self.names)):
            name_technic.append(self.names[i].text())

        for i in range(len(self.sns)):
            sn_technic.append(self.sns[i].text())

        for i in range(len(self.user)):
            print(self.user[i])


        if len(name_technic) == len(sn_technic):
            for i in range(len(name_technic)):
                print(name_technic[i])
                print(sn_technic[i])

    def act_start(self):

        self.user.append(self.line_user.text())
        self.user.append(self.line_post.text())
        self.user.reverse()

        name_technic = []
        sn_technic = []

        for i in range(len(self.names)):
            name_technic.append(self.names[i].text())

        for i in range(len(self.sns)):
            sn_technic.append(self.sns[i].text())

        act = Act(self.user, name_technic, sn_technic)
        act.central_command()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Windows_act()
    ex.show()
    sys.exit(app.exec_())
