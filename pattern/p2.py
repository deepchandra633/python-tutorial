#         1
#       1 2 
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5
print("#pattern")

# rows=5
# for row in range(1,rows+1):
#     print("  "*(rows-row),end="")
#     for col in range(row,0,-1):
#         print(col,end=" ")
#     print()

#         1
#       2 1
#     3 2 1
#   4 3 2 1
# 5 4 3 2 1
# print("#pattern")

# rows=5
# for row in range(1,rows+1):
#     print("  "*(rows-row),end="")
#     for col in range(1,row+1):
#         print(col,end=" ")
#     print()


#         1
#       2 2
#     3 3 3 
#   4 4 4 4 
# 5 5 5 5 5
print("#pattern")


# rows=5
# p=1
# for row in range(1,rows+1):
#     print("  "*(rows-row),end="")
#     for col in range(row,0,-1):
#         print(p,end=" ")
#     p+=1
#     print()

#         5
#       4 4
#     3 3 3
#   2 2 2 2
# 1 1 1 1 1
print("#pattern")

 
# rows=5
# p=5
# for row in range(1,rows+1):
#     print("  "*(rows-row),end="")
#     for col in range(row,0,-1):
#         print(p,end=" ")
#     p-=1
#     print()


#         5
#       4 5
#     3 4 5
#   2 3 4 5
# 1 2 3 4 5 


# for row in range(5,0,-1):
#     print("  "*(row-1),end="")
#     for col in range(row,6):
#         print(col,end=" ")
#     print()



# * * * * *
# *     *
# *   *
# * *
# *

for row in range(6,0,-1):
    for col in range(1,row+1):
        if row==6 or col==1 or row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


