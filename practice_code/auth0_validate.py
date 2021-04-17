import sys
import json
from jose import jwt
from urllib.request import urlopen
from cryptography.utils import int_from_bytes, int_to_bytes

# Configuration
# UPDATE THIS TO REFLECT YOUR AUTH0 ACCOUNT
AUTH0_DOMAIN = 'blackmer.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'fsnd'

'''
AuthError Exception
A standardized way to communicate auth failure modes
'''


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


'''
PASTE YOUR OWN TOKEN HERE
MAKE SURE THIS IS A VALID AUTH0 TOKEN FROM THE LOGIN FLOW

The problem here is that the code for the front end hasn't been written at this
point in the module, so it's not possible to get this token. I can probably
come back to this once the app is built.
'''
token = "hKFo2SBKTm1fbUlFWC0zVms4TExNR296bHlqamNGZ05qQWZtMqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIExCbFZWWmtTT0F2M2RLYVNZT2hzaFgxRE54TlFFZHpEo2NpZNkgc0dpcWRxMWRBZXRMMGM3WHk4UDNOaHhJTlZzemFVSHU"
# Auth Header


def verify_decode_jwt(token):
    # GET THE PUBLIC KEY FROM AUTH0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    # GET THE DATA IN THE HEADER
    unverified_header = jwt.get_unverified_header(token)

    # CHOOSE OUR KEY
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }

    # Finally, verify!!!
    if rsa_key:
        try:
            # USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
    }, 400)


verify_decode_jwt(token)
