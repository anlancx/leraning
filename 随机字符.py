import random
def b():
    a = ''
    for _ in range(4):
        a += random.choice('0123456789abcdefghijklmnopqrstuvwxyz')
    return a
for _ in range(100):
    print(b())
