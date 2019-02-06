import json
from Detached.Global.Configurations.ConnectionEstablishment import *

"""File which consist of user dependent configurations. These probably be different for each user.
   Hence, if this file doesn't exists, create manually at following location (within the project):
   Detached/Global/Configurations/LocalUsersConfigurations.py
   
   Note that this file is not supposed to be on tracking."""
from Detached.Global.Configurations.LocalUsersConfigurations import *


# This function should be called for creating a subject list for a new course.
def insert_course_and_subjects():
    course_name = input("Type the course name")
    total_semesters = int(input("Provide total semesters"))

    # creating an empty data structure for storing subjects
    document = {course_name: [{str(sem_number): []} for sem_number in range(1, total_semesters + 1)]}

    # adding subjects in required empty lists
    for i in range(total_semesters):
        while True:
            subject = input(f"Add Subject for semester {i + 1}")
            document[course_name][i][str(i + 1)].append(subject)
            add_more = input("Any more subjects\n1.True\n2.False")
            if add_more == "2":
                break

    db[collection].insert(document)
    db[collection].find()


def subject_removal():
    """Define a function to remove a subject/s from given course
       of a particular semester"""
    # include a function to display list of subjects from which to remove it.


def display():
    pass


def update_subject(course, sem, replacing, replaced_by):
    course_sem = str(str(course) + "." + str(sem))
    to_be_changed = course_sem + ".$"
    db[collection].find_one_and_update({course_sem: replacing}, {"$set": {to_be_changed: replaced_by}})


# give absolute address of the records.json file to load at once
def insert_all():
    # location (within the project) of the file to be loaded
    file_location = 'Detached/Database/records.json'

    # address (from the root location) of file
    complete_location = project_location + file_location
    with open(complete_location) as f:
        file_data = json.load(f)

    db[collection].insert(file_data)
    print(db[collection].find())


# function to get subjects list of a given course and respective semester
def get_list_of_subject_for(course, semester):
    sub_list = []
    course_sem = str(str(course) + "." + str(semester))
    cursor = db[collection].find_one({course: {"$exists": "true"}}, {course_sem: "true", "_id": 0})
    for subject in cursor[str(course)][str(semester)]:
        sub_list.append(subject)
    return sub_list
