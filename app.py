import json

from flask import Flask, request
from to_do import todos
import db_functions

app = Flask(__name__)


@app.route('/api/', methods=["GET"])
def get_all_todos():
    return db_functions.get_all_todos(), 200


@app.route('/api/<string:todo_id>', methods=["GET"])
def get_todo_by_id(todo_id):
    todo = db_functions.get_todo_by_id(todo_id)
    if len(todo) == 0:
        return json.dumps(todo), 200
    else:
        return "Todo not found!!!", 404


@app.route('/api/', methods=["POST"])
def create_todo():
    new_todo = request.get_json()
    res = db_functions.create_todo(new_todo)
    if len(res) != 0:
        return res, 200
    else:
        return "Todo already exists", 400


@app.route('/api/', methods=["PUT"])
def update_todo():
    updated_todo = request.get_json()
    res = db_functions.update_todo(updated_todo)
    if res is not None:
        return res, 200
    else:
        return "Bad Request, todo doesn't exist!!!", 400


@app.route('/api/<string:todo_id>', methods=["DELETE"])
def delete_todo_by_id(todo_id):
    res = db_functions.delete_todo(todo_id)
    if res is not None:
        return res, 200
    else:
        return "Bad Request, todo doesn't exist!!!", 400


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

if __name__ == '__main__':
    app.run()
