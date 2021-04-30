import json
import os

absFilePath = os.path.abspath(__file__)
print(absFilePath)
projectPath = absFilePath
for i in range(3):
    projectPath = os.path.dirname(projectPath)
dataPath = projectPath + "/res/Data/config.json"
print(dataPath)

def read_json_file():


    with open(dataPath, 'r') as file:
        d = file.read()
        data = json.loads(d)
        print(data["host"])

def write_to_file():
    data = {'student': [
        {'student_id': '19021226', 'student_name': 'Nguyễn Thành Bổng', 'DOB': '20/08/2001',
                          'course': 'QH-2019-I/CQ-C-A-CLC3'},
        {'subject': [
        {'subject_id': 'INT2211', 'subject_name': 'Cơ sở dữ liệu', 'credit': '4', 'class_id': 'INT2211 23',
         'teacher_name': 'ThS.Lê Hoàng Quỳnh', 'number_of_student': '26', 'weekday': '2', 'time': '3-4',
         'place': 'PM 307-G2', 'type': '2', 'color': '#299A03'},
        {'subject_id': 'PES1025', 'subject_name': 'Bóng đá', 'credit': '1', 'class_id': 'PES1025 3',
         'teacher_name': 'TT GDTC&TT', 'number_of_student': '52', 'weekday': '2', 'time': '7-8',
         'place': 'Sân bãi ĐHNN', 'type': 'CL', 'color': '#D8A2F2'},
        {'subject_id': 'INT2208E', 'subject_name': 'Công nghệ phần mềm', 'credit': '3', 'class_id': 'INT2208E 23',
         'teacher_name': 'TS.Đặng Đức Hạnh', 'number_of_student': '49', 'weekday': '3', 'time': '4-6',
         'place': '206-GĐ3', 'type': 'CL', 'color': '#9523ED'},
        {'subject_id': 'EPN1096', 'subject_name': 'Vật lý đại cương 2', 'credit': '2', 'class_id': 'EPN1096 26',
         'teacher_name': 'GS.TS.Hoàng Nam Nhật; ThS.Nguyễn Đăng Cơ', 'number_of_student': '39', 'weekday': '3',
         'time': '9-10', 'place': '205-GĐ3', 'type': 'CL', 'color': '#893667'},
        {'subject_id': 'INT3401E', 'subject_name': 'Trí tuệ nhân tạo', 'credit': '3', 'class_id': 'INT3401E 22',
         'teacher_name': 'TS.Nguyễn Văn Vinh', 'number_of_student': '50', 'weekday': '4', 'time': '3-5',
         'place': '101-G8', 'type': 'CL', 'color': '#789799'},
        {'subject_id': 'INT2213', 'subject_name': 'Mạng máy tính', 'credit': '4', 'class_id': 'INT2213 25',
         'teacher_name': 'ThS.Đào Minh Thư', 'number_of_student': '21', 'weekday': '4', 'time': '7-9',
         'place': 'PM 307-G2', 'type': '1', 'color': '#7D096E'},
        {'subject_id': 'INT2213', 'subject_name': 'Mạng máy tính', 'credit': '4', 'class_id': 'INT2213 25',
         'teacher_name': 'PGS.TS.Nguyễn Hoài Sơn', 'number_of_student': '50', 'weekday': '6', 'time': '7-8',
         'place': '208-GĐ3', 'type': 'CL', 'color': '#7D096E'},
        {'subject_id': 'INT2211', 'subject_name': 'Cơ sở dữ liệu', 'credit': '4', 'class_id': 'INT2211 23',
         'teacher_name': 'TS.Nguyễn Tuệ', 'number_of_student': '41', 'weekday': '6', 'time': '9-10', 'place': '208-GĐ3',
         'type': 'CL', 'color': '#299A03'},
        {'subject_id': 'INT1050', 'subject_name': 'Toán học rời rạc', 'credit': '4', 'class_id': 'INT1050 26',
         'teacher_name': 'GVC.TS.Lê Phê Đô', 'number_of_student': '47', 'weekday': '7', 'time': '7-10',
         'place': '207-GĐ3', 'type': 'CL', 'color': '#82AE1F'}]}, {'subject': [
        {'subject_id': 'INT2211', 'subject_name': 'Cơ sở dữ liệu', 'credit': '4', 'class_id': 'INT2211 23',
         'teacher_name': 'ThS.Lê Hoàng Quỳnh', 'number_of_student': '26', 'weekday': '2', 'time': '3-4',
         'place': 'PM 307-G2', 'type': '2', 'color': '#299A03'},
        {'subject_id': 'PES1025', 'subject_name': 'Bóng đá', 'credit': '1', 'class_id': 'PES1025 3',
         'teacher_name': 'TT GDTC&TT', 'number_of_student': '52', 'weekday': '2', 'time': '7-8',
         'place': 'Sân bãi ĐHNN', 'type': 'CL', 'color': '#D8A2F2'},
        {'subject_id': 'INT2208E', 'subject_name': 'Công nghệ phần mềm', 'credit': '3', 'class_id': 'INT2208E 23',
         'teacher_name': 'TS.Đặng Đức Hạnh', 'number_of_student': '49', 'weekday': '3', 'time': '4-6',
         'place': '206-GĐ3', 'type': 'CL', 'color': '#9523ED'},
        {'subject_id': 'EPN1096', 'subject_name': 'Vật lý đại cương 2', 'credit': '2', 'class_id': 'EPN1096 26',
         'teacher_name': 'GS.TS.Hoàng Nam Nhật; ThS.Nguyễn Đăng Cơ', 'number_of_student': '39', 'weekday': '3',
         'time': '9-10', 'place': '205-GĐ3', 'type': 'CL', 'color': '#893667'},
        {'subject_id': 'INT3401E', 'subject_name': 'Trí tuệ nhân tạo', 'credit': '3', 'class_id': 'INT3401E 22',
         'teacher_name': 'TS.Nguyễn Văn Vinh', 'number_of_student': '50', 'weekday': '4', 'time': '3-5',
         'place': '101-G8', 'type': 'CL', 'color': '#789799'},
        {'subject_id': 'INT2213', 'subject_name': 'Mạng máy tính', 'credit': '4', 'class_id': 'INT2213 25',
         'teacher_name': 'ThS.Đào Minh Thư', 'number_of_student': '21', 'weekday': '4', 'time': '7-9',
         'place': 'PM 307-G2', 'type': '1', 'color': '#7D096E'},
        {'subject_id': 'INT2213', 'subject_name': 'Mạng máy tính', 'credit': '4', 'class_id': 'INT2213 25',
         'teacher_name': 'PGS.TS.Nguyễn Hoài Sơn', 'number_of_student': '50', 'weekday': '6', 'time': '7-8',
         'place': '208-GĐ3', 'type': 'CL', 'color': '#7D096E'},
        {'subject_id': 'INT2211', 'subject_name': 'Cơ sở dữ liệu', 'credit': '4', 'class_id': 'INT2211 23',
         'teacher_name': 'TS.Nguyễn Tuệ', 'number_of_student': '41', 'weekday': '6', 'time': '9-10', 'place': '208-GĐ3',
         'type': 'CL', 'color': '#299A03'},
        {'subject_id': 'INT1050', 'subject_name': 'Toán học rời rạc', 'credit': '4', 'class_id': 'INT1050 26',
         'teacher_name': 'GVC.TS.Lê Phê Đô', 'number_of_student': '47', 'weekday': '7', 'time': '7-10',
         'place': '207-GĐ3', 'type': 'CL', 'color': '#82AE1F'}]}]}

    with open(dataPath, 'w') as file:
        json.dump(data, file)
if __name__ == '__main__':

    read_json_file()