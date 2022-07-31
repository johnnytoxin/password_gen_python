import json
import os
from encrypter import decrypt_file, get_encrypter
from generators import generate_character_key, generate_word_key
from getpass import getpass
from pathlib import Path


DATA_DIR = f'{os.path.dirname(__file__)}/data'
ANIMALS_FILE_PATH = os.path.join(DATA_DIR, 'animals.json')
PLACES_FILE_PATH = os.path.join(DATA_DIR, 'places.json')
TITLES_FILE_PATH = os.path.join(DATA_DIR, 'titles.json')

animals = []
places = []
titles = []


def load_file(file_path: str) -> list:
    with open(file_path, 'r') as f:
        file_data = f.read()
        return json.loads(file_data)


def load_word_data():
    global animals
    animals = load_file(ANIMALS_FILE_PATH)
    global places
    places = load_file(PLACES_FILE_PATH)
    global titles
    titles = load_file(TITLES_FILE_PATH)


def prompt_for_operation() -> None:
    valid_selections = ['1', '2', '3', 'q']
    selection = None
    while selection == None:
        print('(1) Generate a word key')
        print('(2) Generate a character key')
        print('(3) Decrypt password file')
        print('\n(Q) Quit application')

        selection = input('\nYour selection: ')
        if selection.casefold() not in valid_selections:
            selection = None
    if selection == 'q':
        return None
        
    if selection == '1':
        new_password = generate_word_key(animals, places, titles)
        prompt_for_save(new_password)
    elif selection == '2':
        new_password = generate_character_key()
        prompt_for_save(new_password)
    elif selection == '3':
        decrypt_file()


def prompt_for_save(new_password: str) -> None:
    file_path = None
    filename = None
    while not file_path:
        file_path = input('\nPlease enter a full path: ')
        if not file_path:
            print('\nProvided value is empty.')
        try:
            Path(file_path).resolve()
        except OSError:
            print('\nInvalid path.')
            file_path = None
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    while not filename:
        filename = input('\nPlease enter a name for your new file (no extension): ')
        if '.' in filename:
            filename = filename.split('.')[0]

    master_pass = getpass(prompt='Enter a master password to lock the file: ')
    fernet = get_encrypter(master_pass)
    token = fernet.encrypt(new_password.encode('utf-8'))

    file_full_path = os.path.join(file_path, filename)
    with open(file_full_path, 'wb') as f:
        f.write(token)


if __name__ == '__main__':
    try:
        print('''
######################
## PASSWORD UTILITY ##
######################
        ''')
        load_word_data()
        prompt_for_operation()
    except Exception as e:
        print(f'An unhandled exception occurred: {e}')
