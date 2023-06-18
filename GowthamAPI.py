#I can use Django framework too, but this is don't need much complexity so uing Flask.
from flask import Flask, jsonify, request
import time



app = Flask(__name__)

@app.route('/')
def say_hi():
    return "This is Gowtham's API for House Price Prediction"


@app.route('/timestamp')
def time_():
    timestamp = int(time.time())
    return jsonify({'timestamp': timestamp})

@app.route('/readdata', methods=['POST'])
def readdata():
    data = request.get_json()
    return jsonify(data)

@app.route('/noexist')
def not_found():
    response = jsonify({'error': 'Not Found'})
    response.status_code = 404
    response.status = '404 Not Found'
    return response.status

if __name__ == '__main__':
    app.run(debug= False)