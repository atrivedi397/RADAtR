# -------- values decided by governing authority -----
totalWorkingDays = 5
maximumSlots = 6  # maximum possibility of total lectures in a day
days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
starting_time = 1000
duration = 100  # in hrs
time_slot = ["1000"]

for i in range(maximumSlots):
    list_content = starting_time + duration
    starting_time = list_content
    # print (list_content)
    convert_to_str = str(list_content)
    time_slot.append(convert_to_str)
print(time_slot)
dictionary_of_teachers = [
    {'DR. SHALINI CHANDRA': ['Object Oriented Programming & C++', 'Internet and Java Programming', 'Programming Lab-3']},
    {'DR. NARENDRA KUMAR': ['Computer Architecture', 'Elective Paper-1']},
    {'DR DEEPA RAJ ': ['Discrete Structures', 'DATA STRUCTURES', 'Analysis and Design of Algorithm']},
    {'DR. MANOJ KUMAR ': ['Computer Based Numerical & Statistical Techniques', 'Graph Theory and Combinatorics']},
    {'PROFF. SANJAY KUMAR DWIVEDI': ['System Programming', 'Operating System', 'Compiler Design',
                                    'Artificial Intelligence']},
    {'PROFF. VIPIN SAXENA': ['Software Engineering']}]

for i in dictionary_of_teachers:
    for j,k in i:
        print(j)

# print(dictionary_of_teachers)

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
