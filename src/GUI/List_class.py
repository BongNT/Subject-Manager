from tkinter.ttk import *
from tkinter import *
import json
import os

class TableSubject(Treeview):
    def __init__(self, parent):
        Treeview.__init__(self, parent)
        self.HEADING = ("order", "subject", "subject_name", "credit", "subject_id",
                        "teacher_name", "number_of_students", "time", "weekday",
                        "lesson", "place", "note")
        self.initUI()
        self.read_json_file()

    def initUI(self):
        style = Style()
        # configure color
        style.configure("Treeview",
                        backgound="#D3D3D3",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="#D3D3D3"
                        )
        style.map("Treeview",
                  background=[('selected', "#347083")])
        # create scrollbar
        tree_scroll = Scrollbar(self)
        tree_scroll.pack(side=RIGHT, fill=Y)
        self.configure(yscrollcommand=tree_scroll.set, selectmode="extended")
        tree_scroll.configure(command=self.yview)
        self.tag_configure('oddrow', background="white")
        self.tag_configure('evenrow', background="lightblue")
        self['columns'] = self.HEADING
        # formate the columns
        self.column("#0", width=0, stretch=NO)
        for heading in self.HEADING:
            self.column(heading, width=1, anchor=CENTER)

        # create heading
        self.heading("#0", anchor=CENTER, text="")
        for heading in self.HEADING:
            self.heading(heading, text=heading, anchor=CENTER)

    def insert_data(self, data):
        count = 0
        for i in data:
            list = tuple(i.values())
            if count % 2 == 0:
                self.insert(parent='', index='end', iid=count, values=list, tag=('evenrow'))
            else:
                self.insert(parent='', index='end', iid=count, values=list, tag=('oddrow'))
            count += 1

    def read_json_file(self):
        absFilePath = os.path.abspath(__file__)
        print(absFilePath)
        projectPath = absFilePath
        for i in range(3):
            projectPath = os.path.dirname(projectPath)
        dataPath = projectPath + "/res/Data/timetable.json"

        with open(dataPath, 'r') as file:
            d = file.read()
            data = json.loads(d)
            self.insert_data(data)


    def get_selected_data(self):
        selected = self.selection()
        value = []
        for s in selected:
            value.append(self.item(s, 'values'))
        print(value)
        return value


if __name__ == "__main__":
    root = Tk()
    root.geometry()
    app = TableSubject(root)
    app.grid(row=0, column=0)

    root.mainloop()
