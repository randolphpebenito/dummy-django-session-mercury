import random
import string




#from shortener.models import KirrURL

def code_generator(size=5, chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for _ in range(size))

c = code_generator()
print c
