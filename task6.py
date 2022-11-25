import sys

num = int(sys.argv[1])

for i in range(1, num):
    for j in range(i):
        print('*', end='')
    print('')
