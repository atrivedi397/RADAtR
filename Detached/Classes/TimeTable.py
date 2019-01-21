from Detached.Global.Variables.varFile1 import maximumSlots
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
        """This will select the 'freeSlots' of a teacher at a time. After that it will iterate on 'freeLectures' to place or
           update its(freeLecture) value. Once 'freeLecture' gets updated, another teacher will get selected. The procedure goes on
           until either all the subjects have enough lectures or teacher maximum lecture value is reached. Which teacher to select
           could either be in sequence or could be random"""
        pass

    def random(self):
        # picks teachers randomly
        pass


"""Argument to this function should be of type 
value = [{"21136": ["System Programming", "Programming Lab-2"]},
         {"21135": ["CBOT", "Programming Lab-3"]}]
"""


def update_subjects_of_teachers(list_of_dictionaries):
    for index in range(len(list_of_dictionaries)):
        for key, values in list_of_dictionaries[index].items():
            db[teacher_collection].find_one_and_update({"uid": str(key)},
                                                       {"$set": {"subjects": values}})


# update_subjects_of_teachers(value)
