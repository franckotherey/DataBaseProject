import random
import string

def get_random_string(length):
    characters = string.ascii_lowercase + string.digits    
    result_str = ''.join(random.choice(characters) for i in range(length))
    return result_str

def get_random_text(max_length):
    characters = string.ascii_lowercase + ' '
    result_str = ''.join(random.choice(characters) for i in range(random.randint(25, max_length)))
    return result_str


#print(get_random_text(40))