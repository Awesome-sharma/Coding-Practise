# Minimum rotations required to get the same string

# Difficulty Level : Medium

# Given a string, we need to find the minimum number of rotations required to get the same string.

# Examples: 
# Input : s = "geeks"
# Output : 5

# Input : s = "aaaa"
# Output : 1


s = input()
def rotate(s):
  s1 = s
  count = 1
  for i in range(len(s)):
    s1 = s1[1:]+s1[:1]  # Slicing
    if s1 == s:
      print(count)
      break
    else:
      count += 1

rotate(s)
