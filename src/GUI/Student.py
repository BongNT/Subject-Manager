
class Student:
    def __init__(self, data):
        self.name = "a b c"
        self.DOB = "dd/mm/yyyy"
        self.id = 12345678
        self.course = "QH-yyyy-I/CQ ....."
        self.insert_data(data)
        self.is_CLC = False
    def get_info(self):
        return "Họ và tên : {}\nMã sinh viên : {}\nNgày sinh : {}\nKhóa : {}".\
            format(self.name, self.id,self.DOB, self.course)



    def insert_data(self, data):
        data = data[0]
        self.id = data[0]
        self.name = data[1]
        self.DOB = data[2]
        self.course = data[3]
        if "CLC" in self.course:
            self.is_CLC = True
        print((self.is_CLC))