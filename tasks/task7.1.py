import sys

num = int(sys.argv[1])

for i in range(num):
    for j in range(i):
        print(' ', end='')
    for k in range(num-i):
        print('*', end=' ')
    print('')
