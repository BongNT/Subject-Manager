from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from Subject import Subject
from SubjectManager import SubjectManager

class Timetable(Frame):
    def __init__(self, parent, isConfiged = True):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.subject_manager = SubjectManager(self)
    def initUI(self):
        # self.parent.title("timetable")

        Style().configure("", padding=(0, 0, 0, 0), font='Calibri 10')
        # http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        # rows là chiếm cả 1 hàng
        for i in range(9):
            self.grid_columnconfigure(i, weight=1)
        for i in range(15):
            self.grid_rowconfigure(i, weight=1)

        # label_morning = Label(self, height = 2, width = 10,background = "pale violet red", relief=GROOVE,text = "Sáng")
        # label_morning.grid(row=1,column=0, rowspan=6,sticky ="nsew")
        # label_afternoon = Label(self, height=2, width=10, background="cyan2", relief=GROOVE, text="Chiều")
        # label_afternoon.grid(row =7, column=0,rowspan = 6,sticky ="nsew")
        label_time = Label(self, height=2, width=7, background="yellow", relief=GROOVE, text="Tiết", )
        label_time.grid(row=0, column=0, sticky="nsew")


        for i in range(1, 15):
            temp_label = Label(self, height=2, width=10, background="white", relief=GROOVE, font='calibri 7',
                               text="{} ({}h - {}h)".format(i, i + 6, i + 7))
            temp_label.grid(row=i, column=0, sticky="nsew")

        for i in range(2, 9):
            temp_label = Label(self, background="yellow", relief=GROOVE, text=("Thứ " + str(i)) if i < 8 else "Chủ Nhật")
            temp_label.grid(row=0, column=i-1, sticky="nsew")
        #  create popup
        self.popup_menu = Menu(self, tearoff=False)
        self.popup_menu.add_command(label="Delete all subject", command=self.delete_all_subjects)
        self.bind("<Button-3>", self.show_popup_menu)

    def insert_subject_from_student_id(self,student_id):
        self.subject_manager.create_list_subject(student_id)

    def insert_subject(self, list_data):
        for data in list_data:
            self.subject_manager.append(data)

    def delete_all_subjects(self):
        self.subject_manager.delete_all()

    def show_popup_menu(self, event=None):
        self.popup_menu.tk_popup(event.x_root, event.y_root)

if __name__ == "__main__":
    root = Tk()

    root.geometry()
    app = Timetable(root)
    app.pack()
    root.mainloop()
