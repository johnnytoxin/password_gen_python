import string
from random import choice, randrange, random


def generate_character_key() -> str:
    minimum_length = 8
    random_range = 6
    length = 0
    new_password = ''
    while length < minimum_length:
        length = input('Enter password length (minimum: 8): ')
        if length.isnumeric():
            length = int(length)
            if length < minimum_length:
                print(f'\nLength must be greater than {minimum_length} characters. Please enter again.')

    decided_on_special_characters = False
    has_special_characters = None
    while not decided_on_special_characters:
        selection = input('Do you want special characters [y/n]?: ')
        if selection in ['y', 'n']:
            decided_on_special_characters = True
            has_special_characters = selection == 'y'

    for i in range(length):
        # First letter is always a capital letter
        if i == 0:
            new_password += generate_letter(i, False)
        # Generate a random alphabetical character or special character
        elif i > 0 and i < length - 1:
            random_int = randrange(0, random_range)
            new_password += generate_letter(random_int, has_special_characters)
        elif i == length - 1:
            # Generate a guaranteed special character as the last character if provided
            new_password += generate_letter(random_range, has_special_characters)

    print(f'Your new password is: {new_password}')
    return new_password


def generate_letter(random_int, has_special_character) -> str:
    common_special_characters = [ '?', '_', '-', '!', '@', '$', '#', '&' ]
    if random_int in [0, 1, 2, 3, 4]:
        return choice(string.ascii_letters)
    elif random_int == 5:
        return str(randrange(0, 10))
    elif random_int == 6:
        if has_special_character:
            index = randrange(0, len(common_special_characters))
            return common_special_characters[index]
        else:
            return str(randrange(0, 10))
    else:
        raise Exception(f'Unexpected random value received in `generate_letter` function: {random_int}')


def generate_word_key(animals: list, places: list, titles: list) -> str:
    new_password = None
    unique_title = get_random_element(titles)
    unique_place = get_random_element(places)
    unique_animal = get_random_element(animals)

    random_number = str(randrange(0, 10))
    first_or_second_position = random() < 0.5

    if first_or_second_position:
        new_password = (
            unique_title
            + unique_place
            + '_'
            + unique_animal
            + random_number
        )
    else:
        new_password = (
            unique_title
            + '_'
            + unique_place
            + unique_animal
            + random_number
        )
    
    print(f'Your new password is: {new_password}\n')
    return new_password


def get_random_element(array: list) -> str:
    random_index = randrange(0, len(array))
    return array[random_index]
