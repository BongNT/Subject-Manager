from tkinter import *
from SQLManagement import SQLManagement
from Subject import Subject
class SubjectManager:

    def __init__(self, parent):
        # list subject_id
        self.list_subject = []
        self.sql_management = SQLManagement()
        self.color_manager = [] # [(class_id, hex color),...]
        self.parent = parent
        self.available_lesson = [[1 for x in range(7)] for x in range(14)]
    def create_list_subject(self, student_id):
        # search MSV -> list data
        # init subject_id
        list_data = self.sql_management.getStudentClasses(student_id)
        for i in list_data:
            print(i)
        for data in list_data:
            self.append(data)

    def append(self, data):
        # ('INT2211', 'Cơ sở dữ liệu', 4, 'INT2211 23', 'ThS.Lê Hoàng Quỳnh', 26, 2.0, '3-4', 'PM 307-G2', '2')
        if self.__check_inputdata(data):
            color = self.randomColor()
            # kiem tra xem co mon nay trong color_manager ko
            ck =True
            for i in self.color_manager:
                if i[0] == data[3]:
                    color = i[1]
                    ck = False
                    break
            if ck:
                c = [data[3], color]
                self.color_manager.append(c)
            new_subject = Subject(self.parent, data,color)
            self.list_subject.append(new_subject)

    def __check_inputdata(self, data):
        # kiem tra mon hoc co bi trung thoi gian khong
        lesson = data[7].split("-")
        weekday = int(data[6])
        print(weekday,lesson[0], lesson[1])
        for i in range(int(lesson[0]), int(lesson[1]) + 1):
            if self.available_lesson[i - 1][weekday - 2] != 1:
                print(12323132312312)
                return False
        for i in range(int(lesson[0]), int(lesson[1]) + 1):
            self.available_lesson[i-1][weekday - 2] = 0

        # kiem tra xem du lieu dua vao co trung voi mon dang co
        for subject in self.list_subject:
            # môn học đã được đăng ký
            if data[3] == subject.class_id and data[9] == subject.type:
                print("Lỗi, lớp học{}-{} đã được đăng ký trước đó ".format(data[3], data[1]))
                return False
            if data[0] == subject.subject_id and data[3] != subject.class_id:
                print("Lỗi, bạn đã đăng ký lớp học{}-{} ".format(subject.class_id, subject.subject_name))
                return False
        return True

    def getinfo(self):
        for i in self.list_subject:
            pass

    def randomColor(self):
        import random
        ck = True
        color = None
        while ck:
            ck = False
            r = lambda: random.randint(0, 255)
            color = '#%02X%02X%02X' % (r(), r(), r())
            for c in self.color_manager:
                if c[1] == color:
                    ck =True
        return color

    def delete(self, class_id):
        d=[]
        for subject in self.list_subject:
            if class_id == subject.class_id:
                lesson = subject.time
                weekday = subject.weekday
                for i in range(int(lesson[0]), int(lesson[1]) + 1):
                    self.available_lesson[i-1][weekday - 2] = 1
                d.append(subject)
                subject.destroy()
        for i in d:
            self.list_subject.remove(i)
        for i in self.color_manager:
            if i[0] == class_id:
                self.color_manager.remove(i)
                break
        print(len(self.color_manager))

        #print(len(self.list_subject))
        d.clear()

    def delete_all(self):
        for subject in self.list_subject:
            lesson = subject.time
            weekday = subject.weekday
            for i in range(int(lesson[0]), int(lesson[1]) + 1):
                self.available_lesson[i-1][weekday - 2] = 1
            subject.destroy()
        self.list_subject.clear()
        self.color_manager.clear()
    def __len__(self):
        return len(self.list_subject)

if __name__ == "__main__":
    sm = SubjectManager()
    root = Tk()

    root.geometry()

    sm.delete(11)
    sm.getinfo()
    root.mainloop()
