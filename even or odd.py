# WAP to check number is even or odd.\

# Method 1
num = int(input("Enter a Number:"))
if num % 2 == 0:
    print("Given number is Even")
else:
    print("Given number is Odd")
    
# Method 2

num = int(input("give input = "))

print("Given number is Even" if num%2 == 0 else "Given number is Odd")
