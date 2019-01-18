from Detached.Global.Functions.TeacherManagement import check_teacher_availability
from Detached.Global.Variables.varDB import *
from pymongo import MongoClient

client = MongoClient(localhost)
db = client[database]


# Course Data Structure definition
class Course:
    def __init__(self, name=None, code=None, batch=0, sem=0, start_time=0):
        self.name = name
        self.code = code
        self.batch = batch
        self.totalSemesters = sem
        self.startingHour = start_time  # 24 Hrs.
        self.teachers = []  # append teacher's uID

    # displaying all attributes of 'Course' object
    def getinfo(self):
        print(f"Name: {self.name}")
        print(f"Code: {self.code}")
        print(f"Start Timing: {self.startingHour} hours")
        print(f"No. of Semesters: {self.totalSemesters}")
        print(f"Teachers:")
        for teacher in self.teachers:
            print(teacher)
        print()

    def update_info(self):
        self.getinfo()
        print("What is the attribute you want to update ?")
        attribute = int(input(f"1.Name\n2.Course Code\n3.Start Timing\n4.No. of Semesters"
                              f"\n Any other key to exit"))
        if attribute == 1:
            self.name = input("Enter New Course Name")
        elif attribute == 2:
            self.code = input("Enter New Course Code")
        elif attribute == 3:
            self.startingHour = input("Enter New Start Time(24 Hrs)")
        elif attribute == 4:
            self.totalSemesters = int(input("Enter Total Semesters"))
        else:
            return

    # Done
    def add_teacher(self, teacher_uid):
        if check_teacher_availability(teacher_uid):
            """Write a query to get a teacher by given uID from DataBase"""
            self.teachers.append(teacher_uid.uID)
            print("Added Successfully")
        else:
            print("Teacher is running out of time hence, can't be added")

    # its working depends on adding of the "Teacher"'s instance or just name in above self.teacher list
    def remove_teacher(self, uid):
        if uid in self.teachers:
            self.teachers.remove(uid)
            print("Teacher removed ")


# Test:
# obj = Teacher("Manoj", "DCS", 3, "SIST", "mca-mk", 17, 13, 15)
# obj.getinfo()
# print(check_teacher_availability(obj))
# course1 = Course("MCA", "mca", 2, 2, 10)
# course1.getinfo()
# course1.add_teacher(obj)
# course1.getinfo()
# course1.remove_teacher("mca-mk")
# course1.getinfo()

def get_list_of_subject_for(course, semester):
    sub_list = []
    course_sem = str(str(course) + "." + str(semester))
    cursor = db[collection].find_one({course: {"$exists": "true"}}, {course_sem: "true", "_id": 0})
    print(cursor)
    for subject in cursor[str(course)][str(semester)]:
        sub_list.append(subject)
    print(sub_list)
    return sub_list


get_list_of_subject_for("MCA", 3)
