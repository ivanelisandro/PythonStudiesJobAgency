import math


def validate(number):
    try:
        return int(number)
    except ValueError:
        print('Please pass a number like "5" or 5')
    return None


def find_sqrt(number):
    try:
        print(math.sqrt(number))
    except TypeError:
        number = validate(number)
        if number:
            print(math.sqrt(number))
