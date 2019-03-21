import os
import subprocess
from Detached.Global.Functions.IndependentFunctions import insert_all
from Detached.Global.Functions.TeacherManagement import load_teachers_at_once

# stores address of Project folder(RADAtR)
RADAtR_location = str(subprocess.check_output('pwd'))[2:-3]

# stores body content of 'LocalUsersConfigurations.py' file
file_content = "project_location = '" + RADAtR_location + "/'"

print('\nChecking if the file for local configuration exists already...')
# checking if the file exists
file_exists = os.path.isfile('Detached/Global/Configurations/LocalUsersConfigurations.py')

if file_exists:
    print('File already exists.\n\nChecking configurations...')
    configuration_file = open('Detached/Global/Configurations/LocalUsersConfigurations.py', 'r')
    existing_content = str(configuration_file.readline())
    configuration_file.close()

    # matching existing configuration with current system configuration
    if (file_content + '\n') == existing_content:
        print('Configurations are already correct. Configuration is as follow:\n')
        configuration_file = open('Detached/Global/Configurations/LocalUsersConfigurations.py', 'r')
        print(configuration_file.readline())
        configuration_file.close()
    else:
        print('Configuration mismatch. Updating configuration...')
        configuration_file = open('Detached/Global/Configurations/LocalUsersConfigurations.py', 'w')
        configuration_file.write(file_content + '\n')
        configuration_file.close()
        print('Configuration updated. Current configuration(s) are as follow:\n')
        configuration_file = open('Detached/Global/Configurations/LocalUsersConfigurations.py', 'r')
        print(configuration_file.read())
        configuration_file.close()

else:
    print('No local configuration file found. Creating a new one...')
    configuration_file = open('Detached/Global/Configurations/LocalUsersConfigurations.py', 'x')
    configuration_file.write(file_content + '\n')
    configuration_file.close()
    print('File created. Current configuration(s) are as follow:\n')
    configuration_file = open('Detached/Global/Configurations/LocalUsersConfigurations.py', 'r')
    print(configuration_file.readline())

# #######   creating databases and collection required for the project ########
print('Loading subjects of different courses...')
insert_all()                                        # creating collection for subjects of each course
print('Loading Teachers...')
load_teachers_at_once()                  # creating collection for all teachers
print('All successfully done. You may run the project now')
