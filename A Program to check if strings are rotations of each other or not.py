# A Program to check if strings are rotations of each other or not

# Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?

# eg given s1 = ABCD and s2 = CDAB, return true
# given s1 = ABCD, and s2 = ACBD , return false


s1 = input()
s2 = input()

def rotate(s1,L1):
  for i in range(L1):
    return (s1[-1]+ s1[:-1])
    
def check_rotate(s1,s2):
  L1 = len(s1)
  l = L1
  L2 = len(s2)
  if L1 != L2:
    print("false")
  else:
    for i in range(L1):
      s1 = rotate(s1,L1)
      if s1 == s2:
        print("true")
        break
      else:
        l -= 1
        if l == 0:
          print("false")
          break
check_rotate(s1,s2)
