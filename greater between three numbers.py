a = int(input("give value a = "))
b = int(input("give value b = "))
c = int(input("give value c = "))

# Method 1
if a == b == c:
  print("all values are equal !!")
elif a>b>c:
  print("a is greater")
elif a<b<c:
  print("c is greater")
else:
  print("b is greater")

# Method 2
# if a == b == c:
#   print("all values are equal !!")
# else:
#   print(max(a,max(b,c)))
