
s1 = int(input("Enter marks of Subject 1: "))
s2 = int(input("Enter marks of Subject 2: "))
s3 = int(input("Enter marks of Subject 3: "))
s4 = int(input("Enter marks of Subject 4: "))
s5 = int(input("Enter marks of Subject 5: "))

total = s1 + s2 + s3 + s4 + s5
percentage = total / 5

print("Total Marks =", total)
print("Percentage =", percentage)

match percentage // 10:
    
    case 9 | 10:
        print("Grade A")
        
    case 8:
        print("Grade B")
        
    case 7:
        print("Grade C")
        
    case 6:
        print("Grade D")
        
    case _:
        print("Fail")