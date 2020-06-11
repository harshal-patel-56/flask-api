import json

todos = []

todo = {
    "id": 1,
    "title": "First To-Do",
    "is_completed": False
}

todos.append(todo)

todo = {
    "id": 2,
    "title": "Second To-Do",
    "is_completed": True
}

todos.append(todo)

todo = {
    "id": 3,
    "title": "Third To-Do",
    "is_completed": False
}

todos.append(todo)

# print("Current static todos : " + json.dumps(todos))
