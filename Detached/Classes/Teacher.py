from Detached.Global.Configurations.ConnectionEstablishment import *
import Detached.Global.Variables.varFile1 as Var

"""The subjects attribute that is provided in the class will be a list of dictionaries which will 
    contain semester number as their keys and "list" of subjects as their values, 
    as an example of this attribute is given in the teachers.json file.
"""


# Teacher Data Structure Definition
class Teacher:
    def __init__(self, name=None, dept=None, rank=None, school=None, course=None, uid=None, max_lec=None, min_lec=None,
                 sem_taught=None):
        self.name = name
        self.department = dept
        self.rank = rank
        self.school = school
        self.course = course   # added for new teachers
        self.uID = uid  # String
        self.maxLectures = max_lec  # per week
        self.minLectures = min_lec  # per week
        self.lectureSlots = [[False] * Var.maximumSlots] * Var.totalWorkingDays
        self.semestersTeaching = sem_taught
        self.subjects = []  # self.add_subjects_for_teachers()

    # function to fetch attributes and their values
    def getinfo(self):

        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"School: {self.school}")
        print(f"Universal ID: {self.uID}")
        print(f"Maximum no. of Lectures: {self.maxLectures}")
        print(f"Minimum no. of Lectures: {self.minLectures}")
        # print("Lecture Slots")        # how to show busy slots?
        print("Subjects:")
        print("Teachers:")
        for semester in self.semestersTeaching:
            print(semester)
        print()

    def set_max_lectures(self, max_lectures):
        if max_lectures < self.minLectures:
            print("Cannot be less than minimum lectures")
        else:
            self.maxLectures = max_lectures

    def update_info(self):
        pass

    def add_teacher(self):
        document = {"name": self.name, "department": self.department, "school": self.school, "course": self.course,
                    "uid": self.uID,
                    "rank": self.rank, "max_l": self.maxLectures, "min_l": self.minLectures,
                    "semester_teaching": [{self.department: self.semestersTeaching}],
                    "subjects": self.subjects,
                    "empty_slots": [{day: list(str(x) for x in range(1, 7))} for day in Var.days_list]
                    }

        db[teacher_collection].insert(document)
        print("data inserted")
