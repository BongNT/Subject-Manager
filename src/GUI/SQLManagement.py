import tables

class SQLManagement:

    def __init__(self):
        conn = None

    def connectSQL(self):
        self.conn = tables.connect(host='localhost', user='root', port='3306', database='cnpm')

        if self.conn.is_connected():
            print('Connected to MySQL database')

        cur = self.conn.cursor()

        try:
            db = cur.execute("show databases")
        except:

            self.conn.rollback()
        for x in cur:
            print(x)

        self.conn.close()

    def query(self):
        cur = self.conn.cursor()

        sql = "INSERT INTO `listsubject` (`student_id`,`subject_id`, `class_id`, `type`) VALUES (%d,%s,%s,%s)"
        cur.execute(sql, ('1234','CEN432','CEN432 21','CL'))

    if __name__ == '__main__':
        connectSQL()
