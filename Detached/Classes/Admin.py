import enum


# representational type used for login status of an admin
class Status(enum):
    active = True
    inactive = False


# class for creating administrator information
class Admin:            # (class under development)
    def __init__(self):
        # variables commented will be required in future
        # self.name = None
        # self.ID = None
        # self.password = None
        # self.email = None
        self.department = {}                            # format => { "DepartmentNames" : ["CoursesUnderTheDepartment"] }
        self.loginStatus = Status.active                # to avoid the same admin in logging at multiple remotes
