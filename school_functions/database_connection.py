from pymongo import MongoClient
from school_functions.school_database_variables import *

client = MongoClient(localhost)
db = client[school_database]

