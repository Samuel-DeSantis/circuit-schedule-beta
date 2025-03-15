import flask

from db.connection import db
from db.seed import seed_circuit_schedule
from middleware.authenticator import Authenticator

app = flask.Flask(__name__)
auth = Authenticator()
seed_circuit_schedule()

@app.route('/')
def home():
    return flask.jsonify({'message': 'Welcome to the API!'})

@app.route('/api/v1/circuit_schedule', methods=['GET'])
def get_circuit_schedule():
    circuit_schedule = db.table('circuit_schedule').read()
    return flask.jsonify(circuit_schedule), 200

@app.route('/api/v1/auth/register', methods=['POST'])
def register():
    data = flask.request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')

    # Check if user already exists
    existing_user = db.table('users').filter({'username': username})
    if existing_user:
        return flask.jsonify({'error': 'User already exists'}), 409

    # Hash the password
    hashed_password = auth.encrypt(password)

    # Create new user
    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'username': username,
        'password': hashed_password
    }

    db.table('users').record.create(new_user)

    # Remove password from the response
    del new_user['password']

    return flask.jsonify(new_user), 201

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    data = flask.request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if user exists
    user = db.table('users').filter({'username': username})

    # Check if user is found
    if not user:
        return flask.jsonify({'error': 'User not found'}), 404

    # Check if password is correct
    if not auth.check(password, user['password']):
        return flask.jsonify({'error': 'Invalid password'}), 401

    # Remove password from the response
    del user['password']

    return flask.jsonify(user), 200

app.run()