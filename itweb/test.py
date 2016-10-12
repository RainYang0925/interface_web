import os
import string
import random

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, "static")
print BASE_DIR
print STATIC_ROOT

chars = string.digits
s = ''
length = len(chars) - 1
for i in range(11):
    s += chars[random.randint(0, length)]
print s


def random_phonenum():
    chars = string.digits
    s = ''
    length = len(chars) - 1
    for i in range(11):
        s += chars[random.randint(0, length)]
    return s
