# a=10
# b=20
# c=30
a=int(input("Enter 1st Number :"))
b=int(input("Enter 2nd Number :"))
c=int(input("Enter 3rd Number :"))

def print_average(x,y,z):
    ave=(x+y+z)/3
    # print(ave)
    return ave

ave=print_average(a,b,c)
print(ave)