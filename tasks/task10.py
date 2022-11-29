import math
import sys


def funcommonDivisor(first, second):
    commonDivisor = 1

    for i in range(1, second+1):
        if first % i == 0 and second % i == 0:
             commonDivisor = i
            # print(commonDivisor)
    print(commonDivisor)

funcommonDivisor(int(sys.argv[1]), int(sys.argv[2]))

# print(math.gcd(int(sys.argv[1]), int(sys.argv[2])))
