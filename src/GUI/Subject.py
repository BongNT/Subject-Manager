
from tkinter.ttk import *

from tkinter import *
from tkinter import colorchooser
from tkinter.tix import *


class Subject(Label):
    def __init__(self, parent, data, color="yellow"):
        # 1 subject_id co thể có tiết thực hành, bài tập, hoặc chỉ có thực hành
        Label.__init__(self, parent)
        self.parent = parent
        self.get_data(data)
        self.initUI(color)

    # data of one subject_id
    def get_data(self, data):
        self.subject_id = data[0]
        self.subject_name = data[1]
        self.credit = data[2]
        self.class_id = data[3]
        self.teacher_name = data[4]
        self.number_of_student = data[5]
        self.weekday = int(data[6])
        self.time = data[7].split("-")
        self.place = data[8]
        self.type = data[9]

        self.grid(column=self.weekday -1 if self.weekday !=0 else 7, row=self.time[0], rowspan=int(self.time[1]) - int(self.time[0]) + 1,
                  sticky="nsew")
        info = Balloon(self,bg="red")
        info.bind_widget(self, balloonmsg=self.get_info())
        info.message.config(bg="white")

    def get_info(self):
        return "Tên môn : {}\nMã môn học : {}\nGiảng viên : {}\nSố lượng sinh viên :{}\nTín chỉ : {}\nNhóm : {}".format(
            self.subject_id, self.class_id, self.teacher_name
            , self.number_of_student, self.credit, self.type)

    def initUI(self, color):
        info_text = "{}\n{}".format(self.subject_name, self.place)
        self.configure(text="{}\n{}".format(self.subject_name, self.place), background=color, relief=GROOVE,
                       font='calibri 10')
        self.popup_menu = Menu(self, tearoff=False)
        self.popup_menu.add_command(label="Xóa", command=self.delete_subject)
        self.popup_menu.add_command(label="Đổi màu", command=self.change_color)
        self.bind("<Button-3>", self.show_popup_menu)

    def show_popup_menu(self, event):
        self.popup_menu.tk_popup(event.x_root, event.y_root)

    def delete_subject(self):
        self.parent.subject_manager.delete(self.class_id)

    def set_color(self, color):
        self.configure(background=color)

    def change_color(self):
        subject_manager = self.parent.subject_manager

        color_picker = colorchooser.askcolor()[1]
        print(color_picker)
        # kiem tra xem co mau nao trung voi mau da chon
        for class_id, color  in subject_manager.color_manager:
            if color == color_picker:
                print("error, Mau nay da duoc dung")
        for subject in subject_manager.list_subject:
            if self.class_id == subject.class_id:
                subject.set_color(color_picker)

