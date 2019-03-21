import random

from Detached.Global.Variables.varFile1 import *
from Detached.Global.Configurations.ConnectionEstablishment import *
from Detached.Classes.Course import *

prev_time_tables = []


# class for generating Time Table for a single batch
class TimeTable:
    def __init__(self, course, semester=None, batch=1, batch_timing=starting_time):
        self.batchNo = batch                        # batch (could be alphanumeric, numeric, alphabetical)
        self.batchTiming = batch_timing             # time at which the batch starts
        self.course = course
        self.semester = str(semester)                    # semester is stored into string format in the database
        self.totalSlots = maximumSlots              # decides till when the batch will go on

        # contains the mappings of teachers and their subject
        self.lectures = []                          # format => [ {"teacher1" : "subject1"}, {"teacher2" : "subject2"} ]

        # initially empty, will be updated only by place()/assign() function
        self.assignedLectures = []          # format => [ {"Monday" : [1,2,3] }, {"Tuesday" : [1,2,3,4] } ]

        # initially empty, used as the list on which to iterate for placing lectures
        self.freeLectures = []
    
        # obtaining all subjects taught in a given semester of a given course
        self.subjectList = get_list_of_subject_for(self.course, self.semester)

    # creating a dictionary for subject as key and teaching hours per week per subject as 4
    def create_dict_per_week_lecture_hrs(self):
        lecture_per_week = {subject: 0 for subject in self.subjectList}
        return lecture_per_week

    def place(self, teacher_to_place):   # teacher-subject mapping should be provided with teacher as keys

        # getting a dictionary of subject and respective lectures per week
        lecture_per_week = self.create_dict_per_week_lecture_hrs()

        """Checking and returning the last value if the limit of time table generation is reached"""
        if len(prev_time_tables) >= time_table_generation_limit:
            print(f"You cannot generate more than {time_table_generation_limit} time tables,"
                  f" so returning the last generated.")
            for day in prev_time_tables[-1]:
                print(day, "\n")
            return prev_time_tables[-1]

        # Else generating a new time table under the limit of time table generation
        else:
            teacher_list = []
            for value in teacher_to_place:
                temp_name = str(value.keys())
                name = temp_name[12:-3]  # only extracting the name from whole word from string "dict_keys([\\Name\\])"
                teacher_list.append(name)

            while True:
                # creating a matrix for [days*slots], rows represents days and columns represent slots
                # it is a nested list of dictionaries in which every dictionary represent {teacher:subjects}
                time_table = [[{} for _ in range(maximumSlots)] for _ in range(len(days_list))]
                for slot in range(maximumSlots):
                    for day in range(len(time_table)):
                        # randomly picking a teacher from the given mapping
                        """teacher_to_place.keys() can be replaced with teacher_
                           to_place only iff the argument teacher_to_place is a list"""
                        selected_teacher = self.random(teacher_list)

                        # checking if the randomly selected teacher is available for a particular slot or not
                        if selected_teacher in get_teacher_availability_for_a_slot(days_list[day], slot + 1):
                            for dictionary in teacher_to_place:
                                if selected_teacher in dictionary:
                                    # actual placing of teacher-subject mapping
                                    time_table[day][slot][selected_teacher] = dictionary[selected_teacher]

                                    # adding 1 each time the subject is allotted/placed
                                    lecture_per_week[dictionary[selected_teacher][0]] += 1

                                    # counting the allotted lectures
                                    # ensuring the lectures do not exceed 4 hours a week
                                    if lecture_per_week[dictionary[selected_teacher][0]] >= 4:
                                        teacher_list.remove(selected_teacher)
                        else:
                            time_table[day][slot]["not"] = "-"  # putting blank if selected teacher is not free for slot

                # appending the new random time table if it was not already generated one
                if time_table not in prev_time_tables:
                    prev_time_tables.append(time_table)
                    print(f"You have created {len(prev_time_tables)} time tables.")
                    for day in time_table:
                        print(day, "\n")
                    return prev_time_tables[-1]
                # if only one teacher-subject mapping given(6 sem MCA), then saving from infinite loop.
                elif len(teacher_to_place) == 1:
                    for day in time_table:
                        print(day, "\n")
                    return prev_time_tables[-1]
                # else continuing with next unique generation
                else:
                    continue

    def store_time_table_in_db(self):
        i = 0
        for index in range(len(prev_time_tables[-1])):
            for _ in range(len(prev_time_tables[-1][index])):
                query = "empty_slots" + ".$[]." + str(days_list[i])
                slot_no = str(index + 1)
                # pulling out the empty_slots from respective teachers
                db[teacher_collection].find_one_and_update({"uid": str(prev_time_tables[-1][index][i])},
                                                           {"$pull": {query: slot_no}})
                if i >= 4:
                    i = 0
                else:
                    i += 1
        # saving the time_table in database for semester(semester, course can be changed),
        """Inclusion of batch number and batch timings are yet to be sent and stored to database"""
        db[time_table_collection].find_one_and_update({"course": self.course, "semester": self.semester},
                                                      {"$set": {"latest": prev_time_tables[-1]}})

    @staticmethod
    def random(list_of_teachers):
        global choice_taken
        # the teachers list will become of length zero when all the teachers \
        # have been allotted all the 4 lectures in a week, hence returning none
        if len(list_of_teachers) == 0:
            return None

        # returning the same value if only one mapping is present
        elif len(list_of_teachers) == 1:
            return random.choice(list_of_teachers)
        else:
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
        free_teachers_for_slot.append(value["name"])  # can be changed to value["uid"] if uid is needed

    # print(free_teachers_for_slot)
    return free_teachers_for_slot


# assign the teacher(s) about their subjects in different semesters
def update_subjects_of_teachers(list_of_dictionaries):
    for index in range(len(list_of_dictionaries)):
        for key, values in list_of_dictionaries[index].items():
            db[teacher_collection].find_one_and_update({"uid": str(key)},
                                                       {"$set": {"subjects": values}})
