# Left Rotation and Right Rotation of a String
# Difficulty Level : Medium

# Given a string of size n, write functions to perform the following operations on a string-
# 1. Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
# 2. Right (Or clockwise) rotate the given string by d elements (where d <= n).

# Examples: 
# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe" 
#          Right Rotation : "ksGeeksforGee"  


# Input : s = "qwertyu" 
#         d = 2
# Output : Left rotation : "ertyuqw"
#          Right rotation : "yuqwert" 

s = input() # take input string
d = int(input()) # take value input
def LR (s,d): # Left Rotation function
  print(s[d:]+s[:d])
LR(s,d)
def RR (s,d): #Right Rotation
  print(s[-d:]+s[:-d])
RR(s,d)
