from flask import Flask, request, Response, jsonify
import json
from http import HTTPStatus

app = Flask(__name__)
tasksList = []
number_of_tasks = 0

@app.get('/tasks')
def get_tasks():
    global tasksList
    return jsonify({'task': tasksList}), 200

@app.post('/tasks')
def post_tasks():
    global tasksList
    global number_of_tasks
    title = request.json.get('title')
    description = request.json.get('description')
    if not title or not description:
        return jsonify('Вы хотите добавить пустую карточку.'), HTTPStatus.BAD_REQUEST
    else:
        number_of_tasks += 1
        task = {
            'title': title,
            'description': description,
            'task_id': number_of_tasks
        }
        tasksList.append(task)
        r = Response()
        r.mimetype = 'application/json'
        r.response = json.dumps(tasksList)
        r.status_code = HTTPStatus.OK
        return r, 201

@app.route('/tasks/<int:id>', methods = ['DELETE'])
def delete_tasks(id):
    global tasksList
    global number_of_tasks
    task = next((task for task in tasksList if task['task_id'] == id), None)
    if not task:
        return jsonify({'message': 'Задача не найдена'}), 404
    tasksList.remove(task)
    number_of_tasks -= 1
    r = Response()
    r.mimetype = 'application/json'
    r.response = json.dumps(tasksList)
    r.status_code = HTTPStatus.OK
    return r, 200



if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')