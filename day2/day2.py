import sys
sys.path.append('..')
from functions import openWrite as o

values = o.open_file('day2.txt')

# Part A

dic = {}

for i in range(len(values)): 
    directions, distance = values[i].split(" ")

    if directions in dic:
        dic[directions] += int(distance)
    elif directions == 'up': 
        dic['down'] -= int(distance)
    else:
        dic[directions] = int(distance)

print('Part A:', dic['forward'] * dic['down'])

# Part B
aim = 0
forward = 0
depth = 0

for i in range(len(values)): 
    direction, distance = values[i].split(" ")

    if direction == 'forward':
        current_forward = int(distance)
        forward += current_forward
        depth += (aim*current_forward)

    elif direction == 'down':
        aim += int(distance)
        
    else:
        aim -= int(distance)

print('Part B:', forward * depth)
