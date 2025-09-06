from flask import Flask, request, Response
import json
from http import HTTPStatus

app = Flask(__name__)

@app.route('/api/convert-temperature', methods = ['POST'])
def celsius_to_fahrenheit():
    celsius = request.json.get('celsius')
    if celsius is None:
        return f'Вы ничего не передали'
    else:
        r = Response()
        r.mimetype = 'application/json'
        mydict = dict()
        fahrenheit = celsius * 1.8 + 32
        mydict['fahrenheit'] = fahrenheit
        # кодируем словарь в формат JSON
        r.response = json.dumps(mydict)
        r.status = HTTPStatus.OK
        return mydict

if __name__ == '__main__':
    app.run(debug=True, port=5002, host='0.0.0.0')



# Используем API
# import requests
#
#
# try:
#     payload = {
#         "celsius": 25
#     }
#     r = requests.post('http://192.168.0.113:5002/api/convert-temperature', json=payload)
#     data = r.json()
#     print(data)
# except requests.exceptions.RequestException as error:
#     print(f'Возникла ошибка {error}')
