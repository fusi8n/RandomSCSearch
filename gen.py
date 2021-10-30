import random
import string
import webbrowser


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    numbers = string.digits
    result_str = ''.join(random.choice(letters+numbers) for i in range(length))
    link = 'http://prnt.sc/'
    actual = link + result_str
    print(actual)

    webbrowser.open(actual)

get_random_string(6)

