# Roots of a quadratic equation
# ax^2 + bx +c =0
# r1 = -b+sqrt(b^2-4ac)/2a
# r2 = -b-sqrt(b^2-4ac)/2a

# Example:

# 1 4 4
# Roots are :  -2.0 -2.0

import math
def roots_of_qe(a,b,c):
    r1= (-b+math.sqrt(pow(b,2)-(4*a*c)))//2*a
    r2= (-b-math.sqrt(pow(b,2)-(4*a*c)))//2*a
    print("Roots are : ",r1,r2)

a,b,c=map(int,input().split())
roots_of_qe(a,b,c)
