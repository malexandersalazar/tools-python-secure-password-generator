# %%
import random
import sys as _s

# %%
_chars = 'abcdefghijklmnopqrstuvwxyz^¡!@$%*+-=&#?¿ABCDEFGHIJKLMNOPQRSTUVWXZ0123456789'
_alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZ0123456789'

# %%
def run(**kwargs):
    mode = kwargs.pop('mode')
    size = kwargs.pop('size')

    for i in range(kwargs.pop('quantity')):
        if mode == 'a':
            pwd = ''.join(random.SystemRandom().choices([c for c in _alphanumeric], k=size))
        else:
            pwd = ''.join(random.SystemRandom().choices([c for c in _chars], k=size))

        print(pwd)

# %%
if __name__ == "__main__":
    mode = None
    size = 16
    quantity = 1
    
    for arg in _s.argv:
        if(arg.startswith("-m")):
            mode = arg.split("=")[1]
        elif(arg.startswith("-s")):
            size = int(arg.split("=")[1])
        elif(arg.startswith("-q")):
            quantity = int(arg.split("=")[1])

    run(mode=mode, size=size, quantity=quantity)


