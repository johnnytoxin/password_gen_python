from base64 import urlsafe_b64encode
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from getpass import getpass
import os


def decrypt_file() -> None:
    # TODO: Provide an early exit
    file_path = None
    while not file_path:
        file_path = input('Enter the full path to your encrypted file: ')
        if not os.path.exists(file_path):
            print('File could not be found.')
            file_path = None

    master_pass = getpass(prompt='Enter your master password: ')
    token = None
    with open(file_path, 'r') as f:
        token = f.read()
    fernet = get_encrypter(master_pass)
    decrypted_token = fernet.decrypt(token.encode('utf-8'))
    password = decrypted_token.decode('utf-8')
    print(f'Your password was: {password}')


def get_encrypter(master_pass: str) -> Fernet:
    salt = b'notsosalt'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000
    )
    encoded_master_pass = master_pass.encode('utf-8')
    key_material = kdf.derive(encoded_master_pass)
    key = urlsafe_b64encode(key_material)
    return Fernet(key)
