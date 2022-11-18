import random
import string

def get_random_string(length):
    characters = string.ascii_lowercase + string.digits + string.punctuation
    result_str = ''.join(random.choice(characters) for i in range(length))
    return result_str

def get_random_code(length):
    characters = string.ascii_lowercase + string.digits
    result_str = ''.join(random.choice(characters) for i in range(length))
    return result_str
    

