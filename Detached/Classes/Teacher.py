from Detached.Global.Configurations.ConnectionEstablishment import *
import Detached.Global.Variables.varFile1 as Var

"""The subjects attribute that is provided in the class will be a list of dictionaries which will 
    contain semester number as their keys and "list" of subjects as their values, 
    as an example of this attribute is given in the teachers.json file.
"""


# Teacher Data Structure Definition
class Teacher:
    def __init__(self, name=None, dept=None, rank=None, max_lec=None, min_lec=None, school=None, course=None, uid=None,
                 sem_taught=None):
        self.name = name
        self.department = dept
        self.rank = rank
        self.school = school
        self.course = course                            # added for new teachers
        self.uID = uid                                  # String
        self.maxLectures = max_lec                      # per week
        self.minLectures = min_lec                      # per week
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

    # function to set maximum number of lectures that could be taken per week by a teacher
    def set_max_lectures(self, max_lectures):
        if max_lectures < self.minLectures:
            print("Cannot be less than minimum lectures")
        else:
            self.maxLectures = max_lectures

    def update_info(self):
        pass

    def add_teacher(self):
        # getting id for the teacher
        self.uID = self.generate_id()

        # creating a JS formatted document to insert it into the teacher's database
        document = {"name": self.name, "department": self.department, "school": self.school, "course": self.course,
                    "uid": self.uID,
                    "rank": self.rank, "max_l": self.maxLectures, "min_l": self.minLectures,
                    "semester_teaching": [{self.department: self.semestersTeaching}],
                    "subjects": self.subjects,
                    "empty_slots": [{day: list(str(x) for x in range(1, 7))} for day in Var.days_list]
                    }

        # insertion of all information (as a document) into the database
        db[teacher_collection].insert(document)
        print("data inserted")

    # function to create an ID for a new teacher
    def generate_id(self):
        string_for_id = self.rank[0:4]                  # fetching the 1st 3 characters of teacher's designation
        cursor = db[configuration].find_one({}, {"_id": 0, "id_number": "true"})
        id_number = None
        if cursor is not None:
            for value in cursor["id_number"]:
                id_number = value
        else:
            db[configuration].insert(Var.db_variables)
            cursor = db[configuration].find_one({}, {"_id": 0, "id_number": "true"})
            for value in cursor["id_number"]:
                id_number = value

        whole_id = string_for_id + str(id_number)   # appending a number into the above sliced string
        Var.id_number += 1                              # ##### must be updated in database #######
        db[configuration].find_one_and_update({}, {"$set": {"id_number": str(Var.id_number)}})
        return whole_id                                 # is a string.


# you can as many subjects as needed
def update_teacher_subject(teacher_uid, course, semester, *subjects):
    key = "subjects" + "." + str(course) + "." + str(semester)
    cursor = db[teacher_collection].find_one({"uid": teacher_uid}, {"_id": 0, key: "true"})
    print(cursor)
    db[teacher_collection].find_one_and_update({"uid": teacher_uid},
                                               {"$set": {key: subjects}})
