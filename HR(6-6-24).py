'''
indentify srting

if __name__ == '__main__':
    s = input()
    print(any(i.isalnum() for i in s) )
    print(any(i.isalpha() for i in s) )
    print(any(i.isdigit() for i in s) )
    print(any(i.islower() for i in s) )
    print(any(i.isupper() for i in s) )
'''


"""
all about wrap function, wrap function return a string with a given width, the line contain exact same no. of word given in width
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width) #///textwrap.fill (string i/p, width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

i/p
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
o/p

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""

"""
i/p = 9rows  27colum


n, m = map(int,input().split())
for i in range(n//2):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))
    
    
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
    
print('WELCOME'.center(m,'-'))
for i in reversed(range(n//2)):
    j = int((2*i)+1)
    print(('.|.'*j).center(m, '-'))

----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------ 
"""




