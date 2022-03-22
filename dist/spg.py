import random
import sys as _s

_chars = 'abcdefghijklmnopqrstuvwxyz!@#$%&*+-=?¿ABCDEFGHIJKLMNOPQRSTUVWXZ0123456789'

def run(list_Size = 16):
    return ''.join(random.SystemRandom().choices([c for c in _chars], k=list_Size))

if __name__ == "__main__":
    if(len(_s.argv) == 1):
        print(run())
    else:
        try:
            print(run(int(_s.argv[1])))
        except:
            print(run())