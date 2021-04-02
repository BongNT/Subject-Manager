from tkinter import *


class SubjectManager:

    def __init__(self):
        # list subject
        self.list_subject = []


    def create_list_subject(self, MSV):
        # search MSV -> list data
        # init subject
        pass

    def append(self):
        #check new subject in
        pass

    def getinfo(self):
        for i in self.list_subject:
            print(i._id)

    def delete(self, subject_id):
        for i in self.list_subject:
            if subject_id == i._id:
                self.list_subject.remove(i)


if __name__ == "__main__":
    sm = SubjectManager()
    root = Tk()

    root.geometry()

    sm.delete(11)
    sm.getinfo()
    root.mainloop()
