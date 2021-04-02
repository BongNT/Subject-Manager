from tkinter.ttk import *
from tkinter import *
from Subject import Subject


class Timetable(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        # self.parent.title("timetable")

        Style().configure("abc", padding=(0, 0, 0, 0), font='Calibri 10')
        # http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        # rows là chiếm cả 1 hàng
        for i in range(8):
            self.grid_columnconfigure(i, weight=1)
        for i in range(15):
            self.grid_rowconfigure(i, weight=1)

        # label_morning = Label(self, height = 2, width = 10,background = "pale violet red", relief=GROOVE,text = "Sáng")
        # label_morning.grid(row=1,column=0, rowspan=6,sticky ="nsew")
        # label_afternoon = Label(self, height=2, width=10, background="cyan2", relief=GROOVE, text="Chiều")
        # label_afternoon.grid(row =7, column=0,rowspan = 6,sticky ="nsew")
        label_time = Label(self, height=2, width=7, background="yellow", relief=GROOVE, text="Tiết", )
        label_time.grid(row=0, column=1, sticky="nsew")

        label_list_time = []
        for i in range(1, 15):
            temp_label = Label(self, height=2, width=10, background="white", relief=GROOVE, font='calibri 7',
                               text="{} ({}h - {}h)".format(i, i + 6, i + 7))
            temp_label.grid(row=i, column=1, sticky="nsew")
            label_list_time.append(temp_label)
        for i in range(2, 8):
            temp_label = Label(self, background="yellow", relief=GROOVE, text=("Thứ " + str(i)))
            temp_label.grid(row=0, column=i, sticky="nsew")
        for i in range(9):
            self.grid_columnconfigure(i, weight=1)
        for i in range(16):
            self.grid_rowconfigure(i, weight=1, )

    def update_subject(self, list_data):
        for data in list_data:
            print(data)
            subject = Subject(self, data)


if __name__ == "__main__":
    root = Tk()

    root.geometry()
    app = Timetable(root)
    app.pack()
    root.mainloop()
