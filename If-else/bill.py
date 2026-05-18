unit=int(input("Enter The total  Units consumed :"))

if(unit<=20):
    bill=unit*8
    print(bill,"is your total electricity bill ")
elif(unit>20 and unit<=40):
    bill=unit*10
    print(bill,"is your total electricity bill ")
else:
    bill=unit*12
    print(bill,"is your total electricity bill ")