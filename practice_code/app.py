from flask import Flask, request, abort, jsonify
import json
from functools import wraps
from jose import jwt
from urllib.request import urlopen

AUTH0_DOMAIN = 'blackmer.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'fsnd'


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


def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'Permissions not included in JWT.'
        }, 400)

    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'Permission not found.'
        }, 403)
    return True


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            jwt = get_token_auth_header()
            try:
                payload = verify_decode_jwt(jwt)
            except:
                abort(401)

            check_permissions(permission, payload)

            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator


app = Flask(__name__)


@app.route('/login-results')
@requires_auth
def headers(jwt):
    print(jwt)
    return 'not implemented'


@app.route('/images')
@requires_auth
def images(jwt):
    print(jwt)
    return 'not implemented'
