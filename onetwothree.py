from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random_number', methods=['GET'])
def get_random_number():
    numbers = ["one", "two", "three"]
    random_number = random.choice(numbers)
    response = {'result': random_number}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
