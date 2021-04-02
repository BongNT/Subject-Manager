from tkinter.ttk import *
from tkinter import *
from tkinter.tix import *


class Subject(Label):
    def __init__(self, parent, data):
        # 1 subject co thể có tiết thực hành, bài tập, hoặc chỉ có thực hành
        Label.__init__(self, parent)

        self.get_data(data)
        self.initUI()

    # data of one subject
    def get_data(self, data):
        self.subject = data[1]
        self.subject_name = data[2]
        self.credit = data[3]
        self.subject_id = data[4]
        self.teacher_name = data[5]
        self.number_of_student = data[6]
        self.weekday = int(data[8])
        self.time = data[9].split("-")
        self.place = data[10]
        self.note = data[11]
        self.grid(column=self.weekday, row=self.time[0], rowspan=int(self.time[1]) - int(self.time[0]) + 1,
                  sticky="nsew")

    @property
    def get_info(self):
        return "subject_name:{}\nsubject_id:{}\nteacher_name:{}\nnumber_of_student:{}\ncredit:{}\nnote:{}".format(
            self.subject, self.subject_id, self.teacher_name
            , self.number_of_student, self.credit, self.note)

    def initUI(self):
        info_text = "{}\n{}".format(self.subject_name, self.place)
        self.configure(text="{}\n{}".format(self.subject_name, self.place), background="yellow", relief=GROOVE,
                       font='calibri 10')
        self.popup_menu = Menu(self, tearoff=False)
        self.popup_menu.add_command(label="Delete Subject", command=self.delete_subject)
        self.popup_menu.add_command(label="Change color", command=self.change_color)
        self.bind("<Button-3>", self.show_popup_menu)

    def show_popup_menu(self, event):
        self.popup_menu.tk_popup(event.x_root, event.y_root)

    def delete_subject(self):
        self.destroy()

    def change_color(self):
        pass


if __name__ == "__main__":
    root = Tk()
    root.geometry()
    app = Subject(root, ("djaksjdlkajdlkasdsdasdasfsafsaggsfsa", "gd3", "1-3", "4"))

    root.mainloop()
