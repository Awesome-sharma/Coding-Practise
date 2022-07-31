# Write a Program to check the grade of the students based on marks

# If marks <50 then Grade is F

# if marks >=50 <60 then Grade is D

# if marks >=60 <70 then Grade is C

# if marks >=70 <80 then Grade is B

# if marks >=80 <90 then Grade is A

# if marks >=90 <=100 then Grade is A+

# If marks are not in the above range then print "Invalid"

marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid")
elif marks < 50:
    print("Grade F")
elif marks >= 50 and marks < 60:
    print("Grade D")
elif marks >= 60 and marks < 70:
    print("Grade C")
elif marks >= 70 and marks < 80:
    print("Grade B")
elif marks >= 80 and marks < 90:
    print("Grade A")
else:
    print("Grade A+")
