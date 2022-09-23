from flask import Flask, jsonify, request
import random
import string

app = Flask(__name__)

text = 'V5'

def random_id_generator(digit_count):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(digit_count))

@app.route('/')
def home():
    return "Server is now active!", 200


@app.route('/random')
def random_():
    return "%s" % str(random_id_generator(10)), 200


@app.route('/version')
def version():
    return "%s" % str(text), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, threaded=True)


# sudo docker build -t test .
# sudo docker run -d -ti -p 5003:5003 test
