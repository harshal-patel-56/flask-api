import pymongo

# DEFAULT DB CONFIGURATIONS
DB_NAME = "todo_test"
DB_PASS = ""

# DEFAULT MySQL CONNECTION CONFIGURATIONS
URI = "mongodb+srv://flask_api:" + DB_PASS + "@todos-kithc.mongodb.net/" + DB_NAME + "?retryWrites=true&w=majority"
CLIENT = pymongo.MongoClient(URI)

# CONNECTION TO DB
db = CLIENT[DB_NAME]

# DB_CURSOR OBJECT
todos_info = db["todos"]
