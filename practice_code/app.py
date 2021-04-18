from flask import Flask, request, abort
from functools import wraps


def get_token_auth_header():
    # Unpack the request header
    if 'Authorization' not in request.headers:
        abort(401)

    # Headers is a dictionary object containing all header types
    auth_header = request.headers['Authorization']

    # Splitting the header on the space and taking the first part of the array
    # will give only the token
    header_parts = auth_header.split(' ')

    # First check that the token has two parts, and then check that the first
    # part is the keyword 'bearer'
    if len(header_parts) != 2:
        abort(401)
    elif header_parts[0].lower() != 'bearer':
        abort(401)

    return header_parts[1]


def requires_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        jwt = get_token_auth_header()
        return f(jwt, *args, **kwargs)
    return wrapper


app = Flask(__name__)


@app.route('/headers')
@requires_auth
def headers(jwt):
    print(jwt)
    return 'not implemented'

@app.route('/list')
def get_list():
    return 'not implemented'
