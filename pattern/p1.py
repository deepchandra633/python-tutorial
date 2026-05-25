# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
print("#pattern")
for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print()

# 5 
# 5 4 
# 5 4 3
# 5 4 3 2 
# 5 4 3 2 1
print("#pattern")

for row in range(5, 0, -1):
    for col in range(5, row - 1, -1):
        print(col, end=" ")
    print()


# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
print("#pattern")

for row in range(1,6):
    for col in range(row,0,-1):
        print(col,end=" ")
    print()


# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4
# 5 5 5 5 5
print("#pattern")

p=1
for row in range(1,6):
    for col in range(1,row+1):
        print(p,end=" ")
    p+=1
    print()

# 5
# 4 4 
# 3 3 3 
# 2 2 2 2 
# 1 1 1 1 1
print("#pattern")

p=5
for row in range(1,6):
    for col in range(1,row+1):
        print(p,end=" ")
    p-=1
    print()



# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
print("#pattern")

for row in range(5,0,-1):
    for col in range(row,0,-1):
        print(col,end=" ")
    print()