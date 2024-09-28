from flask import Flask
import random

app = Flask(__name__)

@app.get('/random-quote')
def get_quote():
    with open('quotes.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines() # каждая строка прочитана и добавлена в список
        return random.choice(lines)


if __name__ == '__main__':
    app.run(port=5002, host='0.0.0.0')

# открывать на http://192.168.0.113:5002/random-quote

# import requests
#
# try:
#     r = requests.get('http://192.168.0.113:5002/random-quote')
#     print(r.text)
# except requests.exceptions.RequestException as error:
#     print(f'Возникла ошибка {error}')