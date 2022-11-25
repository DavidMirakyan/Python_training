import sys

word = sys.argv[1]
char = sys.argv[2]

charCount = 0

for i in range(len(word)):
    if word[i] == char:
        charCount += 1
print('Get character count in word by loop result: ', charCount)

print('Get character count in word by count() function: ', word.count(char))
