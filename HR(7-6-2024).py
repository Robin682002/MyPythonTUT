"""
i/p string = AABCAAADA
     k=3
def merge_the_tools(string, k):
    substring = ""
    counter = 1

    for s in string:
        if s not in substring:
                            # that no is doing main thing it checks if is there any dublicate character then it will not add that character in  the substring
         substring += s
        if counter >= k: #add the valuse in string upto the length of K
            print(substring)
            counter = 0
            substring = ""
        counter +=1




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

o/p
AB
CA
AD
"""

"""
# numbers which are stars with 789 and contain 9 digits are then all are nor no.s
#2 no.s
9587456281
1252478965
import re

total = int(input())
text = []
pattern = r'^([789]\d{9})$' #checking 789 and 9 digit

#for _ in range(total): # _ <-- this is called  throwaway it means no need of sorting 
'''
eg of throaway 
for _ in range(3):
  # This code will run 3 times without using the loop variable
  print("Looping...")
'''
for i in range(total):
    value = input()
    text.append(value)
    
for num in text:
    result = re.match(pattern, num)
    if result:
        print("YES")
    else:
        print("NO")
    
o/p = yes
mo
"""

"""
#checks the pattern of email
name, address =: This assigns the results of the function call on the right side to two variables, name and address.
email.utils.parseaddr(input()): This is the key part. Let's break it down further:
email.utils: This refers to the email.utils module in the Python standard library, which provides various utilities for working with email messages.
parseaddr(input()): This calls the parseaddr function from the email.utils module. It takes one argument, input(), which is a function used to get user input from the console.
How it Works:

The input() function prompts the user to enter an email address.
The entered email address is passed as an argument to the email.utils.parseaddr function.
The parseaddr function attempts to parse the email address and separate it into two parts:
Name (optional): This is the display name associated with the email address, enclosed in quotation marks (e.g., "John Doe").
Address: This is the actual email address, following the format user@domain.com.
The function returns a tuple containing these two components (name, address).
The returned tuple is unpacked and assigned to the variables name and address.


import re
import email.utils
n = int (input())
p = r'^[a-z][\w\-_.]*[@][a-z]+[.][a-z]{1,3}$'

for i in range(n):
    name, address = email.utils.parseaddr(input()) <-- this line is main explain in above
    if re.match(p, address):
        print(email.utils.formataddr((name, address)))
    else:
        continue
"""

"""
Key Points:

finditer returns an iterator, which is an object that you can use to loop through all the matches in the string. It's different from findall which returns a list of all matches.
Each iteration of the loop using the iterator m will provide a match object. This object contains information about the specific match, such as its starting and ending index in the string.
Example:

Python
import re

text = "The quick brown fox jumps over the lazy dog."
pattern = "dog"

# Find all non-overlapping matches of the pattern in the text
matches = re.finditer(pattern, text)

# Print the start and end indexes of each match
for match in matches:
  print(f"Match found at start index {match.start()} and end index {match.end()}")
  
i/p = 11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   


import re

n = int(input())
pattern = r'#[A-Fa-f0-9]{3,6}'
for i in range(n):
    line = input()
    m = re.finditer(pattern, line)
    for i in m:
        if i.group() == '#BED' or i.group() == '#Cab'or i.group() == '#f0f':
            continue
        print(i.group())
  
  
o/p =#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
  
"""

"""
def swap_case(s):
     x = s.swapcase() # swapcase swap the upper case into lower case

     return x
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
i didn't write the return variable like in this case return variable is x  
"""

