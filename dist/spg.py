import argparse

parser=argparse.ArgumentParser(
    description='A tool for generating strong passwords to prevent from being hacked by social engineering, brute force or dictionary attack method.',
    epilog='github.com/malexandersalazar/tools-python-secure-password-generator')

def length_argument(x):
    x = int(x)
    if x < 12:
        raise argparse.ArgumentTypeError("Minimum length is 12")
    return x

parser.add_argument('-m','--mode', choices=['s','a'], default='s', type=str, help='specifies the mode in which the password generation should be executed, "s" for secure and "a" for alphanumeric (default: "s")')
parser.add_argument('-l','--length', default=16, type=length_argument, help='specifies the password length (default: 16, min: 12)')
parser.add_argument('-q','--quantity', default=1, type=int, help='specifies the number of passwords that should be generated (default: 1)')
args=parser.parse_args()

MODE = args.mode
LENGTH = args.length
QUANTITY = args.quantity

import random
import sys as _s

_chars = """abcdefghijklmnopqrstuvwxyz!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ABCDEFGHIJKLMNOPQRSTUVWXZ0123456789"""
_symbols = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
_alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789'

def validate_secure(pwd):
    contains_upper = False
    contains_lower = False
    contains_special = False
    for s in pwd:
        if s.isupper():
            contains_upper = True
        elif s.islower():
            contains_lower = True
        elif s in _symbols:
            contains_special = True
    return contains_upper and contains_lower and contains_special


def run(mode,length,quantity):
    for i in range(quantity):
        if mode == 's':
            is_secure = False
            while not is_secure:
                pwd = ''.join(random.SystemRandom().choices([c for c in _chars], k=length))
                is_secure = validate_secure(pwd)
        else:
            pwd = ''.join(random.SystemRandom().choices([c for c in _alphanumeric], k=length))

        print(pwd)

run(MODE,LENGTH,QUANTITY)