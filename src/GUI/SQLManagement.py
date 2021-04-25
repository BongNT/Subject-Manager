import mysql.connector
from mysql.connector import Error

class SQLManagement:

    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', user='root', port='3306', database='test')
        self.connectDB()
        #self.query()

    def connectDB(self):
        self.cur = self.conn.cursor()
        if self.conn.is_connected():
            print('Connected to MySQL database')
        try:
            print("connect successfully")
        except:
            self.conn.rollback()



    def query(self):

        #sql = "INSERT INTO `listsubject` (`student_id`,`class_id`, `class_id`, `type`) VALUES (%s,%s,%s,%s)"
        sql = "SELECT * FROM `listsubject`"
        self.cur.execute(sql)
        s=self.cur.fetchone()
        print(s)

    def getStudentClasses(self,student_id):
        print("sql")
        query ='''SELECT subject.subject_id, subject.subject_name, subject.credit,
            class.class_id, class.teacher_name, class.number_of_students
            ,class.weekday, class.lesson, class.place, class.`type`
            FROM students JOIN listsubject ON students.`student_id` = listsubject.`student_id`
            JOIN subject ON subject.`subject_id` = listsubject.`subject_id`
            JOIN class ON class.class_id = listsubject.class_id 
            WHERE students.student_id = {} AND listsubject.type = class.type'''.format(student_id)
        self.cur.execute(query)
        s = self.cur.fetchall()
        return s
    def find(self, input, findOption, sortOption, is_DESC):
        option = ["class.subject_id", "subject.subject_name", "subject.credit", "class.class_id",
                  "class.teacher_name", "class.number_of_students", "class.time", "class.weekday",
                  "lesson", "place", "note"]
        query = '''SELECT class.subject_id, subject.subject_name, subject.credit, 
                    class.class_id,class.teacher_name, class.number_of_students, 
                    class.time, class.weekday, class.lesson, class.place, class.type
                    FROM `class`  JOIN subject ON class.subject_id = subject.subject_id
                    '''
        if len(input) >2 :
            query += " WHERE {} LIKE '{}' ".format(option[findOption], input)
        query += " ORDER BY {} ".format(option[sortOption])
        if is_DESC:
            query += "DESC"
        print(query)
        self.cur.execute(query)
        s = self.cur.fetchall()
        return s

    def get_list_class(self):
        query = '''SELECT class.subject_id, subject.subject_name, subject.credit, 
            class.class_id,class.teacher_name, class.number_of_students, 
            class.time, class.weekday, class.lesson, class.place, class.type
            FROM `class`  JOIN subject ON class.subject_id = subject.subject_id
            ORDER BY `weekday` DESC,`lesson`DESC'''
        self.cur.execute(query)
        s = self.cur.fetchall()
        return s

    def get_student(self, student_id):
        query = '''SELECT * FROM `students` WHERE student_id = {}'''.format(student_id)
        self.cur.execute(query)
        s = self.cur.fetchall()
        return s

    def close(self):
        self.conn.close()
        self.cur.close()


if __name__ == '__main__':
    a = SQLManagement()
    a.get_list_class()
