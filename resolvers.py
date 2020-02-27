import json
import time
import math

students={{'studentId':'1234456'},{'name':'Bob Vance'}}

def student_with_id(_, info, _name):

        for s in data[students]:
            if students['name'] == _name:
                return student


# def resolve_residents_in_building(building, info):
#      print(building)
#      with open('./students.json') as file:
#          data = json.load(file)
#          students = [
# #             student 
# #             for student 
# #             in data['students'] 
# #             if student['building'] 
# #             == building['id']]
# #         return students

def resolver_createStudent(_,info,_data):
    new_student={}
    new_student['studentId']=get_new_id()  
    new_student['name'] = _data["name"]
    students.append(new_student)
    print(students)
    return True

def get_new_id():
    new_id=int(time.time())
    new_id=math.trunc(new_id)
    return new_id    