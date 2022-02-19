import random
import sys

num=int(sys.argv[1])

char=[]

while len(char) < num:
    char.append(chr(random.randint(32,126+1)))

for item in char:
    print(item,end="")
