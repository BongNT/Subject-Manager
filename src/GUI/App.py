from tkinter.ttk import *
from tkinter import *
from timetable import Timetable
from List_class import TableSubject


class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.is_show_new_timetable = False
        self.is_show_class_list = False
        self.pack(fill=BOTH, expand=True, side=TOP)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=14)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=18)

        Style().configure("abc", padding=(0, 0, 0, 0), font='Calibri 10')
        self.initUI()

        print(self.grid_slaves(1, 1))

    def initUI(self):
        self.top_frame = LabelFrame(self)
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(1, weight=10)
        self.top_frame.grid_columnconfigure(2, weight=1)
        self.top_frame.grid_columnconfigure(3, weight=1)
        self.top_frame.grid(row=0, column=1, rowspan=1, sticky="nsew")

        self.mid_frame = LabelFrame(self)
        self.mid_frame.grid_rowconfigure(0, weight=1)
        self.mid_frame.grid_columnconfigure(0, weight=1)
        self.mid_frame.grid_columnconfigure(1, weight=1)
        self.mid_frame.grid(row=1, column=1, rowspan=1, sticky="nsew")

        # top
        input_label = Label(self.top_frame, text="MSV :")
        input_label.grid(row=0, column=0, rowspan=1, sticky="nsew")
        self.input_bar = Entry(self.top_frame)
        self.input_bar.grid(row=0, column=1, rowspan=1, sticky="nsew")
        self.input_bar.bind("<Return>", self.search_MSV)
        search_button = Button(self.top_frame, text="Search", command=self.search_MSV)
        search_button.grid(row=0, column=2, rowspan=1, sticky="nsew")
        mic_button = Button(self.top_frame, text="Mic")
        mic_button.grid(row=0, column=3, rowspan=1, sticky="nsew")
        new_timetable_button = Button(self.top_frame, text="Add new Timetable", command=self.show_new_timetable)
        new_timetable_button.grid(row=0, column=4, sticky="nsew")
        # mid
        self.timetable1 = Timetable(self.mid_frame)
        self.timetable1.grid(row=0, column=0, sticky="nsew")
        self.timetable2 = Timetable(self.mid_frame)

        self.left_frame = LabelFrame(self, width=300)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(1, weight=1)
        self.left_frame.grid_rowconfigure(2, weight=7)
        self.left_frame.grid_rowconfigure(3, weight=1)
        self.left_frame.grid_columnconfigure(0, weight=1)

        self.left_frame.grid(column=0, row=0, rowspan=2, sticky="nsew")
        expand_button = Button(self.left_frame, text="Expand").grid(row=0, column=0, sticky="nsew")
        self.show_class_list_frame = Frame(self.left_frame)
        # self.show_class_list_frame.grid(row=2, column=0, sticky="nsew")
        self.show_class_list_frame.grid_columnconfigure(0, weight=1)
        self.show_class_list_frame.grid_columnconfigure(1, weight=1)
        self.show_class_list_frame.grid_rowconfigure(0, weight=1)
        self.show_class_list_frame.grid_rowconfigure(1, weight=1)
        self.show_class_list_frame.grid_rowconfigure(2, weight=100)
        show_class_list_button = Button(self.left_frame, text="Show Class", command=self.show_class_list)
        show_class_list_button.grid(row=1, column=0, columnspan=2, sticky="nsew")
        sort_class_list_label = Label(self.show_class_list_frame, text="Sort")
        sort_class_list_label.grid(row=1, column=0, sticky="ew")
        find_label = Label(self.show_class_list_frame, text="Find :")
        find_label.grid(row=0, column=0)
        self.find_entry = Entry(self.show_class_list_frame)
        self.find_entry.grid(row=0, column=1, sticky="ew")
        self.find_entry.bind("<Return>", self.find)
        sortby = StringVar()
        sort_class_list_selection = OptionMenu(self.show_class_list_frame, sortby, "a", "b")  # dropdown(18)
        sort_class_list_selection.grid(row=1, column=1, sticky="ew")
        self.subject_table = TableSubject(self)

        # create popup menu in subject table
        self.popup_menu = Menu(self.subject_table, tearoff=False)
        self.popup_menu.add_command(label="Insert into Timetable", command=self.insert_data)
        self.subject_table.bind("<Button-3>", self.show_popup_menu)

        setting_button = Button(self.left_frame, text="Setting", command=self.open_setting)
        setting_button.grid(row=4, column=0, columnspan=2, sticky="nsew")

    def show_class_list(self):
        if self.is_show_class_list:
            self.mid_frame.grid(row=1, column=1, rowspan=1, sticky="nsew")
            self.top_frame.grid(row=0, column=1, rowspan=1, sticky="nsew")
            self.show_class_list_frame.grid_forget()
            self.subject_table.grid_forget()
            self.is_show_class_list = False
        else:
            self.top_frame.grid_forget()
            self.mid_frame.grid_forget()
            self.show_class_list_frame.grid(row=2, column=0, sticky="nsew")
            self.subject_table.grid(column=1, row=0, rowspan=2, sticky="nsew")
            self.is_show_class_list = True

    def show_popup_menu(self, event):
        self.popup_menu.tk_popup(event.x_root, event.y_root)

    def insert_data(self):
        self.timetable2.update_subject(self.subject_table.get_selected_data())

    def show_new_timetable(self):
        if self.is_show_new_timetable:
            self.timetable2.grid_forget()
            self.is_show_new_timetable = False
            print(self.winfo_children())

        else:
            self.timetable2.grid(row=0, column=1, sticky="nsew")
            print(self.mid_frame.winfo_children())
            self.is_show_new_timetable = True

    def search_MSV(self, event = None):
        print(self.input_bar.get())
        self.input_bar.delete(0, END)

    def find(self, event):
        print(self.find_entry.get())
        self.find_entry.delete(0, END)

    def open_setting(self):
        pass


if __name__ == "__main__":
    root = Tk()
    root.geometry()
    root.state('zoomed')
    app = App(root)
    root.mainloop()
