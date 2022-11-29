import sys
import random

minimum = int(sys.argv[1])
maximum = int(sys.argv[2])

randomNumber = random.randint(minimum, maximum)
print('Generated number is ' f'{randomNumber}')

for i in range(2, randomNumber):
    if randomNumber % i == 0:
        print(f'{randomNumber} number is NOT simple')
        exit(0)
else:
    print(f'{randomNumber} number is simple')
