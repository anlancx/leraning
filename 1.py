"""用Python设计第一个游戏"""

import random

answer = random.randint(1,10)
counts = 3

while counts > 0:
     temp = input("不防猜一下我现在心里想的数值：")
     guess = int(temp)

     if guess == answer:
        print("对了")
        print("猜中无奖励")
        break
     else:
         if guess < answer:
            print("小啦")
         else:
            print("大了")
     counts = counts - 1

print("game over")