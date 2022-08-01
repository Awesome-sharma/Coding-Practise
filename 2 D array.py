R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row-wise:")

# For user input
matrix = [[int(input()) for x in range(C)] for y in range(R)]


# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()
