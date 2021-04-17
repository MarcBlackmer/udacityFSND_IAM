import jwt
import base64

'''
This script will encode and then decode the three variables below.

The decode method expects the algorithms to be a list or dictionary, but the
script can only handle a single value, currently.

I'll also have to figure out how to make the passing of the variable values
more dynamic.
'''

payload = {'school': 'udacity'}
algo = 'HS256'  # HMAC-SHA 256
secret = 'learning'


def main():

    def encode_jwt(payload, secret, algorithm):
        encoded_jwt = jwt.encode(payload, secret, algorithm=algorithm)
        print('Encoded JWT = ' + encoded_jwt)
        decode_jwt(encoded_jwt, secret, algo)
        decode_base64(encoded_jwt)

        return encoded_jwt

    def decode_jwt(encoded_jwt, secret, algorithms):
        try:
            decoded_jwt = jwt.decode(
                encoded_jwt, secret, verify=True, algorithms=[algo])
            print('Decoded JWT = ' + str(decoded_jwt))
        except Exception as e:
            print(e)
            pass

        return decoded_jwt

    def decode_base64(encoded_jwt):
        decoded_base64 = base64.b64decode(
            str(encoded_jwt).split(".")[1] + "==")
        print('Base64-decoded JWT = ' + str(decoded_base64))

        return decoded_base64

    encode_jwt(payload, secret, algo)


main()
