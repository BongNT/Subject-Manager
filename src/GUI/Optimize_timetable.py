from tkinter.ttk import Frame

from Subject import Subject
from SubjectManager import SubjectManager
from timetable import Timetable


class Optimize(Frame):
    def __init__(self, parent, can_config=True):
        Frame.__init__(self, parent)

    def optimize(self, list_data):
        list_timetable =[]
        self.do(0,list_data)

    def do(self, index, list_data, subject_manager=None, lst=None):

        last_subject = list_data[index][3]
        while True:
            if subject_manager is None:
                subject_manager = SubjectManager(self)
            data = list_data[index]
            index += 1
            if subject_manager.check_inputdata(data):
                new_subject = Subject(self, data)
                subject_manager.list_subject.append(new_subject)
                self.do(index, list_data, subject_manager)
            else:
                while list_data[index][3] == data:
                    index += 1
                self.do(index, list_data, subject_manager)
                break


