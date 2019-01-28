# This file is created to resolve all the dependencies of database connection by its own.
# Inclusion of mere this file is enough where any kind of database operation occur
from pymongo import MongoClient
from Detached.Global.Variables.varDB import *

client = MongoClient(localhost)         # connecting to server
db = client[database]                   # choosing the desired DB on the server
