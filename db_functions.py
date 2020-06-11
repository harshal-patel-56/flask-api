from bson import ObjectId

from db_config import db, todos_info
import json


# sample_todo = {
#     "_id": "5ee201663f10c2767f989684",
#     "title": "Fifth To-Do Updated",
#     "is_completed": True
# }

def get_all_todos():
    todos = []
    for x in todos_info.find():
        x["_id"] = str(x["_id"])
        todos.append(x)
    return json.dumps(todos)


def get_todo_by_id(id):
    todos = []
    for x in todos_info.find({"_id": ObjectId(id)}):
        x["_id"] = str(x["_id"])
        todos.append(x)
    return json.dumps(todos)


def create_todo(new_todo):
    x = todos_info.insert_one(new_todo)
    res = {"_id": str(x.inserted_id)}
    return json.dumps(res)


def update_todo(updated_todo):
    query = {"_id": ObjectId(updated_todo["_id"])}
    res = todos_info.update_one(query, {
        "$set": {"title": updated_todo["title"], "is_completed": updated_todo["is_completed"]}})
    if res.modified_count == 1:
        return "Updated Successfully!!!"
    else:
        return None


def delete_todo(todo_id):
    query = {"_id": ObjectId(todo_id)}
    res = todos_info.delete_one(query)
    if res.deleted_count == 1:
        return "Deleted Successfully!!!"
    else:
        return None
