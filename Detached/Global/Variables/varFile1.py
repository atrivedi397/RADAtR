# -------- values decided by governing authority -----
totalWorkingDays = 5
maximumSlots = 6                    # maximum possibility of total lectures in a day

starting_time = 1000
duration = 60                       # in minutes
lunch_slot_no = 4

# -------- teacher oriented variables --------------
# Professors Ranks
professor = "Professor"
associate_prof = "Associate_prof"
assistant_prof = "Assistant_prof"

# used to generate teacher's ID
id_number = 10001

db_variables = {"totalWorkingDays": str(totalWorkingDays), "maximumSlots": str(maximumSlots),
                "days_list": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "professor": str(professor), "associate_prof": str(associate_prof),
                "assistant_prof": str(assistant_prof),
                "id_number": str(id_number)}
