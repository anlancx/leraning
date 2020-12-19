import os
import time

content = '北京欢迎你'
while True:
    os.system('cls')
    print(content)
    time.sleep(0.2)
    content = content[1:] + content[0]
