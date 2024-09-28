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



# Пользуемся API:
# import requests


# try:
#     payload = {
#         "title": "Покормить кота",
#         "description": "Надо купить ему Whiskas или Purina, а то будет опять злой"
#     }

#     r = requests.post('http://192.168.0.103:5002/tasks', json=payload)
#     data = r.json()
#     print(data)
# except requests.exceptions.RequestException as error:
#     print(f'Возникла ошибка {error}')




# try:
#     payload = {
#         "description": "Или она выгуляет меня?",
#         "title": "Выгулять собаку"
#     }
#     r = requests.post('http://192.168.0.103:5002/tasks', json=payload)
#     data = r.json()
#     print(data)
# except requests.exceptions.RequestException as error:
#     print(f'Возникла ошибка {error}')





# try:
#     payload = {
#         "description": "Ведь они такие крутышки",
#         "title": "Погладить капибару"
#     }
#     r = requests.post('http://192.168.0.103:5002/tasks', json=payload)
#     data = r.json()
#     print(data)
# except requests.exceptions.RequestException as error:
#     print(f'Возникла ошибка {error}')




# try:
#     r = requests.get('http://192.168.0.103:5002/tasks')
#     data = r.json()
#     print(data)
# except requests.exceptions.RequestException as error:
#     print(f'Возникла ошибка {error}')




# url = f'http://192.168.0.103:5002/tasks?id=1'
# try:
#     response = requests.delete(url)
#     if response.status_code == 200:
#         data = response.json()
#         print(f"Задача 1 успешно удалена: {data}")
#     elif response.status_code == 404:
#         print(f"Задача с ID 1 не найдена.")
#     else:
#         print(f"Ошибка: статус-код {response.status_code}, ответ: {response.text}")

# except requests.exceptions.RequestException as e:
#     print(f"Возникла ошибка при отправке запроса: {e}")
