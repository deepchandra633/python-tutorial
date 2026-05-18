marks=int(input("Enter Student Marks :"))
if(marks>=90 and marks<=100):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=60 and marks<70):
    grade="C"
elif(marks>=50 and marks<60):
    grade="D"
else:
    grade="F"
    print(grade)