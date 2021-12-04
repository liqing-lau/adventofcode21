import sys
sys.path.append('..')
from functions import openWrite as o

values = o.open_file("day1.txt")

# part A
counter_A = 0

for i in range(1, len(values)):
    if values[i - 1] < values[i]:
        counter_A += 1

print(counter_A)

# part B
counter_B = 0

for i in range(len(values)):
    if sum(values[i : i+3]) < sum(values[i+1 : i+4]):
        counter_B += 1

print(counter_B)

# if __name__ == '__main__':
#     main()

