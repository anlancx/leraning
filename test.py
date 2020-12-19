items = ['Python', 'Java', 'Go', 'Swift']

for index in range(len(items)):
    print(f'{index}:{items[index]}')

for index, item in enumerate(items):
    print(f'{index}:{item}')