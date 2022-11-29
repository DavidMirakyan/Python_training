import math
import sys

def funcommonMultiple(first, second):
    commonMultiple = first * second
    for i in reversed(range(1, first * second)):
         if i % first == 0 and i % second == 0:
            commonMultiple = i
           # print(commonMultiple)
    print(commonMultiple)

funcommonMultiple(int(sys.argv[1]), int(sys.argv[2]))

#print(math.lcm(int(sys.argv[1]), int(sys.argv[2])))