"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l=[]

    for i in s:
        l.append(i)

        l[0] = l[0].upper()

    for i in range(1,len(l)):

        if l[i-1]==" ":
            l[i] = l[i].upper()

    ans = "".join(l)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

"""

"""

minion game

def minion_game(string):
    v = 'AEIOU'
    Kevin_scores = Stuart_scores = 0
    leng = len(string)
    #list(range(leng)) # just for checking the leng by converting it in to list 
    for i in range(leng):
        if string [i] in v:
            Kevin_scores+= leng -i
        else:
            Stuart_scores+=leng-i
    if Stuart_scores > Kevin_scores:
        print(f'Stuart {Stuart_scores}')
    elif Kevin_scores > Stuart_scores:
        print(f'Kevin {Kevin_scores}')
    else:
        print("Draw")
    
   
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
"""