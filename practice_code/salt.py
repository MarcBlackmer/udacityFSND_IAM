import bcrypt
import sys

pwd_list = {b'securepassword', b'udacity', b'learningisfun'}


def salt(password):
    salt = bcrypt.gensalt(14)
    hashed = bcrypt.hashpw(password, salt)
    print(salt)
    print(hashed)

    bcrypt.checkpw(password, hashed)


for password in pwd_list:
    salt(password)
