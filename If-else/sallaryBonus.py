sal=float(input("Enter Your Salary :"))

if(sal>=50000):
    bonus=(sal*20)/100
    total_sal=sal+bonus
    print(total_sal," is your total salary with the bonus amount :")
else:
    bonus=(sal*10)/100
    total_sal=sal+bonus
    print(total_sal," is your total salary with the bonus amount :")