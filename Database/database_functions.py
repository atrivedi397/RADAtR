from Database.database_connection import *


# function to register the first time user/admin
def first_time_admin_registration(usrname, passwd):
    db[admin_collection].insert({"admin_name": usrname, "password": passwd})
    print("success")


# function which will verify if the user is already registered or not
def verify_admin(usrname, passwd):
    if_user_exists = db[admin_collection].find_one({"admin_name": usrname, "password": passwd})
    if if_user_exists is not None:
        print("Found And Matched")
        return True
    else:
        print("User Not Found")
        return False


# initially saving the school details
def save_school_details(name, board, level_of_education, classroom_no,
                        total_teachers, working_days, address, working_hours):
    db[school_info].insert({"name": name, "board": board, "level_of_education": level_of_education,
                            "classroom_no": classroom_no, "total_teachers": total_teachers,
                            "working_days": working_days, "address": address, "working_hours": working_hours,
                            "data_inserted": "true"})
    print("entered successfully")


# finally getting the school details (searching can be done only by name of school)
def get_school_details(name=None):
    cursor = db[school_info].find({"name": name}, {"_id": 0})
    school_details = {key: None for key in school_attrib}
    for value in cursor:
        school_details.update(value)

    for k, v in school_details.items():
        print(k, " : ", v)

    return school_details


# call this function for saving fee details for the first time ever
def save_fee_details(admission_fee, re_admission_fee, tuition_fee, late_fee,
                     vvn, computer_fee, project_fee, other_fee):
    db[fee_details].insert({"admission_fee": admission_fee, "re_admission_fee": re_admission_fee,
                            "tuition_fee": tuition_fee, "late_fee": late_fee, "vvn": vvn,
                            "computer_fee": computer_fee, "project_fee": project_fee, "other_fee": other_fee})


# call this function to get fee details from database
def get_fee_details():
    cursor = db[fee_details].find({}, {"_id": 0})
    fee = {key: None for key in fee_attrib}
    for value in cursor:
        fee.update(value)

    for k, v in fee.items():
        print(k, " : ", v)

    return fee


def if_details_are_inserted():
    cursor = db[school_info].find({"data_inserted": "true"}, {"_id": 0})

    if cursor["data_inserted"] == "true":
        print("true")


if __name__ == "__main__":
    """first_time_admin_registration("abhishek", "123456789")
    verify_admin("abhishek", "123456789")
    verify_admin("abhishek", "12345678")
    save_school_details("KV", "CBSE", "12", 50, 80, 5, "Raebareli", "7:30-1:30")
    get_school_details("KV")

save_fee_details(1000, 2000, 3000, 6000, 5000, 9000, 6000, 4000)
print(get_fee_details())"""
    if_details_are_inserted()
