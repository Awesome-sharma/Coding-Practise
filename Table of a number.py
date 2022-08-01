num = int(input("Give the number = "))

# method 1 - For loop
# for i in range(1,11):
#   print (num,"x",i,"=",num*i)

# method 2 - While loop
# i = 1
# while i != 11:
#   print (num,"x",i,"=",num*i)
#   i += 1

# method 3 - Recursive 
i = 1
def recurfun(i,num):
  if i <= 10:
    print (num,"x",i,"=",num*i)
    i += 1
    return recurfun(i,num)
x = recurfun(i,num)
