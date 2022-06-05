import random
import sys as _s

_chars = 'abcdefghijklmnopqrstuvwxyz!@#$%&*+-=?¿ABCDEFGHIJKLMNOPQRSTUVWXZ0123456789'
_alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789'

def run(list_Size = 16, mode = None):
    if mode == '--an':
        return ''.join(random.SystemRandom().choices([c for c in _alphanumeric], k=list_Size))
    else:
        return ''.join(random.SystemRandom().choices([c for c in _chars], k=list_Size))

if __name__ == "__main__":
    if len(_s.argv) == 1:
        print(run())
    elif len(_s.argv) == 2:
        try:
            if _s.argv[1].startswith('--'):
                print(run(mode=_s.argv[1]))
            else:
                print(run(int(_s.argv[1])))
        except:
            print(run())        
    else:
        try:
            if _s.argv[1].startswith('--'):
                print(run(int(_s.argv[2]),_s.argv[1]))
            else:
                print(run(int(_s.argv[1]),_s.argv[2]))
        except:
            print(run())  