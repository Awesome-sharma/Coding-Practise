# Number of integers which has exactly x divisors

def exactly_x_div(num,div):
    c=0
    for i in range(1,num+1):
        cf=0
        for j in range(1,i+1):
            if(i%j==0):
                cf+=1
        if (cf==div):
            c+=1
    return c

num=int(input())
div=int(input())
print(exactly_x_div(num,div))
