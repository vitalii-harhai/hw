from math import ceil
from random import choice, randint, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_password(start=10, end=20) -> str:
    """
    Generates a random password length between start and end
    For generate password using four types - lowercase, uppercase, digits and punctuation
    For expansion add character as sequence in variable rand_list
    :param start: Range start length
    :param end: Range end length
    :return: random password
    """

    password_length = randint(start, end if end >= start else start)
    rand_list = [ascii_lowercase, ascii_uppercase, digits, punctuation]
    repetition = ceil(password_length / len(rand_list))

    shuffle(rand_list)
    password = ''
    for i in range(repetition):
        for item in rand_list:
            if len(password) >= password_length:
                break
            password += choice(item)

    password = list(password)
    shuffle(password)
    password = ''.join(password)

    return password
