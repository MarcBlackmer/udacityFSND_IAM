'''
The base code is taken from exercise code in the cryptography practice section
'''

from cryptography.fernet import Fernet


def main():
    def default_encryption():
        key = Fernet.generate_key()
        f = Fernet(key)
        print(key)

        plaintext = b'encryption is very useful'
        ciphertext = f.encrypt(plaintext)
        print(ciphertext)

        decryptedtext = f.decrypt(ciphertext)
        print(decryptedtext)

    def exercise_1():
        key = b'8cozhW9kSi5poZ6TWFuMCV123zg-9NORTs3gJq_J5Do='
        f = Fernet(key)

        ciphertext = b'gAAAAABc8Wf3rxaime-363wbhCaIe1FoZUdnFeIXX_Nh9qKSDkpBFPqK8L2HbkM8NCQAxY8yOWbjxzMC4b5uCaeEpqDYCRNIhnqTK8jfzFYfPdozf7NPvGzNBwuuvIxK5NZYJbxQwfK72BNrZCKpfp6frL8m8pdgYbLNFcy6jCJBXATR3gHBb0Y='

        decryptedtext = f.decrypt(ciphertext)
        print(decryptedtext)

    def exercise_2():
        key = b'8cozhW9kSi5poZ6TWFuMCV123zg-9NORTs3gJq_J5Do='
        f = Fernet(key)

        plaintext = b'encrypting is just as useful'
        ciphertext = f.encrypt(plaintext)
        print(ciphertext)

    exercise_1()
    exercise_2()


main()
