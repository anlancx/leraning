import random

def display(balls):
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end='')
        print(f'{ball:0>2d}',end='')
    print()

def random_select():
    red_balls = [x for x in range(1,34)]
    select_balls = random.sample(red_balls,6)
    select_balls.sort() #排序
    select_balls.append(random.randint(1,16))
    return select_balls

n = int(input('机选几注：'))
for _ in range(n):
    display(random_select())