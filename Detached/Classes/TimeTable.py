import random

from Detached.Global.Variables.varFile1 import *
from Detached.Global.Configurations.ConnectionEstablishment import *


# class for generating Time Table for a single batch
class TimeTable:
    def __init__(self):
        self.batchNo = 0
        self.totalSlots = maximumSlots              # decides till when the batch will go on
        self.lectures = []                          # contains the mappings of teachers and their subject
        """ format => [ {"teacher1" : "subject1"}, {"teacher2" : "subject2"} ]"""

        self.assignedLectures = []                  # initially empty, will be updated only by place()/assign() function
        """ format => [ {"Monday" : [1,2,3] }, {"Tuesday" : [1,2,3,4] } ]"""

        self.freeLectures = []                      # initially empty, used as the list on which to iterate for placing lectures

    def map(self, teachers):                        # teachers: T3, T1, T2, T6, T4  (as an example)
        """Mapping is done on the basis matching the sequence of subjects and sequence of teachers provided as in the list.
           So mapping would be as:
           MCA-401 => T3, MCA-402 => T1, MCA-403 => T2, MCA-404 => T6, MCA-405 => T4 """
        pass

    def place(self, teacher_to_place):
        while True:
            time_table = [[None for _ in range(len(days_list))] for _ in range(maximumSlots)]
            for index in range(len(time_table)):
                for day in range(len(time_table[index])):
                    for slot in range(maximumSlots):
                        time_table[slot][day] = self.random(teacher_to_place)

            for value in time_table:
                print(value)

            db[time_table_collection].insert({"course": "MCA",
                                              "semester": "1",
                                              "previous_one": time_table})

            value = int(input("\nAre you satisfied?\n1. Yes\n0.No\n"))
            if value:
                for index in range(len(time_table)):
                    for i in range(len(time_table[index])):
                        query = "empty_slots" + ".$[]." + str(days_list[i])
                        slot_no = str(index + 1)

                        db[teacher_collection].find_one_and_update({"uid": str(time_table[index][i])},
                                                                   {"$pull": {query: slot_no}})
                db[time_table_collection].find_one_and_update({"course": "MCA", "semester": "1"},
                                                              {"$set": {"latest": time_table}})
                break

            else:
                continue

        _, uid, empty = fetch_empty_slots("MCA")
        print(empty)
        print(uid)

    def random(self, list_of_teachers):
        global choice_taken
        while True:
            choice = random.choice(list_of_teachers)
            if choice != choice_taken:
                choice_taken = choice
                return choice
            else:
                continue


choice_taken = None
# this function must be modified as it's definition isn't the supposed definition.
# this function is supposed to be called before subject-teacher mapping and
# its aim to find the no. of free slots of a teacher for teaching a subject per week.
def fetch_empty_slots(course):
    empty_slots = db[teacher_collection].find({"course": str(course)},
                                              {"_id": 0, "empty_slots": "true",
                                               "name": "true", "uid": "true"})

    # this isn't required as per its objective
    names, uid, slots = [], [], []
    for value in empty_slots:
        names.append(value["name"])
        uid.append(value["uid"])
        slots.append(value["empty_slots"])

    return names, uid, slots


# called after subject-teacher mapping. It checks the availability of a teacher for a given day and slot(s)
def get_teacher_availability_for_a_slot(day, slot_to_check):
    q_string = "empty_slots" + "." + str(day)
    cursor = db[teacher_collection].find({q_string: str(slot_to_check)}, {"_id": 0, "name": "true", "uid": "true"})
    free_teachers_for_slot = []
    # making a list of dictionaries available teachers and their respective uid for a slot on a day
    for value in cursor:
        free_teachers_for_slot.append({value["name"]: value["uid"]})

    print(free_teachers_for_slot)
    return free_teachers_for_slot


# assign the teacher(s) about their subjects in different semesters
def update_subjects_of_teachers(list_of_dictionaries):
    for index in range(len(list_of_dictionaries)):
        for key, values in list_of_dictionaries[index].items():
            db[teacher_collection].find_one_and_update({"uid": str(key)},
                                                       {"$set": {"subjects": values}})


obj = TimeTable()
val0, val, val2 = fetch_empty_slots("MCA")
obj.place(val0)
