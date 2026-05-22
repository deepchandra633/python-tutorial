num = int(input("Enter a number: "))
digits=len(str(num))
original = num
arm = 0

while num > 0:

    digit = num % 10
    arm = arm + digit**digits
    num = num // 10

if original == arm:
    print("ArmStrong Number")

else:
    print("Not ArmStrong")


