# Problem Statement

# Mr. Agoji plans to travel to a new city for his vacation.
# There are N number of hotels available in that city. Each hotel has information on the price/night and rating.
# Mr. Agoji has a tight budget for his trip, so he can't afford to book a costly hotel but want's the best experience in his budget range,
# so he plans different budgets for his trip.

# There are Q different budget options for hotel booking in his budget plans.
# Mr. Agoji, who is not that good at calculations, has asked for your help to decide on the bes t-rated hotel in his budget.

# You are given a list of hotel names, the price per night, and the hotel's rating.
# For different budget ranges, you have to find the best-rated hotel for Mr. Agoji.

# Note, that if two hotels in that range have the same rating, you should output the one with the lowest booking price per night,
# and no two hotels should have the same price per night.

# Input Format --
# 1 <- no. of test cases
# 4 3 <- no. of hotels and no. of budget
# a 1000 7.6 <- hotel name , price , rating
# b 750 5.1
# c 1500 8.5
# d 800 5.1
# 700 1200 <- budget ( low , high )
# 900 1600
# 500 800


Hotels , Budgets = map(int,input("Give number of hotels and Budgets = ").split()) # input like --> 4 3
H = []
B = []
for i in range(Hotels):
    h , p , r = map(str,input("Give hotel name , price , rating = ").split()) # like --> a 1000 7.6
    H.append([h,int(p),float(r)])

for i in range(Budgets):
    l , h  = map(int,input("Give hotel budget min and high = ").split()) # like --> 700 1200
    B.append([l,h])

for i in range(len(B)): # 3
    Rating = 0
    Hotel = " "
    Price = 0
    for j in range(len (H)):  # 4
        if B[i][ 0 ] <= H[j][1] and B[i][1] >= H[j][1]:
            if Rating < H[ j ] [ 2 ] or ( Rating == H[ j ] [ 2 ] and Price > H[ j ] [ 1 ]):
                Rating = H[j][2]
                Price = H[j][1]
                Hotel = H[j][0]
    print("Best Hotel in budget range",B[i][0],"to",B[i][1],"is -> ",Hotel,Price,Rating)
    
    
    
# Input --
# 1 
# 4 3 
# a 1000 7.6 
# b 750 5.1
# c 1500 8.5
# d 800 5.1
# 700 1200 
# 900 1600
# 500 800

# Output --
# Best Hotel in budget range 700 to 1200 is ->  a 1000 7.6
# Best Hotel in budget range 900 to 1600 is ->  c 1500 8.5
# Best Hotel in budget range 500 to 800 is ->   b 750 5.1
