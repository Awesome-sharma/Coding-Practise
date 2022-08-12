# Given an array of integers, determine whether each is a power of 2,
# where powers of 2 are [1, 2, 4, 8, 16, 32, 64,...].
# For each integer evaluated, append to an array a value of 1 if the number is a power of 2 or 0 otherwise.
# Example
# arr = [1, 3, 8, 12, 16]
# 1 = 20, 8 = 23 and 16 = 24. The return array is [1, 0, 1, 0, 1].

def powerof2(n):
    if(n==0):
        return 0
    while(n!=1):
        if(n%2!=0):
            return 0
        n=n//2
    return 1

def power(arr):
    l=[]
    for i in range(len(arr)):
        if(arr[i]==1):
            l.append(1)
        else:
            l.append(powerof2(arr[i]))
    return l

n=int(input())
arr=[]
for i in range(n):
    l=int(input())
    arr.append(l)
print(arr)
print(power(arr))
