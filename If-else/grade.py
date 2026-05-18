s1=float(input("Enter The Marks of Maths : "))
s2=float(input("Enter The Marks of Emglish : "))
s3=float(input("Enter The Marks of Hindi : "))
s4=float(input("Enter The Marks of Physics : "))
s5=float(input("Enter The Marks of Chemistry : "))

marks = s1 + s2 + s3 + s4 + s5
percentage = marks / 5

print("tota marks : ",marks)
print("Precentage : ",percentage)

if(percentage>=90):
    print("Grade :  A+")
elif(percentage>=80 and percentage<90):
     print("Grade :  A")
elif(percentage>=70 and percentage<80):
      print("Grade :  B+")
elif(percentage>=60 and percentage<70):
      print("Grade :  B") 
elif(percentage>=50 and percentage<60):
      print("Grade :  C+")
elif(percentage>=40 and percentage<50):
      print("Grade :  C")
elif(percentage>=30 and percentage<40):
      print("Grade :  D")
else:
      print("Fail")
      
